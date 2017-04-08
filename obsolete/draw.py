import turtle

class Turtle(turtle.RawTurtle):
    def __init__(self, robot, canvas):
        self.canvas = canvas
        turtle.RawTurtle.__init__(self, canvas=self.canvas)
        self.hideturtle()

        self.speed(0)
        self.robot = robot

    def draw(self):
        self._clear_and_return()

        for angles in self.robot.q:
            for l, q in zip(self.robot.l, angles):
                self.dot()
                self.left(q)
                self.forward(l)
            self._draw_hand()
            self.home()
            self.pendown()

        self.canvas.update()

    def _draw_hand(self):
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