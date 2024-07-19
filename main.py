from turtle import Screen
from slider import Slider
import time
from ball import Ball
from score import Score
screen = Screen()
screen.setup(800,600)
screen.title("Ping Pong")
screen.bgcolor("black")
screen.tracer(0)
is_on = True
screen.listen()

slider1 = Slider((350,0))
slider2 = Slider((-350,0))
ball = Ball()
score = Score()

screen.update()
screen.onkeypress(slider2.up,"w")
screen.onkeypress(slider2.down,"s")
screen.onkeypress(slider1.up,"Up")
screen.onkeypress(slider1.down,"Down")


while is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.directions_y()
    if ball.distance(slider1) < 50 and ball.xcor() > 330:
        score.scored_by_right()
        ball.directions_x()
        ball.speed_of_ball()
    if ball.distance(slider2) < 50 and ball.xcor() < -330:
        score.scored_by_left()
        ball.directions_x()
        ball.speed_of_ball()
    if ball.xcor() > 380:
        score.scored_by_left()
        time.sleep(0.3)
        ball.restart()
    if ball.xcor() < -380:
        score.scored_by_right()
        time.sleep(0.3)
        ball.restart()

screen.exitonclick()

