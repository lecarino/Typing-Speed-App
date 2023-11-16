import time
from tkinter import *

class Timer():
    def __init__(self):
        self.timer_id = None
        self.start_time = None
        self.word_count = 0
        self.count = None

    def count_down(self, canvas, timer_txt, wpm_txt, window, word_entry):
        count_min = self.count//60
        count_sec = self.count % 60

        if count_sec < 10:
            count_sec = f"0{count_sec}"

        canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")

        if self.count > 0:
            self.count-=1
            self.timer_id = window.after(1000, self.count_down, canvas, timer_txt, wpm_txt, window, word_entry)
        else:
            word_entry.config(state='disabled')
            self.calc_wpm(canvas, wpm_txt)
    
    def start_test(self, canvas, timer_txt, wpm_txt, window, word_entry):
        self.start_time = time.time()
        self.word_count = 0
        self.count_down(canvas=canvas, timer_txt=timer_txt, wpm_txt=wpm_txt, window=window, word_entry=word_entry)
        
    def calc_wpm(self, canvas, wpm_txt):
        elapsed_time = time.time() - self.start_time
        minutes = elapsed_time / 60
        wpm = self.word_count / minutes
        canvas.itemconfig(wpm_txt, text=f"Words Per Min: {wpm:.2f}", font=('Arial', 18))
   
    def reset_timer(self, canvas, timer_txt, window):
        window.after_cancel(self.timer_id)
        canvas.itemconfig(timer_txt, text="00:00")
        self.start_time = None
        self.word_count = 0
    
    def word_typed(self):
        self.word_count += 1


