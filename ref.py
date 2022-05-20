from turtle import Turtle, Screen

import heroes as h
import random

print(h.gen())


gullu = Turtle()

gullu.shape('turtle')


def square():

    for i in range(4):
        gullu.forward(100)
        gullu.right(90)


def pent():

    for i in range(7):
        gullu.forward(100)
        gullu.right(360/7)


def dash():

    for i in range(30):

        gullu.pendown()

        gullu.forward(15)

        gullu.penup()

        gullu.forward(15)


def getcolor():

    col = list()

    for c in range(3):

        col.append(random.randint(0, 255))

    return tuple(col)


def getDir():

    return random.randint(0, 1)


def getAngle():

    return random.randint(-360, 360)


def getDis():
    return random.randint(5, 100)


def drawAll():
    dis = 100
    sides = 2

    while sides < 11:

        gullu.color(getcolor())

        sides += 1
        angle = 360/sides

        for i in range(sides):

            gullu.forward(dis)
            gullu.left(angle)


def walk():

    gullu.pensize(10)
    gullu.speed('fast')
    for i in range(100):

        gullu.color(getcolor())
        gullu.forward(getDis())

        gullu.setheading(getAngle())


def circle(shift):

    gullu.speed('fastest')

    r = 100

    for i in range(int(360/shift)):
        gullu.color(getcolor())
        gullu.circle(r)
        h = gullu.heading()
        gullu.setheading(h+shift)


def start(x, y):

    gullu.hideturtle()
    gullu.penup()
    gullu.goto(x, y)
    gullu.showturtle()
    gullu.pendown()


def paint():
    gullu.speed('fastest')

    start(-300, 300)

    right = True

    rounds = 30

    radius = 10

    dis = radius*2+0.5*radius

    gap = radius+0.1*radius

    for i in range(rounds):

        for j in range(rounds):

            gullu.fillcolor(getcolor())

            gullu.begin_fill()

            gullu.circle(radius)

            gullu.penup()

            if j != rounds-1:
                gullu.forward(dis)

            gullu.pendown()
            gullu.end_fill()

        if right:
            gullu.right(90)
            gullu.penup()
            gullu.forward(gap)
            gullu.pendown()
            gullu.right(90)
        else:
            gullu.left(90)
            gullu.penup()
            gullu.forward(gap+radius*4)
            gullu.pendown()
            gullu.left(90)

        right = not right


canvas = Screen()

canvas.colormode(255)

circle(3)
# paint()

canvas.exitonclick()
