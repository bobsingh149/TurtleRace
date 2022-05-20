from turtle import Turtle, Screen
import random

screen = Screen()

width = 800
height = 600
screen.setup(width=width, height=height)

screen.colormode(255)

colors = ['red', 'blue', 'green', 'yellow', 'pink', 'black', 'orange']

turtles = []

dis = 30

gullu = Turtle()
gullu.penup()
gullu.shape('turtle')
gullu.color('brown')


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

    gullu.forward(getdis())


def back():
    gullu.back(getdis())


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


def init():
    y = 120
    gullu.goto(-(width / 2) + 10, y)
    y -= 30

    for i in range(len(colors)):
        t = Turtle()
        t.shape('turtle')
        t.color(colors[i])
        t.penup()
        t.goto(-(width / 2) + 10, y)
        y -= 30

        turtles.append(t)


def getspeed():
    return random.randint(0, 10)


def getdis():
    return random.randint(10, 25)



def haswon(x):
    return x >= width / 2

def race():
    while True:

        for t in turtles:
            t.speed(getspeed())
            t.forward(getdis())

            x, _ = t.pos()

            gx,_=gullu.pos()



            if haswon(gx):
                print(f'winner is gullu')

                return 'gullu'


            if haswon(x):

                print(f'winner is {t.color()[0]}')

                return t.color()[0]


bet = screen.textinput(title='Turtle Race', prompt='Place your bet choose your color: ')
print(bet)

init()

canvas()

if bet == race():
    print('You won congrats')
else:
    print('You lose')

screen.exitonclick()
