from turtle import Screen, Turtle
import time
import random
from Controls import Paddle
from Ball import ball
from Score import Score
screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))
score_board = Score()
ball1 = ball()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w") 
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    ball1.move()
    screen.update()
    if ball1.ycor() > 280 or ball1.ycor() < -275:
        ball1.bounce()  
    if ball1.distance(r_paddle) < 50 and ball1.xcor() > 320 or ball1.distance(l_paddle) < 50 and ball1.xcor() < -320:
        ball1.collision()
    if ball1.xcor() > 380 or ball1.xcor() < -380:
        if ball1.xcor()>380:
            score_board.l_score+=1
            score_board.update_score()
            ball1.goto(0,0)
            ball1.collision()
        if ball1.xcor()< -380:
            score_board.r_score+=1
            score_board.update_score()
            ball1.goto(0,0)
            ball1.collision()
        
screen.exitonclick()
