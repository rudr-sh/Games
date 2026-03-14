from turtle import Turtle
import random
color = ["black","blue","orange","red","pink","green","brown",]
class gaadi(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(color))
        self.shapesize(0.85,2)
        self.penup()
        self.setheading(180)
        self.goto(280,random.randrange(-250,250,20))
    def move(self,fast):
        self.forward(fast)
    