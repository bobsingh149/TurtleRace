# todo
# pensize
# color
# move
# rotate
# shape
# speed
# setheading

from turtle import Turtle, Screen
import random

gullu = Turtle()
gullu.color('black')
gullu.shape('turtle')

screen = Screen()

screen.setup(width=700, height=600)

screen.colormode(255)

dis = 30


def getcolor():
    col = list()

    for c in range(3):
        col.append(random.randint(0, 255))

    return tuple(col)


def changecolor():
    gullu.color(getcolor())


def pensizeup():
    print(gullu.pensize())
    gullu.pensize(gullu.pensize() + 1)
    print(gullu.pensize())


def pensizedown():
    gullu.pensize(gullu.pensize() - 1)


def forward():
    print('go forward')
    gullu.forward(dis)


def back():
    gullu.back(dis)


def getheading():
    return gullu.heading()


def clockwise():
    gullu.setheading(getheading() + 30)


def anticlock():
    gullu.setheading(getheading() - 30)


def clear():
    gullu.clear()
    gullu.penup()
    gullu.home()
    gullu.pendown()


def canvas():
    screen.listen()

    screen.onkey(key='w', fun=forward)
    screen.onkey(key='s', fun=back)
    screen.onkey(key='d', fun=anticlock)
    screen.onkey(key='a', fun=clockwise)
    screen.onkey(key='n', fun=pensizeup)
    screen.onkey(key='m', fun=pensizedown)
    screen.onkey(key='c', fun=changecolor)
    screen.onkey(key='q', fun=clear)


canvas()
screen.exitonclick()
