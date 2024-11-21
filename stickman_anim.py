import turtle
import time
import random
import math

# Set up the screen
screen = turtle.Screen()

# Create a turtle for drawing
t = turtle.Turtle()
t.shape('turtle')
t.hideturtle()
screen.tracer(0)
screen.colormode(255)

def draw_head(x, y, size):
    t.pensize(5)
    t.pencolor((0, 0, 0))
    t.penup()
    t.goto(x, y)
    t.setheading(180)
    t.pendown()
    for i in range(360):
        t.forward(size / 360)
        t.right(1)
    t.penup()


def draw_body(x, y, height):
    t.pensize(5)
    t.pencolor((0, 0, 0))
    t.penup()
    t.goto(x, y)
    t.setheading(270)
    t.pendown()
    t.forward(height)
    t.penup()



def draw_arm(x, y, flex_amount, dir):
    t.pensize(5)
    t.pencolor((0, 0, 0))
    t.penup()
    t.goto(x, y)
    t.setheading(270 - ((math.sin(frame_no) * ((flex_amount * 4) + 3)) * dir))
    t.pendown()
    t.forward(17)
    t.left(flex_amount * 4.5)
    t.forward(25)
    t.penup()


def draw_leg(x, y, flex_amount, dir):
    t.pensize(5)
    t.pencolor((0, 0, 0))
    t.penup()
    t.goto(x, y)
    t.setheading(270 - ((math.sin(frame_no) * ((flex_amount * 4) + 3)) * dir))
    t.pendown()
    t.forward(20)
    if (flex_amount * 3) > 16: # high flex amount, high walk speed
        t.right(16)
    else: # low flex amount, low walk speed
        t.right(flex_amount * 3)
    t.forward(30)


def draw_bg_lines(x, y):
    t.pensize(15)
    t.pencolor((0, 0, 0))
    t.penup()
    t.goto(x, y)
    t.setheading(0)

    for i in range(40):
        t.pendown()
        t.forward(50)
        t.penup()
        t.forward(50)



frame_no = 0
x = 300
y = -150
while True:
    t.clear()
    draw_head(0, 0, 100) # can call draw_head multiple times at different size and pos to draw eyes and mouth
    draw_body(0, 0, 80)
    draw_arm(0, -20, 20, 1)
    draw_arm(0, -20, 20, -1)
    draw_leg(0, -80, 10, 1)
    draw_leg(0, -80, 10, -1)

    draw_bg_lines(x, y)
    if x < -600:
        x = -300
    x = x - 10

    frame_no = frame_no + 100
    time.sleep(0.01)

    screen.update()





# Keep the screen on
screen.mainloop()















