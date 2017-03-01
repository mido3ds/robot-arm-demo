from robot import Robot
from _draw import input, print

while True:
    dialog = input().split(';')
    for i, part in enumerate(dialog):
        dialog[i] = [float(num) for num in part.strip(' ').split(' ')]

    if len(dialog) == 2:
        r = Robot(l=dialog[0], q=dialog[1])
    elif len(dialog) == 3:
        r = Robot(l=dialog[0], a=dialog[1], b=dialog[2])
    elif len(dialog) == 4:
        r = Robot(l=dialog[0], a=dialog[1], b=dialog[2], theta=dialog[3])

    r.draw()
    print("a =", r.a, '\nb =', r.b, '\nl =', r.l, '\nq =', r.q, '\ntheta =', r.theta)