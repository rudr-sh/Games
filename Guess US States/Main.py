from turtle import *
import pandas
#Basic Setup
screen=Screen()
screen.setup(725,491)
screen.title("US STATES GAME")
screen.bgpic("C:/Users/Rudraksh Sharma/Documents/100-days/Day 25/blank_states_img.gif")
turtle=Turtle()
turtle.hideturtle()
data=pandas.read_csv("C:/Users/Rudraksh Sharma/Documents/100-days/Day 25/50_states.csv")
#Taking User input & checking answer
score=0

while score<50:
    ans=(screen.textinput(f"{score}/50","Enter name of state: "))
    if ans is None:
        break
    ans= ans.lower().strip()
    for i in data["state"]:
        if ans == (i.lower()).strip():
            name_state=data[data.state==i]
            turtle.penup()
            turtle.goto(x=int(name_state["x"]),y=int(name_state["y"]))
            turtle.pencolor("black")
            turtle.pendown()
            turtle.write(f"{i}",align="center",font=("Arial",10,"bold"))
            score+=1
            data = data.drop(name_state.index)
            break
screen.exitonclick()
