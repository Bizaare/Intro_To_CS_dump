# Author : Levi Yates
# Date   : 2022-12-05
# This program experiments with turtle graphics

import turtle
import random


t =turtle.Pen()
t.shape("classic")

t.speed(0) # 1 is the slowest.

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

t.up()
t.forward(50)
t.down()

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

t.reset()

t.write("Hello Turtle Boys", False, "left", ('Arial', 14, 'normal'))

t.up()
t.right(90)
t.forward(50)
t.left(90)
t.down

t.color('red', 'green')
t.begin_fill()
for x in range(1, 9):
    t.speed(0)
    t.forward(100)
    t.right(135)

t.end_fill()

t.up()
t.forward(150)
t.down()

t.color(0.5, 0, 0.5)
for x in range(1, 9):
    t.speed(0)
    t.forward(100)
    t.right(135)

t.up()
t.backward(400)
t.left(90)
t.forward(250)

t.color("#000080")

t.down()
t.begin_fill()
t.circle(20)
t.end_fill()

t.down()
t.begin_fill()
t.circle(20)
t.end_fill()

t.up()
t.forward(20)


# Grill Slots
for x in range(1,8):
    t.speed(0)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.down()
    t.forward(100)
    t.up()
    t.left(180)
    t.forward(100)

t.right(90)
t.forward(20)
t.right(90)
t.forward(20)
t.down()
t.begin_fill()
t.circle(20)
t.end_fill()
t.up()

# end jeep


t.speed(0)
t.hideturtle()
t.backward(200)
t.color("blue", "yellow")
random.seed(672)
t.pensize(3)

t.down()
t.begin_fill()
t.circle(10)
t.end_fill()
t.up()

i = 0
while i < 50:
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)

    if not (x < 0 and y > 60):

        t.goto(x, y)
        t.color((random.random(), random.random(), random.random()), (random.random(), random.random(), random.random()))
        t.down()
        t.begin_fill()
        t.circle(random.randint(5, 31))
        t.end_fill()
        t.up()

        i += 1


t.pensize(5)
t.up()
t.forward(150)
t.down()
t.backward(30)
t.left(90)
t.forward(90)
t.right(90)
t.backward(60)
t.right(90)
t.forward(200)


t.forward(30)
t.right(90)
t.backward(90)
t.left(90)
t.forward(60)
t.left(90)
t.backward(200)

t.color("green")
t.forward(120)
t.left(90)
t.forward(120)
t.left(90)
t.forward(120)
t.left(90)
t.forward(120)

t.up()
t.forward(50)
t.down()

t.color("red")
t.forward(120)
t.left(90)
t.forward(120)
t.left(90)
t.forward(120)
t.left(90)
t.forward(120)

t.up()
t.right(180)
t.forward(200)
t.down()

t.color('purple')
t.begin_fill()
for x in range(1, 9):
    t.speed(0)
    t.forward(100)
    t.right(135)
