import turtle

pen = turtle.Turtle()

pen.hideturtle()
pen.color('black')
pen.speed(0)

def draw(robot):
    for l, q in zip(robot.l, robot.q):
        pen.dot()
        pen.left(q)
        pen.forward(l)

    draw_hand()

    pen.home()

def draw_hand():
    x,y = pen.pos()
    pen.dot()

    pen.left(90)
    pen.forward(10)
    pen.right(90)
    pen.forward(20)

    pen.penup()
    pen.setpos(x,y)
    pen.pendown()

    pen.right(90)
    pen.forward(10)
    pen.left(90)
    pen.forward(20)

    pen.penup()

def clear():
    pen.clear()
    pen.home()