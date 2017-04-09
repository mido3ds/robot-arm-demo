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


def _calc_part(func):
    ''' calc part of x or y, to be able to make multiprocess '''
    global q1, q2, q3, l, step, size
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


def get_xy(robot, given_step):
    '''return x,y numpy.arrays of points to be plotted

        step: int, step of iteration
    '''
    global q1, q2, q3, l, step, size
    q1 = robot['q'][0]
    q2 = robot['q'][1]
    q3 = robot['q'][2]
    l = robot['l']
    step = given_step

    size = _nums_in_range(q1[0], q1[1], step) \
        * _nums_in_range(q2[0], q1[1], step) \
        * _nums_in_range(q3[0], q1[1], step)
    
    # make two processes
    with mpr.Pool() as p:
        x, y = p.map(_calc_part,
                     [mymath.cosd, mymath.sind])

    return x, y


def test():
    import matplotlib.pyplot as plt
    x, y = get_xy((-90, 90), (-90, 90), (-90, 90), [20, 20, 20], 4)
    plt.plot(x, y, '.g')
    plt.show()

if __name__ == "__main__":
    test()
