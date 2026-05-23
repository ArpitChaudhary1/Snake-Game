
from turtle import Turtle

import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_wid=0.5 , stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.goto(x=random.randint(-250,250),y=random.randint(-250,200))
        self.change_pos()


    def change_pos(self):

        self.goto(x=random.randint(-250, 250), y=random.randint(-250, 200))
