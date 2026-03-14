from turtle import Screen,Turtle
import time
from Traffic import gaadi
from Scoreboard import score_board
screen = Screen()
screen.setup(600,600)
screen.tracer(0)
screen.listen()        
Score=score_board()
#Declaring Turtle
obj = Turtle()
obj.shape("turtle")
obj.setheading(90)
obj.penup()
obj.goto(0,-280)
#Controls
def forward():
        obj.forward(10)
screen.onkey(forward,"Up")
speed = 5
#DeclaringTraffic
traffic = []
level_change=1
game_is_on = True
def create_car():
        cars = gaadi()
        traffic.append(cars)
frame_count = 0
cars_spawn_interval=7
while game_is_on:
        for vehical in traffic:
                vehical.move(speed)
                if vehical.distance(obj) < 28:
                        game_is_on = False
                        Score.end()
        if obj.ycor()>280:
                        Score.level+=1
                        Score.update_score()
                        obj.setposition(0,-280)
                        speed+=5
                        
        if frame_count % cars_spawn_interval == 0:
                create_car()
        time.sleep(0.1)
        frame_count+=1
        screen.update()
screen.exitonclick()
