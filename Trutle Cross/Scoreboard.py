from turtle import Turtle 

class score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-200,250)
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}",align="center", font=("Arial",24,"normal"))
    def end(self):
        self.setposition(0,0)
        self.write(f"GAME OVER",align="center",font=("Arial",24,"normal"))