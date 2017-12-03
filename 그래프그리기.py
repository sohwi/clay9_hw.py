import turtle as t
import math

x_min=-5
x_max=5

y_min=-5
y_max=5

space=0.1
t.setworldcoordinates(x_min, y_min, x_max, y_max)
t.up()
t.goto(x_min,0)
t.down()
t.goto(x_max,0)
t.up()
t.goto(0,y_min)
t.down()
t.goto(0,y_max)


t.speed(0)
t.pensize(2)
t.color("green")


func1=input("원하는 함수1를 입력하세요")
func2=input("원하는 함수2를 입력하세요")

list1=[]
list2=[]

x= x_min
exec(func1)
t.up()
t.goto(x,y)
t.down()
while x <= x_max:
    x= x + space
    exec(func1)
    list1.append(y)
    t.goto(x,y)
x=x_min
exec(func2)
t.up()
t.goto(x,y)
t.down()
while x <= x_max:
    x= x + space
    list2.append(y)
    exec(func2)
    t.goto(x,y)

print(list1)
print(list2)

for x in range(0,51):
   if abs(list1[x]-list2[x])<0.2:
    print("교점발견","좌표:",(x,y))
