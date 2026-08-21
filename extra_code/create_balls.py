import random as ran

def create_balls(canvas, root):
    ball1type = ran.choice(['default', 'big', 'fast'])
    ball2type = ran.choice(['default', 'big', 'fast'])



    if ball1type == 'default':
        temp_dx = ran.uniform(0.1, 10.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='gray25'),
            'txt': canvas.create_text(30, 30, text="1", fill="gray90"),
            'hp': 100,
            'damage': 10,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'default'
        }
    elif ball1type == 'big':
        temp_dx = ran.uniform(0.1, 5.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 100, 100, fill='gray25'),
            'txt': canvas.create_text(40, 40, text="1", fill="gray90"),
            'hp': 150,
            'damage': 5,
            'dx': temp_dx,
            'dy': 5 - temp_dx,
            'type': 'big'
        }
    elif ball1type == 'fast':
        temp_dx = ran.uniform(0.1, 25.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='gray25'),
            'txt': canvas.create_text(40, 40, text="1", fill="gray90"),
            'hp': 75,
            'damage': 12,
            'dx': temp_dx,
            'dy': 25 - temp_dx,
            'type': 'fast'
        }



    if ball2type == 'default':
        temp_dx = ran.uniform(0.1, 10.0)
        ball2 = {
            'shape': canvas.create_oval(850, 550, 890, 590, fill='gray25'),
            'txt': canvas.create_text(870, 570, text="2", fill="gray90"),
            'hp': 100,
            'damage': 10,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'default'
        }
    elif ball2type == 'big':
        temp_dx = ran.uniform(0.1, 5.0)
        ball2 = {
            'shape': canvas.create_oval(800, 500, 890, 590, fill='gray25'),
            'txt': canvas.create_text(40, 40, text="2", fill="gray90"),
            'hp': 150,
            'damage': 5,
            'dx': temp_dx,
            'dy': 5 - temp_dx,
            'type': 'big'
        }
    elif ball2type == 'fast':
        temp_dx = ran.uniform(0.1, 25.0)
        ball2 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='gray25'),
            'txt': canvas.create_text(40, 40, text="2", fill="gray90"),
            'hp': 75,
            'damage': 12,
            'dx': temp_dx,
            'dy': 25 - temp_dx,
            'type': 'fast'
        }
    
    return ball1, ball2
