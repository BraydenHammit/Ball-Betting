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
bet = [None,None] #. [Ball#,$$$] 

def start_bet():
    global ball2, ball1, textbox1, textbox2, textboxM, textboxW
    start_button.pack_forget()
    title.pack_forget()
    try:
        textboxW.destroy()
    except: None
    ball1, ball2 = create_balls(canvas, root)
    textbox1 = tk.Label(text=f'Ball 1 will be: {ball1['type'].title()}', fg='red')
    textbox2 = tk.Label(text=f'Ball 2 will be: {ball2['type'].title()}', fg='blue')
    textboxM = tk.Label(text=f'You have: ${money}\n\nWhat would you like to bet?')
    textboxW = tk.Label(text='Who would you like to bet on?')
    textbox1.pack(pady = 5)
    textbox2.pack(pady = 5)
    textboxM.pack(pady = 5)
    betting_enter.pack(pady = 15)
    textboxW.pack(pady = 10)
    betting_ok1.pack(pady = 5)
    betting_ok2.pack(pady = 5)

    root.update_idletasks()

def check_for_winner():
    global winner, bet, money
    prevmoney = money
    won = True
    if winner == 'ball1':
        if bet[0] == 'ball1':
            money += bet[1]
        else:
            money -= bet[1]
    elif winner == 'ball2':
        if bet[0] == 'ball2':
            money += bet[1]
        else:
            money -= bet[1]
    else:
        root.after(100,check_for_winner)
        won = False

    if won:
        textboxW = tk.Label(text=f'{winner[0].title()+winner[1]+winner[2]+winner[3],winner[4]} won.\nYou made {prevmoney-money}, and are now at ${money}.')
        start_button.configure(text='Ok')
        textboxW.pack(pady = 10)
        start_button.pack(pady = 5)
     

def start(betNONGLOBAL):
    global money, bet
    try:
        if (int(betting_enter.get()) >= 0) and (int(betting_enter.get()) <= money):
                bet = betNONGLOBAL
                textbox1.destroy()
                textbox2.destroy()
                textboxM.destroy()
                textboxW.destroy()
                betting_enter.pack_forget()
                betting_ok1.pack_forget()
                betting_ok2.pack_forget()
                canvas.pack(expand=True, fill='none')
                
                frame(canvas=canvas, root=root, ball1=ball1, ball2=ball2, winner=winner)
    except: None

    root.after(100,check_for_winner)



canvas = tk.Canvas(root, width=900, height=600, bg="gray50", highlightbackground="gray10",)
start_button = tk.Button(root, text="Start", command=lambda: start_bet())
title = tk.Label(root, text="Physics Test")
betting_enter = tk.Entry(root, width=30)
betting_ok1 = tk.Button(root, text='Ball 1', command = lambda: start('ball1'))
betting_ok2 = tk.Button(root, text='Ball 2', command = lambda: start('ball2'))
title.pack(pady=10)
start_button.pack(pady=20)

root.mainloop()