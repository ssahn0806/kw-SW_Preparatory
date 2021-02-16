import turtle
import os

color = list()

color.append(input("색상 #1을 입력하시오:"))
color.append(input("색상 #2을 입력하시오:"))
color.append(input("색상 #3을 입력하시오:"))

t = turtle.Pen()
t.shape("turtle")

t.fillcolor(color[0])
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(100,0)
t.down()

t.fillcolor(color[1])
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(200,0)
t.down()

t.fillcolor(color[2])
t.begin_fill()
t.circle(50)
t.end_fill()

os.system("Pause")