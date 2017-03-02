import tkinter as tk
from robot import Robot
import draw

def get_input(text='', title='input'):
    return tk.simpledialog.askstring(title, text)

def give_output(*args):
    tk.simpledialog.messagebox.showinfo('output', ' '.join(str(arg) for arg in args))

print = give_output
input = get_input

class App(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        tk.Frame.__init__(self, master=self.root)
        self.pack()

        self.make_robot()
        self.make_canvas()
        self.pen.draw()

    def make_robot(self):
        input = lambda: '100 200; 20 30'
        dialog = input().split(';')
        for i, part in enumerate(dialog):
            dialog[i] = [float(num) for num in part.strip(' ').split(' ')]

        if len(dialog) == 2:
            self.robot = Robot(l=dialog[0], q=dialog[1])
        elif len(dialog) == 3:
            self.robot = Robot(l=dialog[0], a=dialog[1][0], b=dialog[2][0])
        elif len(dialog) == 4:
            self.robot = Robot(l=dialog[0], a=dialog[1][0], b=dialog[2][0], theta=dialog[3])

    def animate_360(self):
        for q0 in range(0, 360):
            for q1 in range(0, 360):
                self.robot.q[0][0] = q0
                self.robot.q[0][1] = q1
                self.pen.draw()


    def make_canvas(self):
        self.canvas = draw.turtle.Canvas(self, width=800, height=800)
        self.canvas.pack()

        self.pen = draw.Turtle(self.robot, self.canvas)

App().mainloop()