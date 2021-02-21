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
reps = 8
ticks = 0
timer = NONE

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global timer
    window.after_cancel(timer)
    check_label.config(text="")
    name_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(count_text, text="00:00")
    global reps
    global ticks
    reps = 8
    ticks = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global ticks

    if reps % 2 == 1 and reps != 1:
        window.lift()
        window.attributes("-topmost", True)
        window.attributes("-topmost", False)
        ticks += 1
        name_label.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
        check_label.config(text=ticks * "✔")
    elif reps % 2 == 0:
        name_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
    elif reps == 1:
        window.lift()
        window.attributes("-topmost", True)
        window.attributes("-topmost", False)
        ticks += 1
        check_label.config(text=ticks * "✔")
        name_label.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    if reps == 0:
        reset()
    reps -= 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    minutes = math.floor(count / 60)
    seconds = count % 60
    if len(str(seconds)) < 2:
        seconds = f"0{seconds}"

    if len(str(minutes)) < 2:
        minutes = f"0{minutes}"

    canvas.itemconfig(count_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        minutes = count / 60

    if count == 0:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Clock")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
count_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

name_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30), bg=YELLOW)
name_label.grid(column=1, row=0)

check_label = Label(text="", fg=GREEN, font=(FONT_NAME, 30), bg=YELLOW)
check_label.grid(column=1, row=3)


start_button = Button(text="Start", command=start_timer, highlightbackground=YELLOW)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset, highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)

window.mainloop()