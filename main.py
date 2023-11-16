from tkinter import *
from timer_class import Timer
import random


timer = Timer()

def on_enter_pressed(event):
    text = word_entry.get()

    if text == word_bank_label.cget("text"):
        update_word_bank()
        timer.word_typed()  # Increment word count
        word_entry.delete(0, END)
        word_entry.focus()
    else:
        canvas.itemconfig(wpm_txt, text='Try Again')

def update_word_bank():
    with open('data/vocab.txt', 'r') as file:
        words = file.read().split()
        word = random.choice(words)
    word_bank_label.config(text=word)

def start_typing_test():
    word_entry.config(state="normal")
    word_entry.delete(0, END)
    word_entry.focus()
    start_button.config(state="disabled")
    timer.start_test(canvas= canvas, timer_txt=timer_txt, wpm_txt=wpm_txt, window=window, word_entry=word_entry)

def restart_typing_test():
    word_entry.config(state="normal")
    word_entry.delete(0, END)
    start_button.config(state="disabled")
    timer.reset_timer(canvas, timer_txt, window)
    canvas.itemconfig(wpm_txt, text='WPM')

def fifteen_sec_mode():
    timer.count= 15
    start_button.config(state='normal')
    canvas.itemconfig(timer_txt, text='00:15')

def thirty_sec_mode():
    timer.count= 30
    start_button.config(state='normal')
    canvas.itemconfig(timer_txt, text='00:30')

def min_mode():
    timer.count= 60
    start_button.config(state='normal')
    canvas.itemconfig(timer_txt, text='01:00')

window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50)

# TITLES
title_txt = Label(text='Typing Speed Test', font=('Futura', 24))
title_txt.grid(row=0, column=0, columnspan=3)

# Generate a box for words to type
word_entry = Entry(width=12, state="disabled")
word_entry.grid(row=2, column=1)

#Binding Entry key
word_entry.bind('<Return>', on_enter_pressed)

# Generate a timer_txt and wpm_txt thru canvas
canvas = Canvas(width=200, height=100, highlightthickness=0)
timer_txt = canvas.create_text(100, 50, text="00:00", fill='black', font=('Arial', 18, "bold"))
wpm_txt = canvas.create_text(100, 70, text="WPM", fill='black', font=('Arial', 18, "bold"))
canvas.grid(row=5, column=1)


# Generate buttons
start_button = Button(text="Start Test", command=start_typing_test, state='disabled')
start_button.grid(row=3, column=1)

restart_button = Button(text="Restart Test", command=restart_typing_test)
restart_button.grid(row=4, column=1)

fifteen_sec_button = Button(text='15 seconds', command = fifteen_sec_mode)
fifteen_sec_button.grid(row=7, column=0)

thirty_sec_button = Button(text='30 seconds', command = thirty_sec_mode)
thirty_sec_button.grid(row=7, column=1)

min_button = Button(text='60 seconds', command = min_mode)
min_button.grid(row=7, column=2)

# Generate a word bank label
word_bank_label = Label()
word_bank_label.grid(row=1, column=1)

# Call the update_word_bank function to initialize the display
update_word_bank()

window.mainloop()

