from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    canvas.itemconfig(heading,text="Timer",fill=GREEN)
    canvas.itemconfig(check,text="")
    global reps
    reps =0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec= LONG_BREAK_MIN *60
    
   
    if reps % 8 == 0:
        canvas.itemconfig(heading,text="Break",fill="Pink")
        count_down(long_break_sec)
    elif reps % 2 == 0 :
        canvas.itemconfig(heading,text="Break", fill="Green")
        count_down(short_break_sec)
    else:
        canvas.itemconfig(heading,text="Work",fill="Red")
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minute = math.floor(count/60)
    count_sec=count%60
    if count_sec < 10:
        count_sec= f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_minute}:{count_sec}")
    if count>0:
        global timer
        timer =window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark+="✓"
        canvas.itemconfig(check,text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro Timer")
window.config(padx=100,pady=50,bg=YELLOW)
window.minsize(500,600) 
canvas=Canvas(width=500,height=500,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="C:/Users/Rudraksh Sharma/Documents/100-days/Day 28/tomato.png")
canvas.create_image(250,200,image=tomato_img)
canvas.image = tomato_img
timer_text=canvas.create_text(250,210,text="00:00",font=("Courier",35,"bold"))
heading=canvas.create_text(250,60,text="Timer",font=("Courier",35,"bold"),fill=GREEN)
check = canvas.create_text(245,350,font=("Courier",25,"bold"),fill=GREEN)
canvas.pack() 
start=Button(text="Start",command=start_timer)  
start.config(height=1,width=5)
start.place(x=90,y=350)
reset=Button(text="Reset",command=reset)
reset.config(height=1,width=5)
reset.place(x=350,y=350)
window.mainloop()
