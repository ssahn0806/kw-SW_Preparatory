import random
import turtle
import os
def draw_rect(colors):
    t = turtle.Pen()
    t.shape("turtle")
    for color in colors:
        t.up()
        x = random.randint(-100,100)
        y = random.randint(-100,100)
        t.goto(x,y)
        t.down()
        t.color(color)
        t.pencolor("black")
        t.begin_fill()
        for i in range(4):
            t.forward(100)
            t.left(90)
        t.end_fill()
if __name__ == "__main__":
    colors = ['yellow','red','purple','blue']
    draw_rect(colors)
    os.system("Pause")