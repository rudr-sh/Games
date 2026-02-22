from turtle import Turtle
import random
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("Red")
        self.penup()
        self.shapesize(stretch_len=0.75,stretch_wid=0.75)
        self.speed("fastest")
        self.goto(random.randint(-280,280),random.randint(-280,280))
        