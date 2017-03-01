import tkinter as tk
from robot import Robot
import turtle

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

        tk.Button(self, text='hello button').pack()

        self.make_robot()
        self.make_canvas()
        self.draw()

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
        self.canvas = turtle.Canvas(self)
        self.canvas.pack()

        self.pen = turtle.RawTurtle(self.canvas)
        self.pen.hideturtle()

        self.pen.speed(0)

    def draw(self):
        self._clear_and_return()

        for angles in self.robot.q:
            for l, q in zip(self.robot.l, angles):
                self.pen.dot()
                self.pen.left(q)
                self.pen.forward(l)
            self._draw_hand()
            self.pen.home()
            self.pen.pendown()

        self.canvas.update()

    def _draw_hand(self):
        x,y = self.pen.pos()
        self.pen.dot()

        for turn in (90, -90):
            self.pen.left(turn)
            self.pen.forward(10)
            self.pen.right(turn)
            self.pen.forward(20)

            self.pen.penup()
            self.pen.setpos(x,y)
            self.pen.pendown()

        self.pen.penup()

    def _clear_and_return(self):
        self.pen.home()
        self.pen.clear()
        self.pen.pendown()

App().mainloop()