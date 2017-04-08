'''intended to optimize robotics project plotting, still no effect'''
import numpy as np
import mymath
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


class gl:
    ''' globals '''
    pos = 0
    p2, p3, p4 = Point(0, 0), Point(0, 0), Point(0, 0)
    li1, li2, li3 = None, None, None

    @staticmethod
    def reset():
        gl.pos = 0
        gl.p2, gl.p3, gl.p4 = Point(0, 0), Point(0, 0), Point(0, 0)
        gl.li1, gl.li2, gl.li3 = None, None, None


def get_xy(q1, q2, q3, l, step=3):
    '''return x,y numpy.arrays of points to plot

        @param: step: int, step of iteration
    '''
    gl.reset()

    def nums_in_range(start, end):
        n = end - start + 1
        result = int(n / step)

        if n % step == 0:
            return result
        else:
            return result + 1

    def get_size():
        return nums_in_range(*q1) * nums_in_range(*q2) * nums_in_range(*q3)

    size = get_size()
    arr = np.zeros((size, 2))

    def calc_xy(i1, i2, i3):
        if i1 != gl.li1:
            gl.p2 = Point(
                l[0] * mymath.cosd(i1),
                l[0] * mymath.sind(i1)
            )
        if i2 != gl.li2:
            gl.p3 = Point(
                gl.p2.x + l[1] * mymath.cosd(i1 + i2),
                gl.p2.y + l[1] * mymath.sind(i1 + i2)
            )

        p4 = Point(
            gl.p2.x + gl.p3.x + l[2] * mymath.cosd(i1 + i2 + i3),
            gl.p2.y + gl.p3.y + l[2] * mymath.sind(i1 + i2 + i3)
        )

        # store it in array
        arr[gl.pos, 0] = p4.x
        arr[gl.pos, 1] = p4.y

        gl.pos += 1

    for i1 in range(q1[0], q1[1] + 1, step):
        for i2 in range(q2[0], q2[1] + 1, step):
            for i3 in range(q3[0], q3[1] + 1, step):
                calc_xy(i1, i2, i3)

    x = arr[:, 0].view()
    y = arr[:, 1].view()
    return x, y

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    x, y = get_xy((-90, 90), (-90, 90), (-90, 90), [20, 20, 20], 4)
    plt.plot(x, y, '.g')
    plt.show()
