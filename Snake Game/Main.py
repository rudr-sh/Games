from turtle import Screen, Turtle
import time
from Snake import Snake
from food import Food
import random
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("snake Game")
screen.tracer(0)
screen.listen()
snake=Snake()
food = Food()
game_is_on = True
score_board=Turtle()
score=0
while game_is_on:
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.update()
    time.sleep(0.1)
    snake.move()
    score_board.color("white")
    score_board.hideturtle()
    score_board.clear()
    score_board.penup()
    score_board.goto(-280,260)
    score_board.write(f"Score: {score}",False,align="left",font=("Arial",24,"normal"))
    if snake.segments[0].distance(food) < 20:
        food.goto(random.randint(-280,280),random.randint(-280,280))   
        score+=1
        snake.extend_snake()
    if snake.segments[0].xcor() > 298 or snake.segments[0].xcor() < -298 or snake.segments[0].ycor() > 298 or snake.segments[0].ycor() < -298:
        game_is_on = False
        score_board.goto(0,0)
        score_board.write("Game Over",False,align="center",font=("Arial",24,"normal"))
    if snake.collision():
        game_is_on = False
        score_board.goto(0,0)
        score_board.write("Game Over",False,align="center",font=("Arial",24,"normal"))
screen.exitonclick()
