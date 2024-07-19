from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_cor = 10
        self.y_cor = 10
        self.ball_speed = 0.1
    def move(self):
        x = self.xcor() + self.x_cor
        y = self.ycor() + self.y_cor
        self.goto(x, y)

    def directions_y(self):
        self.y_cor *= -1
    def directions_x(self):
        self.x_cor *= -1
    def restart(self):
        self.ball_speed = 0.1
        self.goto(0,0)
        self.x_cor *=-1
    def speed_of_ball(self):
        self.ball_speed *= 0.9
