from turtle import Turtle
dist = 20
UP = 90
DOWN = 270
class Slider(Turtle):
    def __init__(self,coordinate):
        super().__init__()
        self.shape("square")
        self.shapesize(5,1)
        self.color("white")
        self.penup()
        self.goto(coordinate)
    def up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(),y)
    def down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(),y)