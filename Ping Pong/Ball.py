from turtle import Turtle
from Controls import *
class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.x_move = 15
        self.y_move = 15
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    
    def bounce(self):
        self.y_move *= -1
    def collision(self):
        self.x_move *= -1