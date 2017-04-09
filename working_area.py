import mymath
import numpy as np
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


class gl:
    ''' globals '''
    def __init__(self):
        self.pos = 0
        self.p2, self.p3, self.p4 = Point(0, 0), Point(0, 0), Point(0, 0)
        self.lq1, self.lq2, self.lq3 = None, None, None
        self.arr = 0
        self.l = 0
        self.size = 0


def nums_in_range(start, end, step):
    n = end - start + 1
    result = n // step

    if n % step == 0:
        return result
    else:
        return result + 1


def _calc_xy(q1, q2, q3, myglobal, step):
    for i1 in range(q1[0], q1[1] + 1, step):
        for i2 in range(q2[0], q2[1] + 1, step):
            for i3 in range(q3[0], q3[1] + 1, step):
                if i1 != myglobal.lq1:
                    myglobal.p2 = Point(
                        myglobal.l[0] * mymath.cosd(i1),
                        myglobal.l[0] * mymath.sind(i1)
                    )
                if i2 != myglobal.lq2:
                    myglobal.p3 = Point(
                        myglobal.p2.x + myglobal.l[1] * mymath.cosd(i1 + i2),
                        myglobal.p2.y + myglobal.l[1] * mymath.sind(i1 + i2)
                    )

                p4 = Point(
                    myglobal.p2.x + myglobal.p3.x + myglobal.l[2] * mymath.cosd(i1 + i2 + i3),
                    myglobal.p2.y + myglobal.p3.y + myglobal.l[2] * mymath.sind(i1 + i2 + i3)
                )

                # store it in array
                myglobal.arr[myglobal.pos, 0] = p4.x
                myglobal.arr[myglobal.pos, 1] = p4.y

                myglobal.pos += 1


def get_xy(q1, q2, q3, l, step):
    '''return x,y numpy.arrays of points to be plotted
        step: int, step of iteration
    '''

    myglobal = gl()

    myglobal.size = nums_in_range(q1[0], q1[1], step) \
        * nums_in_range(q2[0], q1[1], step) \
        * nums_in_range(q3[0], q1[1], step)

    myglobal.arr = np.zeros((myglobal.size, 2))
    myglobal.l = l

    
    _calc_xy(q1, q2, q3, myglobal, step)

    x = myglobal.arr[:, 0].view()
    y = myglobal.arr[:, 1].view()

    return x, y


def test():
    import matplotlib.pyplot as plt
    x, y = get_xy((-90, 90), (-90, 90), (-90, 90), [20, 20, 20], 4)
    plt.plot(x, y, '.g')
    plt.show()

if __name__ == "__main__":
    test()
