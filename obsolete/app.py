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
        tk.Frame.__init__(self, master=self.root, takefocus=True)
        self.pack()

        self.make_canvas()
        self.make_buttons()

    def make_buttons(self):
        self.le = tk.Entry(self)
        tk.Label(self, text='lengths').pack()
        self.le.pack()

        # angles
        self.qe1 = tk.Entry(self)
        tk.Label(self, text='q1 range').pack()
        self.qe1.pack()

        self.qe2 = tk.Entry(self)
        tk.Label(self, text='q2 range').pack()
        self.qe2.pack()

        self.qe3 = tk.Entry(self)
        tk.Label(self, text='q3 range').pack()
        self.qe3.pack()

        self.thetae = tk.Entry(self)
        tk.Label(self, text='theta').pack()
        self.thetae.pack()

        self.abe = tk.Entry(self)
        tk.Label(self, text='a and b').pack()
        self.abe.pack()

        self.subm_butt = tk.Button(self, text='Make Robot')
        self.subm_butt.pack()
        self.subm_butt.bind('<Button-1>', self.get_data)

    def get_data(self, event):
        self.data = []
        for entry in [self.le, self.qe1, self.qe2, self.qe3, self.abe, self.thetae]:
            text = entry.get()
            if text != '':
                try:
                    self.data.append([float(num) for num in text.strip(' ').split(',')])
                except:
                    tk.messagebox.showerror('Error', 'entered numbers are not correct, please try again')
        self.make_robot()
        self.pen.draw()

    def get_qs():
        ''' generate q from entries '''
        for qs in self.data[1:4]:
            yield (min(qs), max(qs))


    def make_robot(self):
        dialog = self.data
        if len(dialog) == 2:
            q = [(q1, q2) for q1, q2 in get_qs()] #dialog[1,2,3]
            self.robot = Robot(l=dialog[0], q=q)
        elif len(dialog) == 3:
            self.robot = Robot(l=dialog[0], a=dialog[1][0], b=dialog[2][0])
        elif len(dialog) == 4:
            self.robot = Robot(l=dialog[0], a=dialog[1][0], b=dialog[1][1], theta=dialog[2])
        self.pen.robot = self.robot

    def make_canvas(self):
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack(side='left')

        self.pen = draw.Turtle(None, self.canvas)

App().mainloop()