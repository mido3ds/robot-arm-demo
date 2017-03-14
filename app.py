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
        self.grid()

        self.make_canvas()
        self.make_buttons()

    def make_buttons(self):
        self.le = tk.Entry(self)
        tk.Label(self, text='length').grid()
        self.le.grid()

        self.qe = tk.Entry(self)
        tk.Label(self, text='angles').grid()
        self.qe.grid()

        self.thetae = tk.Entry(self)
        tk.Label(self, text='theta').grid()
        self.thetae.grid()

        self.abe = tk.Entry(self)
        tk.Label(self, text='a and b').grid()
        self.abe.grid()

        self.subm_butt = tk.Button(self, text='Make Robot')
        self.subm_butt.grid()
        self.subm_butt.bind('<Button-1>', self.get_data)

    def get_data(self, event):
        self.data = []
        for entry in [self.le, self.qe, self.abe, self.thetae]:
            text = entry.get()
            if text != '':
                try:
                    self.data.append([float(num) for num in text.strip(' ').split(',')])
                except:
                    tk.messagebox.showerror('Error', 'entered numbers are not correct, please try again')
        self.make_robot()
        self.pen.draw()

    def make_robot(self):
        dialog = self.data
        if len(dialog) == 2:
            self.robot = Robot(l=dialog[0], q=dialog[1])
        elif len(dialog) == 3:
            self.robot = Robot(l=dialog[0], a=dialog[1][0], b=dialog[2][0])
        elif len(dialog) == 4:
            self.robot = Robot(l=dialog[0], a=dialog[1][0], b=dialog[1][1], theta=dialog[2])
        self.pen.robot = self.robot

    def make_canvas(self):
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.grid()

        self.pen = draw.Turtle(None, self.canvas)

App().mainloop()