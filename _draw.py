import turtle

pen = turtle.Turtle()

pen.hideturtle()
pen.color('black')
pen.speed(0)
turtle.tracer(0, 0)

def draw(robot):
    _clear()

    for angles in robot.q:
        for l, q in zip(robot.l, angles):
            pen.dot()
            pen.left(q)
            pen.forward(l)
        _draw_hand()
        pen.home()
        pen.pendown()

    turtle.update()

def _draw_hand():
    x,y = pen.pos()
    pen.dot()

    for turn in (90, -90):
        pen.left(turn)
        pen.forward(10)
        pen.right(turn)
        pen.forward(20)

        pen.penup()
        pen.setpos(x,y)
        pen.pendown()

    pen.penup()

def _clear():
    pen.clear()
    pen.home()
    pen.pendown()