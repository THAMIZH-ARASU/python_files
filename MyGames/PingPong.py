# The Ping Pong Game

import turtle as t

Ascore=0
Bscore=0

#creating a window

win=t.Screen()
win.title("The Pong Game")
win.bgcolor("black")
win.setup(width=900,height=600)
win.tracer(0)

#creating right paddle

rpad=t.Turtle()
rpad.speed(0)
rpad.shape("square")
rpad.color("white")
rpad.shapesize(stretch_wid=5,stretch_len=1)
rpad.penup()
rpad.goto(350,0)

#creating left paddle

lpad=t.Turtle()
lpad.speed(0)
lpad.shape("square")
lpad.color("white")
lpad.shapesize(stretch_wid=5,stretch_len=1)
lpad.penup()
lpad.goto(-350,0)

#Creating the ball

ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdirection=0.2
ballydirection=0.2

#pen for Score Update

pen=t.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score",align="center",font=("Verdana",24,"normal"))

#Left paddle Moving

def lpadUp():
    y=lpad.ycor()
    y+=90
    lpad.sety(y)
    
def lpadDown():
    y=lpad.ycor()
    y-=90
    lpad.sety(y)

def rpadUp():
    y=rpad.ycor()
    y+=90
    rpad.sety(y)

def rpadDown():
    y=rpad.ycor()
    y-=90
    rpad.sety(y)

#Alotting Keys

win.listen()
win.onkeypress(lpadUp,'w')
win.onkeypress(lpadDown,'s')
win.onkeypress(rpadUp,"Up")
win.onkeypress(rpadDown,"Down")

while True:
    win.update()

    #moving ball
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)

    #border setup
    if lpad.ycor()>260:
        lpad.sety(260)
    if lpad.ycor()<-260:
        lpad.sety(-260)

    if rpad.ycor()>260:
        rpad.sety(260)
    if rpad.ycor()<-260:
        rpad.sety(-260)

    if ball.ycor()>290:
        ball.sety(290)
        ballydirection=ballydirection*-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection=ballydirection*-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ballxdirection=ballxdirection* -1
        Ascore+=1
        pen.clear()
        pen.write("Player A:{}                Player B:{}".format(Ascore,Bscore),align="center",font=("Verdana",24,"normal"))

    if (ball.xcor())<-390:
        ball.goto(0,0)
        ballxdirection=ballxdirection*-1
        Bscore+=1
        pen.clear()
        pen.write("Player A:{}                Player B:{}".format(Ascore,Bscore),align="center",font=("Verdana",24,"normal"))

    #Handling collisions of ball with right paddle

    if(ball.xcor()>340) and (ball.xcor()<350) and (ball.ycor()<rpad.ycor()+40 and ball.ycor()>rpad.ycor()-40):
        ball.setx(340)
        ballxdirection=ballxdirection* -1

    #Handling collisions of ball with left paddle
        
    if(ball.xcor()<-340) and (ball.xcor()>-350) and (ball.ycor()<lpad.ycor()+40 and ball.ycor()>lpad.ycor()-40):
        ball.setx(-340)
        ballxdirection=ballxdirection* -1
