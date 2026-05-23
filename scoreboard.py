from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,250)
        self.point = 0
        self.color("White")
        self.write(f"Score : {self.point}" , move=False , align="center" , font=("Arial" , 20 , "normal"))
        self.hideturtle()

    def increase(self):
        self.point += 1
        self.clear()
        self.write(f"Score : {self.point}", move=False, align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER" ,move= False , align="center", font=("Arial", 20, "normal") )