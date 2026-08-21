import random as ran

def frame(canvas, root, ball1, ball2, healthbar1, healthbar2, winner, checkforwinner):
    canvas.move(ball1['shape'], ball1['dx'], ball1['dy'])
    canvas.move(ball2['shape'], ball2['dx'], ball2['dy'])
    pos1 = canvas.coords(ball1['shape'])
    pos2 = canvas.coords(ball2['shape'])

    ball1Mult = ran.uniform(-0.5,0.5)
    ball2Mult = ran.uniform(-0.5,0.5)
    if pos1[2] >= canvas.winfo_width() or pos1[0] <= 0:
        ball1['dx'] = -ball1['dx'] + ball1Mult
        ball1['dy'] -= ball1Mult
    if pos1[3] >= canvas.winfo_height() or pos1[1] <= 0:
        ball1['dy'] = -ball1['dy'] + ball1Mult
        ball1['dx'] -= ball1Mult
    if pos2[2] >= canvas.winfo_width() or pos2[0] <= 0:
        ball2['dx'] = -ball2['dx'] + ball2Mult
        ball2['dy'] -= ball2Mult
    if pos2[3] >= canvas.winfo_height() or pos2[1] <= 0:
        ball2['dy'] = -ball2['dy'] + ball2Mult
        ball2['dx'] -= ball2Mult


    ball1coords = canvas.coords(ball1['shape'])
    ball2coords = canvas.coords(ball2['shape'])
    if (ball1coords[2] >= ball2coords[0] and ball1coords[0] <= ball2coords[2] and ball1coords[3] >= ball2coords[1] and ball1coords[1] <= ball2coords[3]):
        ball2depletion = ball1['damage']*(ran.uniform(0.05,2.5))
        ball1depletion = ball2['damage']*(ran.uniform(0.05,2.5))
        ball1['hp'] -= ball1depletion
        ball2['hp'] -= ball2depletion

        if ball1['type'] == 'vampire':
            ball1['hp'] += (0.25*ball2depletion)
            if ball1['hp'] > ball1['max hp']:
                ball1['hp'] = ball1['max hp']
        if ball2['type'] == 'vampire':
                    ball2['hp'] += (0.25*ball1depletion)
                    if ball2['hp'] > ball2['max hp']:
                        ball2['hp'] = ball2['max hp']

        ball1['dx'] = -ball1['dx']
        ball1['dy'] = -ball1['dy']
        ball2['dx'] = -ball2['dx']
        ball2['dy'] = -ball2['dy']


    healthbar1.configure(text=f'{round(ball1['hp'],1)}/{ball1['max hp']}')
    healthbar2.configure(text=f'{round(ball2['hp'],1)}/{ball2['max hp']}')


    if ball1['hp'] <= 0:
        winner = "ball2"
        healthbar1.configure(text=f'0/{ball1['max hp']}')
        canvas.delete(ball1['shape'])
        canvas.delete(ball2['shape'])
        checkforwinner(winner)
    elif ball2['hp'] <= 0:
        winner = "ball1"
        healthbar2.configure(text=f'0/{ball2['max hp']}')
        canvas.delete(ball1['shape'])
        canvas.delete(ball2['shape'])
        checkforwinner(winner)
    else:
        root.after(16, lambda: frame(canvas, root, ball1, ball2, healthbar1, healthbar2, winner, checkforwinner))