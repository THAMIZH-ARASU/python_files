import turtle
colors=['red','purple','blue','green','orange','yellow']
t=turtle.Pen()
turtle.bgcolor("black")
for i in range(300):
    t.pencolor(colors[i%6])
    t.width(i//100+1)
    t.fd(i)
    t.left(59)
