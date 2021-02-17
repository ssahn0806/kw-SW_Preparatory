import turtle
import math
import os

x1 = int(input("첫번째 원의 중심 x좌표를 입력하시오:"))
y1 = int(input("첫번째 원의 중심 y좌표를 입력하시오:"))
r1 = int(input("첫번째 원의 반지름의 길이를 입력하시오:"))
x2 = int(input("두번째 원의 중심 x좌표를 입력하시오:"))
y2 = int(input("두번째 원의 중심 y좌표를 입력하시오:"))
r2 = int(input("두번째 원의 반지름의 길이를 입력하시오:"))

d = math.sqrt((x1-x2)**2+(y1-y2)**2)
sum_r = r1+r2

t1 = turtle.Pen()
t1.shape("arrow")
t1.up()
t1.goto(x1,y1-r1)
t1.down()
t1.circle(r1)

t2 = turtle.Pen()
t2.shape("turtle")
t2.up()
t2.goto(x2,y2-r2)
t2.down()
t2.circle(r2)

os.system("Pause")
