import turtle

BASE_GIF = 'base.gif'
turtle.Screen().register_shape(BASE_GIF)
turtle.tracer(0, 0)

pen = turtle.Turtle(shape=BASE_GIF)
pen.speed(0)

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
    pen.home()
    pen.clear()
    pen.pendown()

def get_input(text='', title='input'):
    return turtle.simpledialog.askstring(title, text)

def give_output(*args):
    turtle.simpledialog.messagebox.showinfo('output', ' '.join(str(arg) for arg in args))

print = give_output
input = get_input