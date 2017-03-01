import turtle

BASE_GIF = 'base.gif'

class Turtle(turtle.RawTurtle):
    def __init__(self, robot, canvas=turtle.Screen()):
        self.canvas = canvas
        self.canvas.register_shape(BASE_GIF)
        self.canvas.tracer(0, 0)
        turtle.RawTurtle.__init__(self, self.canvas, BASE_GIF)

        self.speed(0)
        self.robot = robot

    def draw(self):
        self._clear_and_return()

        for angles in self.robot.q:
            for l, q in zip(self.robot.l, angles):
                self.dot()
                self.left(q)
                self.forward(l)
            self.draw_hand()
            self.home()
            self.pendown()

        self.canvas.update()

    def draw_hand(self):
        x,y = self.pos()
        self.dot()

        for turn in (90, -90):
            self.left(turn)
            self.forward(10)
            self.right(turn)
            self.forward(20)

            self.penup()
            self.setpos(x,y)
            self.pendown()

        self.penup()

    def _clear_and_return(self):
        self.home()
        self.clear()
        self.pendown()

def get_input(text='', title='input'):
    return turtle.simpledialog.askstring(title, text)

def give_output(*args):
    turtle.simpledialog.messagebox.showinfo('output', ' '.join(str(arg) for arg in args))

print = give_output
input = get_input