import turtle
import time

# Set up the screen
screen = turtle.Screen()

# Create a turtle for drawing
t = turtle.Turtle()
t.shape('turtle')
t.hideturtle()
screen.tracer(0)


def draw_square(x):
    t.pensize(10)
    t.penup()
    t.goto(x, 0)
    t.setheading(0)
    t.pendown()

    for i in range(4):
        t.forward(50)
        t.right(90)


x = -400
while True:
    t.clear()
    draw_square(x)
    if x > 400:
        x = -400
    else:
        x = x + 20
    screen.update()
    time.sleep(0.1)



# Keep the screen on
screen.mainloop()