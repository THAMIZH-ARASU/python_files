import turtle
import time
import random

print("This program draws shapes based on the number you entered in uniform pattern")
n=input("Enter the number of sides:")
if(n.isdigit()):
    sq=int(n)
angle=180-180*(sq-2)/sq
turtle.up()

x=0
y=0
turtle.setpos(x,y)
nshape=8

for x in range(nshape):
    turtle.color(random.random(),random.random(),random.random())
    x+=5
    y+=5
    turtle.forward(x)
    turtle.forward(y)

    for i in range(sq):
        turtle.begin_fill()
        turtle.down()
        turtle.forward(40)
        print(turtle.pos())
        turtle.up()
        turtle.end_fill()
time.sleep(11)
turtle.bye()
