import turtle as t
import random

t.bgcolor("orange")
t.up()
t.goto(-230,-230)
t.down()
t.goto(230,-230)
t.goto(230,230)
t.goto(-230,230)
t.goto(-230,-230)
te=t.Turtle()
te.shape("turtle")
te.color("red")
te.up()
te.goto(0,200)
ts=t.Turtle()
ts.shape("circle")
ts.color("green")
ts.up()
ts.goto(0,-200)
t.shape("turtle")
t.color("white")
t.up()
t.goto(0,0)

def turn_right():
    t.setheading(0)

def turn_left():
    t.setheading(180)

def turn_up():
     t.setheading(90)

def turn_down():
    t.setheading(270)

def play():
        t.forward(10)
        ang=te.towards(t.pos())   #t랑 te랑 각도 알려주는 펑션
        te.setheading(ang)
        te.forward(9)
        if t.distance(te)>=12:
           t.ontimer(play,100)
        if t.distance(te)<=12:
           print("잡혔다")
           print("game over")
         
           
        if t.distance(ts)<12:
           print("먹었다")
           star_x=random.randint(-230,230)
           star_y=random.randint(-230,230)
           ts.goto(star_x,star_y)
           
        

t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()
while True:
    play()
    if t.distance(te)<=12:
        break

