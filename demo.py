from robot import Robot

r = Robot([], [])
while True:
    print("enter robot details")

    l = [float(num) for num in input('lengths: ').split(' ')]
    q = [float(num) for num in input('angles: ').split(' ')]

    r.reset(l, q)
    r.draw()

    print()