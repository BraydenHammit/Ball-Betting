import tkinter as tk
import random as ran
from extra_code.create_balls import create_balls
from extra_code.frames import frame

root = tk.Tk()
root.title("Physics Test")
root.geometry("900x800")
root.minsize(900, 800)
root.state('zoomed')
money = 100
winner = None

def start_bet():
    global ball2, ball1, textbox
    start_button.pack_forget()
    title.pack_forget()
    ball1, ball2 = create_balls(canvas, root)
    textbox = tk.Label(text=f'Ball 1: {ball1['type'].title()}\nBall 2: {ball2['type'].title()}')
    textbox.pack(pady = 5)
    betting_enter.pack(pady = 15)
    betting_ok1.pack(pady = 5)
    betting_ok1.pack(pady = 5)



def start():
    try:
        if int(betting_enter.get()) >= 0:
                textbox.destroy()
                start_button.pack_forget()
                title.pack_forget()
                canvas.pack(expand=True, fill='none')
                
                frame(canvas=canvas, root=root, ball1=ball1, ball2=ball2, winner=winner)
    except: None

#    while winner is None:
#        None

canvas = tk.Canvas(root, width=900, height=600, bg="gray50", highlightbackground="gray10",)
start_button = tk.Button(root, text="Start", command=lambda: start_bet())
title = tk.Label(root, text="Physics Test")
betting_enter = tk.Entry()
betting_ok1 = tk.Button(root, text='Ball 1', command = lambda: start('ball1'))
betting_ok2 = tk.Button(root, text='Ball 1', command = lambda: start('ball2'))
title.pack(pady=10)
start_button.pack(pady=20)

root.mainloop()