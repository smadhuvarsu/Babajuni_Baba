import turtle
from random import randint

turtle.pensize=3
for i in range(10000000000000000000000000000000000000000):
    turtle.color=[randint(0,255),randint(0,255),randint(0,255)]
    for i in range(5):
        turtle.lt(140)
        turtle.fd(5)
        turtle.penup()
        turtle.fd(34)
        turtle.pendown()
    



