import turtle as t
from random import random
class Box:
    def __init__(self, n):
        self.n = n
        if random() > 0.5:
            self.color = 'red'
        else:
            self.color = 'yellow'

    def draw_square(self, a):
        t.penup()
        t.setpos(100,100)
        t.write(self.n)
        t.pendown()
        t.done()


#===========================
boxes = []
for i in range(0,36):
    boxes.append(Box(i+1))

for i in range(0,36):
    print(boxes[i].n, boxes[i].color)

boxes[25].draw_square(10)



