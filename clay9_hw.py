import turtle as t 
t.shape("turtle")      #거북이의모양을거북이로한다
t.bgcolor("black")     #바탕색을 검정으로한다
t.color("red")         #거북이색을 빨강으로한다
t.speed(0)             #거북이를 제일 빠르게 한다
x=input("50+20= ")     #문제를 보여주고 입력받은 답을 x에 저장한다
a=int(x)               #x에 저장된 문자열을 정수로 바꾼다
if a==50+20:           #만약 a가 70이면
 for x in range(60):   #60번 반복해라
  t.circle(5)          #반지름이5인원을그린다
  t.up()               #팬을 투명하게 바꾼다
  t.forward(10)        #앞으로 10만큼 간다
  t.lt(6)              #왼쪽으로 6도 튼다
  t.down()             #펜색이 다시 나오게 한다
else:                  #다른답이면
 t.rt(45)              #오른쪽으로 45도 틀고
 for x in range(60):   #60번반복해라
   t.up()              #팬색을 없애고
   t.forward(3)        #앞으로 3만큼가고
   t.down()            #팬색을 있게한다음
   t.circle(5)         #반지름이 5인원을 그려라
 t.rt(135)             #오른쪽으로 135도 틀고
 t.up()                #팬색을 없앤다음
 t.forward(140)        #거북이가 140만큼 가게한다
 t.down()              #다시 팬색을 있게하고
 t.rt(135)             #오른쪽으로 135도 튼다
 for x in range(60):   #60번 반복해라
    t.circle(5)        #반지름이5인원을그려라
    t.up()             #팬색을없애고
    t.forward(3)       #앞으로3만큼가고
    t.down()           #팬색을 다시 있게해라
