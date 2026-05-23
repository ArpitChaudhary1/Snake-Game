from turtle import Turtle


MOVE_DISTANCE = 20
STARTING_POS = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for positions in STARTING_POS:
            self.add_segment(positions)

    def add_segment(self,positions):
        tur = Turtle(shape="square")
        tur.color("white")
        tur.pu()
        tur.goto(positions)
        self.segments.append(tur)


    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):

        head = self.head.heading()
        if head == 0:
            self.head.setheading(90)
        elif head == 180:
            self.head.setheading(90)


    def down(self):

        head = self.head.heading()
        if head == 0:
            self.head.setheading(270)
        elif head == 180:
            self.head.setheading(270)


    def left(self):

        head = self.head.heading()
        if head == 90:
            self.head.setheading(180)
        elif head == 270:
            self.head.setheading(180)

    def right(self):

        head = self.head.heading()
        if head == 90:
            self.head.setheading(0)
        elif head == 270:
            self.head.setheading(0)
