from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score1 = 0
        self.score2 = 0
        self.goto(-100, 200)
        self.write(self.score1,align="center",font=("Arial",80,"bold"))
        self.goto(100,200)
        self.write(self.score2, align="center", font=("Arial", 80, "bold"))
    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score1, align="center", font=("Arial", 80, "bold"))
        self.goto(100, 200)
        self.write(self.score2, align="center", font=("Arial", 80, "bold"))
    def scored_by_right(self):
        self.score2+=1
        self.update()
    def scored_by_left(self):
        self.score1+=1
        self.update()