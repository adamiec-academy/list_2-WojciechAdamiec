from turtle import forward, penup, pendown, right, left, exitonclick, speed
from random import randint


def bar(n):
    pendown()
    for _ in range(2):
        forward(n)
        right(90)
        forward(20)
        right(90)
    penup()


speed("fastest")
penup()
right(180)
forward(500)
left(90)
forward(200)
left(180)
acc = 30

for i in range(25):
    acc = acc + randint(-3, 40)
    bar(acc)
    right(90)
    forward(30)
    left(90)

exitonclick()
