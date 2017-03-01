import tkinter as tk

class App(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        tk.Frame.__init__(self, master=self.root)
        self.pack()

        

App().mainloop()