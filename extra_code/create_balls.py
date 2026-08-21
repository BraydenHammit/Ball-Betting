import random as ran

def create_balls(canvas, root):
    ball1type = ran.choice(['default', 'big', 'fast', 'hyperspeed', 'vampire'])
    ball2type = ran.choice(['default', 'big', 'fast', 'hyperspeed', 'vampire'])







    if ball1type == 'default':
        temp_dx = ran.uniform(0.1, 10.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='red'),
            'hp': 100,
            'max hp': 100,
            'damage': 10,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'default'
        }
    elif ball1type == 'big':
        temp_dx = ran.uniform(0.1, 5.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 100, 100, fill='red'),
            'hp': 150,
            'max hp': 150,
            'damage': 5,
            'dx': temp_dx,
            'dy': 5 - temp_dx,
            'type': 'big'
        }
    elif ball1type == 'fast':
        temp_dx = ran.uniform(0.1, 25.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='red'),
            'hp': 75,
            'max hp': 75,
            'damage': 12,
            'dx': temp_dx,
            'dy': 25 - temp_dx,
            'type': 'fast'
        }
    elif ball1type == 'hyperspeed':
        temp_dx = ran.uniform(0.1, 100.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='red'),
            'hp': 25,
            'max hp': 25,
            'damage': 20,
            'dx': temp_dx,
            'dy': 100 - temp_dx,
            'type': 'hyperspeed'
        }
    elif ball1type == 'vampire':
        temp_dx = ran.uniform(0.1, 10.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='red'),
            'hp': 75,
            'max hp': 100,
            'damage': 10,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'vampire'
        }







    if ball2type == 'default':
        temp_dx = ran.uniform(0.1, 10.0)
        ball2 = {
            'shape': canvas.create_oval(850, 550, 890, 590, fill='blue'),
            'hp': 100,
            'max hp': 100,
            'damage': 10,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'default'
        }
    elif ball2type == 'big':
        temp_dx = ran.uniform(0.1, 5.0)
        ball2 = {
            'shape': canvas.create_oval(800, 500, 890, 590, fill='blue'),
            'hp': 150,
            'max hp': 150,
            'damage': 5,
            'dx': temp_dx,
            'dy': 5 - temp_dx,
            'type': 'big'
        }
    elif ball2type == 'fast':
        temp_dx = ran.uniform(0.1, 25.0)
        ball2 = {
            'shape': canvas.create_oval(850, 550, 890, 590, fill='blue'),
            'hp': 75,
            'max hp': 75,
            'damage': 12,
            'dx': temp_dx,
            'dy': 25 - temp_dx,
            'type': 'fast'
        }
    elif ball2type == 'hyperspeed':
        temp_dx = ran.uniform(0.1, 100.0)
        ball2 = {
            'shape': canvas.create_oval(850, 550, 890, 590, fill='blue'),
            'hp': 25,
            'max hp': 25,
            'damage': 20,
            'dx': temp_dx,
            'dy': 100 - temp_dx,
            'type': 'hyperspeed'
        }
    elif ball2type == 'vampire':
        temp_dx = ran.uniform(0.1, 10.0)
        ball2 = {
            'shape': canvas.create_oval(850, 550, 890, 590, fill='blue'),
            'hp': 75,
            'max hp': 100,
            'damage': 10,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'vampire'
        }
    



    
    return ball1, ball2
