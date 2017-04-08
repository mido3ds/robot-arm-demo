from robot import Robot
from draw import input, print, Turtle

while True:
    dialog = input().split(';')
    for i, part in enumerate(dialog):
        dialog[i] = [float(num) for num in part.strip(' ').split(' ')]

    if len(dialog) == 2:
        r = Robot(l=dialog[0], q=dialog[1])
    elif len(dialog) == 3:
        r = Robot(l=dialog[0], a=dialog[1][0], b=dialog[2][0])
    elif len(dialog) == 4:
        r = Robot(l=dialog[0], a=dialog[1][0], b=dialog[2][0], theta=dialog[3])

    Turtle(r).draw()
    print("a =", r.a, '\nb =', r.b, '\nl =', r.l, '\nq =', r.q, '\ntheta =', r.theta)