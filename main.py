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

reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If 1st/3rd/5th/7th
    count_down(work_sec)

    # If 2nd/4th/6th
    count_down(short_break_sec)

    # If 8th
    count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

# Window setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=80, bg=YELLOW)

# Canvas setup
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Timer heading
timer_heading = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "normal"))
timer_heading.grid(column=1, row=0)

# Start button
button_start = Button(text="Start", command=start_timer, bg=YELLOW, highlightbackground=YELLOW)
button_start.grid(column=0, row=2)

# Reset button
button_reset = Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW)
button_reset.grid(column=2, row=2)

# Counter
tick = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 28, "normal"))
tick.grid(column=1, row=3)

window.mainloop()
