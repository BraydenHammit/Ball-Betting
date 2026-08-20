def frame(ball1DX=None, ball1DY=None, canvas=None, root=None, ball1=None):
    canvas.move(ball1, ball1DX, ball1DY)
    pos = canvas.coords(ball1)
    if pos[2] >= canvas.winfo_width() or pos[0] <= 0:
        ball1DX = -ball1DX
    if pos[3] >= canvas.winfo_height() or pos[1] <= 0:
        ball1DY = -ball1DY
    root.after(16, lambda: frame(ball1DX=ball1DX, ball1DY=ball1DY, canvas=canvas, root=root, ball1=ball1))