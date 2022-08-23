from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

# Window setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=80, bg=YELLOW)


# Canvas setup
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Timer heading
timer_text = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "normal"))
timer_text.grid(column=1, row=0)


# Start button
def start():
    pass


button = Button(text="Start", command=start, bg=YELLOW, highlightbackground=YELLOW)
button.grid(column=0, row=2)


# Reset button
def reset():
    pass


button = Button(text="Reset", command=reset, bg=YELLOW, highlightbackground=YELLOW)
button.grid(column=2, row=2)


# Counter
timer_text = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 28, "normal"))
timer_text.grid(column=1, row=3)

window.mainloop()
