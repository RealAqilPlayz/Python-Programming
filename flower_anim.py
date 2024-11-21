import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()

# Create a turtle for drawing
t = turtle.Turtle()
t.shape('turtle')
t.hideturtle()
screen.tracer(0)
screen.colormode(255)


def draw_flower(angle):
    t.pensize(10)
    t.pencolor((0, 128, 19))
    t.penup()
    t.goto(0, -380)
    t.setheading(90)
    t.pendown()

    # Draw stem
    for i in range(100):
        t.forward(3)
        t.right(angle)

    # Draw concentric circles for the petal
    t.pencolor((255, 0, 0))
    t.pensize(120)
    t.forward(1)
    t.forward(-1)

    t.pencolor((255, 132, 0))
    t.pensize(60)
    t.forward(1)
    t.forward(-1)


angle = 0
leaning_towards_right = True
while True:
    t.clear()
    draw_flower(angle)
    screen.update()
    time.sleep(0.1)

    if leaning_towards_right == True:
        if angle < 0.5:
            angle = angle + 0.05
        else:
            leaning_towards_right = False

    else:
        if angle > -0.5:
            angle = angle - 0.05
        else:
            leaning_towards_right = True



# Keep the screen on
screen.mainloop()















