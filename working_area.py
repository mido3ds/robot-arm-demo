import mymath
import multiprocessing as mpr
import numpy as np
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


class gl:
    ''' globals namespace '''
    arr = None
    l = None
    step = None


def _nums_in_range(start, end, step):
    n = end - start + 1
    result = n // step

    if n % step == 0:
        return result
    else:
        return result + 1


def _calc_xy(q1, q2, q3, pos):
    ''' calc part of xy, to be able to make multiprocess '''
    lq1, lq2 = None, None
    p2, p3 = Point(0, 0), Point(0, 0)

    print('i have started', 'l is {}'.format(gl.l), 'arr is {}'.format(gl.arr), 'pos is {}'.format(pos))
    for i1 in range(q1[0], q1[1] + 1, gl.step):
        for i2 in range(q2[0], q2[1] + 1, gl.step):
            for i3 in range(q3[0], q3[1] + 1, gl.step):
                if i1 != lq1:
                    p2 = Point(
                        gl.l[0] * mymath.cosd(i1),
                        gl.l[0] * mymath.sind(i1)
                    )
                if i2 != lq2:
                    p3 = Point(
                        p2.x + gl.l[1] * mymath.cosd(i1 + i2),
                        p2.y + gl.l[1] * mymath.sind(i1 + i2)
                    )

                p4 = Point(
                    p2.x + p3.x +
                    gl.l[2] * mymath.cosd(i1 + i2 + i3),
                    p2.y + p3.y +
                    gl.l[2] * mymath.sind(i1 + i2 + i3)
                )

                # store it in array
                gl.arr[pos, 0] = p4.x
                gl.arr[pos, 1] = p4.y

                pos += 1
    print('i have finished', 'l is {}'.format(gl.l), 'arr is {}'.format(gl.arr), 'pos is {}'.format(pos))

def get_xy(q1, q2, q3, l, step):
    '''return x,y numpy.arrays of points to be plotted
        step: int, step of iteration
    '''

    half_q = int(np.ceil((sum(q1)) / 2))
    half_size = _nums_in_range(q1[0], half_q, step) \
        * _nums_in_range(q2[0], q1[1], step) \
        * _nums_in_range(q3[0], q1[1], step)

    gl.arr = np.zeros((half_size * 2, 2))
    gl.l = l
    gl.step = step

    mpr.Process(target=_calc_xy, args=((q1[0], half_q), q2, q3, 0)).start()
    mpr.Process(target=_calc_xy, args=((half_q, q1[1]), q2, q3, half_size)).start()

    x = gl.arr[:, 0].view()
    y = gl.arr[:, 1].view()

    return x, y


def test():
    import matplotlib.pyplot as plt
    x, y = get_xy((-90, 90), (-90, 90), (-90, 90), [20, 20, 20], 4)
    plt.plot(x, y, '.g')
    plt.show()

if __name__ == "__main__":
    test()
