import turtle

pen = turtle.Turtle()

pen.hideturtle()
pen.color('black')
pen.speed(0)

def draw(robot):
    for l, q in zip(robot.conf['l'], robot.conf['q']):
        pen.dot()
        pen.left(q)
        pen.forward(l)

    draw_hand()

    pen.home()

def draw_hand():
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

def clear():
    pen.clear()
    pen.home()