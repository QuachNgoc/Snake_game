import turtle
from turtle import Turtle
from random import randint

turtle.colormode(255)


def random_color():
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    return r, g, b


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color(random_color())
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = randint(-260, 260)
        random_y = randint(-260, 260)
        self.goto(random_x, random_y)
        self.color(random_color())
