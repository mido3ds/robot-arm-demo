import numpy as np


def acosd(x):
    return np.degrees(np.acos(x))


def asind(x):
    return np.degrees(np.asin(x))


def atan2d(x):
    return np.degrees(np.atan2(x))


def atand(x):
    return np.degrees(np.atan(x))


def sind(x):
    return np.sin(np.radians(x))


def cosd(x):
    return np.cos(np.radians(x))


def tand(x):
    return np.tan(np.radians(x))


def alpha(l1, l2, r):
    return acosd((l1 ** 2 + r ** 2 - l2 ** 2) / 2 * l1 * r)


def hypotenuse(a, b):
    ''' return length of hypotenuse in right angle '''
    return np.sqrt(a ** 2 + b ** 2)
