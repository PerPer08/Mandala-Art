#Jasper Nillos BSCS 1B
#Mandala Art - cyber aurora

import turtle

squirtle = turtle
squirtle.colormode(255)
squirtle.speed(0)

squirtle.bgcolor("black")
squirtle.title("Cyber Aurora - Nillos")

colors = [[2, 83, 133],[3, 130, 152],[14, 243, 197],[4, 226, 183]]
petal_leaf = 150
petal_stem = 50
petal_span = 90
petal_angle1 = 90
petal_angle2 = 135
size_pen = 1

trunk = 70
branch = 19
circle_size = 50

def petal():
    for i in range(8):
        squirtle.right(45)
        squirtle.pensize(size_pen / 2)
        squirtle.right(135)
        squirtle.penup()
        squirtle.forward(petal_stem)
        squirtle.pendown()
        squirtle.right(45)
        squirtle.pencolor(colors[ s % 4])
        squirtle.circle(petal_leaf,petal_span)
        squirtle.left(petal_angle1)   
        squirtle.circle(petal_leaf,petal_span)
        squirtle.left(petal_angle2)
        squirtle.right(180)
        squirtle.penup()
        squirtle.forward(petal_stem)
        squirtle.right(45)
        squirtle.pendown()


def octa():
    
    squirtle.penup()
    squirtle.right(135)
    squirtle.forward(trunk)
    squirtle.pendown()
    for i in range(8):
        squirtle.left(45)
        for i in range(8):
            squirtle.pensize(0)
            squirtle.pencolor(2, 83, 133)
            squirtle.forward(branch)
            squirtle.right(45)        
    squirtle.right(180)
    squirtle.penup()
    squirtle.forward(trunk)
    squirtle.right(45)
    squirtle.pendown()



squirtle.pensize(5)
for s in range(4):
    for j in range(3):
        petal()
        petal_leaf -= 13
        petal_stem += 13
        petal_span += .5
        petal_angle1 -= .5
        petal_angle2 -= .5

squirtle.pencolor("blue")
squirtle.pensize(2)

for i in range(8):
    squirtle.right(45)
    octa()
branch *= .5
trunk *= 2 

for k in range(12):
    colors = [[2, 83, 133],[4, 226, 183],[3, 130, 152],[14, 243, 197]]
    if k < 4:
        squirtle.pencolor(colors[ k %4])
    else:
        if k < 7:
            squirtle.pencolor(3, 130, 152)
        elif k < 10:
            squirtle.pencolor(3, 130, 152)
        else:
            squirtle.pencolor(4, 226, 183)
    for i in range(8):
        squirtle.right(45)
        if k < 2:
            squirtle.fillcolor(colors[i % 4])
            squirtle.begin_fill()
        if k == 2:
            squirtle.fillcolor(2, 83, 133)
            squirtle.begin_fill()
        squirtle.circle(circle_size)
        
        squirtle.end_fill()
    if k < 3:
        circle_size -= 7
    else:
        squirtle.pensize(0)
        circle_size -= k/2
       

squirtle.exitonclick()


    