from robot import Robot

while True:
    print("enter robot details")

    lengths = [float(num) for num in input('lengths: ').split(' ')]
    angles = [float(num) for num in input('angles: ').split(' ')]

    r = Robot(l=lengths, q=angles)
    r.draw()

    print()