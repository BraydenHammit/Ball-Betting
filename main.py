import tkinter as tk
import random as ran
from extra_code.frames import frame

root = tk.Tk()
root.title("Physics Test")
root.state('zoomed')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

def start():
    global ball1, ball1DX, ball1DY
    start_button.pack_forget()
    title.pack_forget()
    canvas.grid(row=0, column=0, sticky="nsew")

    ball1 = canvas.create_oval(10, 10, 50, 50, fill='gray25')
    ball1DX = ran.uniform(0.1, 10.0)
    ball1DY = 10 - ball1DX
    frame(ball1DX=ball1DX, ball1DY=ball1DY, canvas=canvas, root=root, ball1=ball1)

canvas = tk.Canvas(root, width=100, height=100)
start_button = tk.Button(root, text="Start", command=lambda: start())
title = tk.Label(root, text="Physics Test")
title.pack(pady=10)
start_button.pack(pady=20)

root.mainloop()