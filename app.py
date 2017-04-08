#!/usr/bin/env python3.6
import argparse
import smooth
import handdraw
import mymath
import math
import tkinter as tk
import numpy as np

INPUT_FILE = 'input.txt'

########################################################################


def read_file(file_name):
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

            # added
            'jacob': np.zeros((3, 3)),
            'torque': np.zeros((3, 1)),
            'specific_q2': np.zeros(3)
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


def get_working_area(robot, step):
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


class App(tk.Frame):

    def __init__(self):
        self.root = tk.Tk()

        tk.Frame.__init__(self, master=self.root, takefocus=True)
        self.pack()

        # handdraw canvas
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack(side='right')
        self.drawer = handdraw.Drawer({})

        # plot canvas
        pass

        # buttons
        self.btn_update = tk.Button(self, text='update')
        self.btn_update.pack(side='bottom')
        self.btn_update.bind('<Button-1>', self.update_data)

        # labels
        self.lbl_torq1 = tk.Label(self, text='torque1')
        self.lbl_torq1.pack(side='bottom')

        self.lbl_torq2 = tk.Label(self, text='torque2')
        self.lbl_torq2.pack(side='bottom')

        self.lbl_torq2 = tk.Label(self, text='torque2')
        self.lbl_torq2.pack(side='bottom')

    def update_data(self, event):
        self.robot = read_file(self.args.input_file)

        # update draw
        self.drawer.draw()

        # update plot
        x, y = get_working_area(robot=self.robot, step=self.args.step)
        raise NotImplementedError()

    def get_args(self):
        parser = argparse.ArgumentParser()

        parser.add_argument('input_file', nargs='?', default=INPUT_FILE)
        parser.add_argument('-s', '--step', nargs='?', default=3)

        self.args = parser.parse_args()


if __name__ == '__main__':
    App().mainloop()
