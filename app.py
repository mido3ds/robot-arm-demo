#!/usr/bin/env python3.6
import argparse
import smooth
import numpy as np

INPUT_FILE = 'input.txt'


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


def inverse_km(robot):
    ''' get q from l, a,b, theta  '''
    pass


def get_working_area(robot, step=3):
    ''' get 2D array of x, y to plot '''
    return smooth.get_xy(
        q1=robot['q'][0],
        q2=robot['q'][1],
        q3=robot['q'][2],
        l=robot['l'],

        step=step,
    )


def get_torque(robot):
    ''' 3x1 matrix, Q = -J.T x Pex '''
    return np.matmul(-1 * get_jacobian(robot).transpose(), robot['pex'])


def get_jacobian(robot):
    ''' 3x3 matrix, see slide num 4 page 12 '''
    pass


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
