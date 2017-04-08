#!/usr/bin/env python3.6
import argparse
import os.path as path
import working_area
import handdraw

import mymath
import numpy as np

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk


class Conf:
    input_file = path.join(path.dirname(path.realpath(__file__)), 'input.txt')
    step = 6

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
        }
    except:
        raise Exception('cant get variables from file,'
                        ' some are not found')

    return robot

########################################################################


def calc_inverse_km(robot):
    ''' return q1, q2 (each is 1D array) from l, a,b, theta  '''
    theta = robot['theta']
    l1 = robot['l'][0]

    a1 = robot['a'] - l3 * np.cos(theta)
    b1 = robot['b'] - l3 * np.sin(theta)
    r = mymath.hypotenuse(a1, b1)

    q1 = _calc_inverse_km(a1, b1, r, l1, theta, +alpha)
    q2 = _calc_inverse_km(a1, b1, r, l1, theta, -alpha)
    return q1, q2


def _calc_inverse_km(a1, b1, r, l1, theta, alpha):
    ''' get one part '''
    q1 = mymath.atan2d(b1 / a1) - alpha
    q2 = mymath.atan2d((r * np.sin(alpha)) / (r * np.acos(alpha) - l1))
    q3 = theta - q1 - q2
    return np.array([q1, q2, q3])

########################################################################


def get_working_area(robot, step):
    ''' return all x, y of end effector to plot '''
    return working_area.get_xy(
        q1=robot['q'][0],
        q2=robot['q'][1],
        q3=robot['q'][2],
        l=robot['l'],

        step=step,
    )

########################################################################


def calc_torque(robot):
    ''' 3x1 matrix, Q = -J.T x Pex '''
    robot['torque'] = np.matmul(-1 * robot['jacob'].transpose(), robot['pex'])


def calc_jacobian(robot):
    ''' 3x3 matrix, see slide num 4 page 12 '''
    get_dr = lambda ls, qs, func: np.array(
        [ls[i] * func(sum(qs[:i + 1])) for i in range(3)])

    dr1 = -1 * get_dr(robot['l'], robot['specific_q'], mymath.sind)
    dr2 = get_dr(robot['l'], robot['specific_q'], mymath.cosd)

    robot['jacob'] = np.mat([
        [sum(dr1[i:]) for i in range(3)],
        [sum(dr2[i:]) for i in range(3)],
        [1, 1, 1]
    ])

########################################################################


def calc_all(robot):
    ''' cal all missing data for robot, then return it '''
    calc_jacobian(robot)
    calc_torque(robot)
    return robot

########################################################################


class App(tk.Frame):

    def __init__(self):
        self.root = tk.Tk()
        self.root.wm_title('Robotics Project')

        tk.Frame.__init__(self, master=self.root, takefocus=True)
        self.pack()

        self.get_args()

        # handdraw canvas
        self.drw_canvas = tk.Canvas(self, width=400, height=400)
        self.drw_canvas.pack(side='right')
        self.drawer = handdraw.Drawer({}, self.drw_canvas)

        # plot canvas
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.subplt = self.fig.add_subplot(111)
        self.plt_canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.plt_canvas.show()
        self.plt_canvas.get_tk_widget().pack(side='left', fill=tk.BOTH, expand=1)
        self.plt_canvas._tkcanvas.pack(side='left', fill=tk.BOTH, expand=1)

        # buttons
        self.btn_update = tk.Button(self, text='update')
        self.btn_update.pack(side='bottom')
        self.btn_update.bind('<Button-1>', self.update_ui)

        # labels
        self.lbl_torq3 = tk.Label(self)
        self.lbl_torq3.pack(side='bottom')
        tk.Label(self, text='torque3').pack(side='bottom')

        self.lbl_torq2 = tk.Label(self)
        self.lbl_torq2.pack(side='bottom')
        tk.Label(self, text='torque2').pack(side='bottom')

        self.lbl_torq1 = tk.Label(self)
        self.lbl_torq1.pack(side='bottom')
        tk.Label(self, text='torque1').pack(side='bottom')

        # update once
        self.update_ui(None)

    def update_ui(self, event):
        self.robot = read_file(self.args.input_file)
        self.robot = calc_all(self.robot)

        # labels
        self.lbl_torq1['text'] = self.robot['torque'][0, 0]
        self.lbl_torq2['text'] = self.robot['torque'][1, 0]
        self.lbl_torq3['text'] = self.robot['torque'][2, 0]

        # draw
        self.drawer.robot = self.robot
        self.drawer.draw()

        # plot
        x, y = get_working_area(robot=self.robot, step=self.args.step)

        self.fig.clear()
        self.subplt = self.fig.add_subplot(111)

        self.subplt.plot(x, y, 'g.')
        self.plt_canvas.draw()


    def get_args(self):
        parser = argparse.ArgumentParser()

        parser.add_argument('input_file', nargs='?', default=Conf.input_file)
        parser.add_argument('-s', '--step', nargs='?',
                            default=Conf.step, type=int)

        self.args = parser.parse_args()


if __name__ == '__main__':
    App().mainloop()
