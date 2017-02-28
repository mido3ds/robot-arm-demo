from robot import Robot
import robot

while True:
    print("enter robot details")

    l = [float(num) for num in input('lengths: ').split(' ')]
    q = [float(num) for num in input('angles: ').split(' ')]

    robot._draw.clear()
    r = Robot(l=l, q=q)
    r.draw()

    print()