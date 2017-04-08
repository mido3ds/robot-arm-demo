import mymath
import numpy as np
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


class gl:
    ''' globals '''
    @staticmethod
    def reset():
        gl.pos = 0
        gl.p2, gl.p3, gl.p4 = Point(0, 0), Point(0, 0), Point(0, 0)
        gl.lq1, gl.lq2, gl.lq3 = None, None, None
        gl.arr = 0
        gl.l = 0


def nums_in_range(start, end, step):
    n = end - start + 1
    result = n // step

    if n % step == 0:
        return result
    else:
        return result + 1


def _calc_xy(q1, q2, q3):
    if q1 != gl.lq1:
        gl.p2 = Point(
            gl.l[0] * mymath.cosd(q1),
            gl.l[0] * mymath.sind(q1)
        )
    if q2 != gl.lq2:
        gl.p3 = Point(
            gl.p2.x + gl.l[1] * mymath.cosd(q1 + q2),
            gl.p2.y + gl.l[1] * mymath.sind(q1 + q2)
        )

    p4 = Point(
        gl.p2.x + gl.p3.x + gl.l[2] * mymath.cosd(q1 + q2 + q3),
        gl.p2.y + gl.p3.y + gl.l[2] * mymath.sind(q1 + q2 + q3)
    )

    # store it in array
    gl.arr[gl.pos, 0] = p4.x
    gl.arr[gl.pos, 1] = p4.y

    gl.pos += 1


def get_xy(q1, q2, q3, l, step):
    '''return x,y numpy.arrays of points to be plotted
        step: int, step of iteration
    '''

    gl.reset()

    size = nums_in_range(*q1, step) * nums_in_range(*q2, step) * nums_in_range(*q3, step)
    gl.arr = np.zeros((size, 2))
    gl.l = l

    for i1 in range(q1[0], q1[1] + 1, step):
        for i2 in range(q2[0], q2[1] + 1, step):
            for i3 in range(q3[0], q3[1] + 1, step):
                _calc_xy(i1, i2, i3)

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
