import random
import turtle
import os
def draw_figure(colors):
    t = turtle.Pen()
    t.shape("turtle")
    for color in colors:
        t.up()
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        number = random.randint(0,10)
        t.goto(x,y)
        t.down()
        t.color(color)
        t.pencolor("black")
        t.begin_fill()
        print(number)
        if number < 3 :
            t.circle(100)
        else :
            for i in range(number):
                t.forward(100)
                t.left(360/number)
        t.end_fill()
if __name__ == "__main__":
    colors = ['white','yellow','blue','skyblue','orange','green']
    draw_figure(colors)
    os.system("Pause")