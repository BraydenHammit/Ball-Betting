def frame(canvas=None, root=None, ball1=None, ball2=None, winner=None):
    canvas.move(ball1['shape'], ball1['dx'], ball1['dy'])
    canvas.move(ball2['shape'], ball2['dx'], ball2['dy'])
    pos1 = canvas.coords(ball1['shape'])
    pos2 = canvas.coords(ball2['shape'])

    if pos1[2] >= canvas.winfo_width() or pos1[0] <= 0:
        ball1['dx'] = -ball1['dx']
    if pos1[3] >= canvas.winfo_height() or pos1[1] <= 0:
        ball1['dy'] = -ball1['dy']

    if pos2[2] >= canvas.winfo_width() or pos2[0] <= 0:
        ball2['dx'] = -ball2['dx']
    if pos2[3] >= canvas.winfo_height() or pos2[1] <= 0:
        ball2['dy'] = -ball2['dy']


    ball1coords = canvas.coords(ball1['shape'])
    ball2coords = canvas.coords(ball2['shape'])
    if (ball1coords[2] >= ball2coords[0] and ball1coords[0] <= ball2coords[2] and ball1coords[3] >= ball2coords[1] and ball1coords[1] <= ball2coords[3]):
        ball1['hp'] -= ball2['damage']
        ball2['hp'] -= ball1['damage']

        ball1['dx'] = -ball1['dx']
        ball1['dy'] = -ball1['dy']
        ball2['dx'] = -ball2['dx']
        ball2['dy'] = -ball2['dy']


    cx1 = (ball1coords[0] + ball1coords[2]) / 2
    cy1 = (ball1coords[1] + ball1coords[3]) / 2
    canvas.move(ball1['txt'],cx1,cy1)
    canvas.tag_raise(ball1['txt'])
    cx2 = (ball2coords[0] + ball2coords[2]) / 2
    cy2 = (ball2coords[1] + ball2coords[3]) / 2
    canvas.move(ball2['txt'],cx2,cy2)
    




    if ball1['hp'] <= 0:
        winner = "ball2"
    elif ball2['hp'] <= 0:
        winner = "ball1"
    else:
        root.after(16, lambda: frame(canvas=canvas, root=root, ball1=ball1, ball2=ball2, winner=winner))