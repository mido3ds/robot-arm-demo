import tkinter as tk
import turtle 

class App(tk.Frame):
    def __init__(self):
        root = tk.Tk(screenName="hello tk", sync=2)
        tk.Frame.__init__(self, root)
        self.pack()

        tk.Button(self, text='clear', command=lambda: self.canvas.delete('all')).pack()
        tk.Button(self, text='draw', command=lambda: self.canvas.create_line(200, 300, 500, 100)).pack()
        tk.Button(self, text='show me an egg warning', command=lambda: tk.messagebox.showwarning('title', 'this is the message')).pack(side='right')

        self.tr = turtle.Canvas(self)
        self.tr.pack()

        pen = turtle.RawTurtle(self.tr)
        pen.speed(0)
        pen.forward(500)

        self.canvas = tk.Canvas(self, bg='white', height=600, width=600)
        self.canvas.pack()

        
        
    def update(self, event):
        self.canvas.delete('all')


App().mainloop()