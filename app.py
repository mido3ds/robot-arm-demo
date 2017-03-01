import tkinter as tk
from robot import Robot
import draw


class App(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        tk.Frame.__init__(self, master=self.root)
        self.pack()

        tk.Button(self, text='hello button').pack()

        self.make_robot()
        self.make_canvas()

    def make_robot(self):
        dialog = input().split(';')
        for i, part in enumerate(dialog):
            dialog[i] = [float(num) for num in part.strip(' ').split(' ')]

        if len(dialog) == 2:
            self.robot = Robot(l=dialog[0], q=dialog[1])
        elif len(dialog) == 3:
            self.robot = Robot(l=dialog[0], a=dialog[1][0], b=dialog[2][0])
        elif len(dialog) == 4:
            self.robot = Robot(l=dialog[0], a=dialog[1][0], b=dialog[2][0], theta=dialog[3])


    def make_canvas(self):
        self.canvas = tk.Canvas(self)
        self.canvas.pack()

        self.pen = draw.Turtle(robot=self.robot, canvas=self.canvas)


App().mainloop()