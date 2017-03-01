import turtle

class Turtle:
    def __init__(self, robot, canvas=turtle.Screen()):
        self.canvas = canvas
        self.pen = turtle.RawTurtles(self.canvas)
        self.pen.hideturtle()
        turtle.tracer(0, 0)

        self.pen.speed(0)
        self.robot = robot

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