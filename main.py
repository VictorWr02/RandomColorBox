import turtle as t
from random import random


class Box:
    def __init__(self, n):
        self.n = n
        if random() > 0.5:
            self.color = 'red'
        else:
            self.color = 'yellow'

    def draw_square(self, x0=300, y0=300, a=50, r=4):
        cat = self.n // r
        rest = self.n % r
        x = 0
        y = 0
        if rest == 0:
            x = x0 + (r-1) * a
            y = y0 - (cat-1) * a
        else:
            x = x0 + (rest - 1) * a
            y = y0 - cat * a

        t.penup()
        t.setpos(x, y)  # Setează poziția inițială
        t.pendown()
        t.color(self.color)
        t.begin_fill()  # Începe umplerea pătratului cu culoare



        for _ in range(4):  # Desenează un pătrat
            t.forward(a)  # Desenează o latură de lungime `a`
            t.right(90)  # Întoarce la dreapta 90 de grade

        t.end_fill()  # Termină umplerea pătratului cu culoare
        t.color("black")
        t.write(self.n)


# ===========================

# def draw_grid(boxes, a):
#     cols = 6  # Numărul de coloane în grid
#     rows = 6  # Numărul de rânduri în grid
#     spacing = 10  # Spațiere între pătrate
#
#     start_x = -150  # Poziția de start pe axa X
#     start_y = 150   # Poziția de start pe axa Y

# for i in range(rows):
#     for j in range(cols):
#         index = i * cols + j
#         x = start_x + j * (a + spacing)
#         y = start_y - i * (a + spacing)
#         boxes[index].draw_square(x, y, a)

# Configurarea turtle
t.speed(0)  # Setează viteza maximă de desenare

# Configurarea listei de pătrate
boxes = []
for i in range(36):
    boxes.append(Box(i + 1))

for i in range(36):
    print(boxes[i].n, boxes[i].color)

for i in range(16):
    boxes[i].draw_square()

# # Desenează grid-ul de pătrate
# draw_grid(boxes, 30)  # Dimensiunea fiecărui pătrat este 30

t.done()  # Termină desenul
