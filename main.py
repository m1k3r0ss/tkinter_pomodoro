from tkinter import *
import math
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
VIOLET = "#9e83db"
GREEN = "#B5C18E"
YELLOW = "#FFFF00"
FONT_NAME = "Spumoni"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
checkmark = "✓"
reps = 0
timer = None
alert = "tonari_no_totoro.mp3"
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    app_label.config(text="Timer", fg=YELLOW)
    check.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global timer
    reps +=1
    work_seconds = int(WORK_MIN * 60)
    short_break_secs = int(SHORT_BREAK_MIN * 60)
    long_break_secs = int(LONG_BREAK_MIN * 60)
    if reps % 2 == 0 and reps != 8 and reps != 0:
        app_label.config(text= "Break", fg=PINK)
        count_down(short_break_secs)
    elif reps % 2!= 0:
        app_label.config(text="Work", fg=VIOLET)
        count_down(work_seconds)
    elif reps == 8:
        app_label.config(text="Break", fg=PINK)
        count_down(long_break_secs)
    if reps > 8:
        window.after_cancel(timer)
        app_label.config(text="Pomodoro Complete!")
        os.system("afplay " + alert)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    minutes = math.floor(count/60)
    seconds = count%60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count>0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += checkmark
        check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=40, pady=20,bg= GREEN,)



app_label = Label(text="Timer", fg=YELLOW, bg=GREEN, font=("Spumoni", 35, "bold"))
app_label.grid(column=1, row=0)

canvas = Canvas(width=300, height= 320, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="Catbus.png")
canvas.create_image(142,160, image=tomato_img)
timer_text = canvas.create_text(142,230, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1,row=1)


start_btn = Button(text="Start", highlightthickness=0, bd=0 ,bg=GREEN, padx=0, pady=0, command=start_timer)
start_btn.grid(column=0,row=2)

reset_btn = Button(text="Reset", highlightthickness=0, bd=0, bg=GREEN, padx=0, pady=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

check = Label(bg=GREEN, fg=YELLOW, font=("Spumoni", 25, "bold"))
check.grid(column=1,row=3)

window.mainloop()