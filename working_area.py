import mymath
import multiprocessing as mpr
import numpy as np


def _nums_in_range(start, end, step):
    n = end - start + 1
    result = n // step

    if n % step == 0:
        return result
    else:
        return result + 1


def _calc_part(q1, q2, q3, l, size, step, func):
    ''' calc part of x or y, to be able to make multiprocess '''
    li1, li2 = None, None
    p2, p3, pos = 0, 0, 0

    # create array
    arr = np.zeros(size)

    for i1 in range(q1[0], q1[1] + 1, step):
        for i2 in range(q2[0], q2[1] + 1, step):
            for i3 in range(q3[0], q3[1] + 1, step):
                if i1 != li1:
                    p2 = l[0] * func(i1)
                if i2 != li2:
                    p3 = p2 + l[1] * func(i1 + i2)

                p4 = p2 + p3 + l[2] * func(i1 + i2 + i3)

                # store it in array
                arr[pos] = p4
                pos += 1

    return arr


def get_xy(q1, q2, q3, l, step):
    '''return x,y numpy.arrays of points to be plotted

        step: int, step of iteration
    '''

    size = _nums_in_range(q1[0], q1[1], step) \
        * _nums_in_range(q2[0], q1[1], step) \
        * _nums_in_range(q3[0], q1[1], step)

    with mpr.Pool() as p:
        x, y = p.starmap(_calc_part,
                         [(q1, q2, q3, l, size, step, mymath.cosd), (q1, q2, q3, l, size, step, mymath.sind)])

    return x, y


def test():
    import matplotlib.pyplot as plt
    x, y = get_xy((-90, 90), (-90, 90), (-90, 90), [20, 20, 20], 4)
    plt.plot(x, y, '.g')
    plt.show()

if __name__ == "__main__":
    test()
