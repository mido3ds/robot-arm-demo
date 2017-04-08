#!/usr/bin/env python3.6
import argparse
import smooth
import mymath
import math
import numpy as np

INPUT_FILE = 'input.txt'

########################################################################


def read_file(file_name=INPUT_FILE):
    try:
        with open(file_name) as f:
            inp = f.read()
    except:
        raise Exception('cant open file, '
                        'file name should be input.txt '
                        'and be in the same folder')

    try:
        exec(inp)
    except:
        raise Exception('cant read file')

    try:
        robot = {
            'mode': locals()['mode'],

            'l': np.array(locals()['l']),  # 1D array
            'theta': locals()['θ'],

            'specific_q': np.array(locals()['specific_q']),  # 1D array
            'pex': np.matrix(locals()['Pex']).transpose(),  # 2D 3x1 matrix

            'q': locals()['q'],
            'a': locals()['a'],
            'b': locals()['b'],
        }
    except:
        raise Exception('cant get variables from file,'
                        ' some are not found')

    return robot

########################################################################


def get_inverse_km(robot):
    ''' return q1, q2 (each is 1D array) from l, a,b, theta  '''
    theta = robot['theta']
    l1 = robot['l'][0]

    a1 = robot['a'] - l3 * math.cos(theta)
    b1 = robot['b'] - l3 * math.sin(theta)
    r = mymath.hypotenuse(a1, b1)

    q1 = _get_inverse_km(a1, b1, r, l1, theta, +alpha)
    q2 = _get_inverse_km(a1, b1, r, l1, theta, -alpha)
    return q1, q2


def _get_inverse_km(a1, b1, r, l1, theta, alpha):
    q1 = mymath.atan2d(b1 / a1) - alpha
    q2 = mymath.atan2d((r * math.sin(alpha)) / (r * math.acos(alpha) - l1))
    q3 = theta - q1 - q2
    return np.array([q1, q2, q3])

########################################################################


def get_working_area(robot, step=3):
    ''' return all x, y of end effector to plot '''
    return smooth.get_xy(
        q1=robot['q'][0],
        q2=robot['q'][1],
        q3=robot['q'][2],
        l=robot['l'],

        step=step,
    )

########################################################################


def calc_torque(robot):
    ''' 3x1 matrix, Q = -J.T x Pex '''
    calc_jacobian()
    robot['torque'] = np.matmul(-1 * robot['jacob'].transpose(), robot['pex'])


def calc_jacobian(robot):
    ''' 3x3 matrix, see slide num 4 page 12 '''
    robot['jacob'] = None
    raise NotImplementedError()

########################################################################


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', nargs='?')
    return parser


def main(args):
    pass

if __name__ == '__main__':
    args = build_parser().parse_args()
    INPUT_FILE = args.input_file or INPUT_FILE

    main(args)
