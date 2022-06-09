from turtle import *
from random import randint


Screen().bgcolor("#2e2e2e")

turt = Turtle()
turt.penup()
turt.speed(0)
turt.goto(-300, 100)


for step in range(1, 16):
    turt.color("white")
    turt.write(step, align="center", font=("Arial", 20, "normal"))
    turt.right(90)
    turt.forward(10)
    turt.pendown()
    turt.forward(250)
    turt.penup()
    turt.backward(260)
    turt.left(90)
    turt.forward(40)

bobby = Turtle()
bobby.penup()
bobby.shape("turtle")
bobby.color("red")
bobby.goto(-325, 70)
bobby.pendown()

glorb = Turtle()
glorb.penup()
glorb.shape("turtle")
glorb.color("orange")
glorb.goto(-325, 40)
glorb.pendown()

randy = Turtle()
randy.penup()
randy.shape("turtle")
randy.color("gold")
randy.goto(-325, 10)
randy.pendown()

alex = Turtle()
alex.penup()
alex.shape("turtle")
alex.color("green")
alex.goto(-325, -20)
alex.pendown()

paul = Turtle()
paul.penup()
paul.shape("turtle")
paul.color("blue")
paul.goto(-325, -50)
paul.pendown()


tarzo = Turtle()
tarzo.penup()
tarzo.shape("turtle")
tarzo.color("indigo")
tarzo.goto(-325, -80)
tarzo.pendown()

emilia = Turtle()
emilia.penup()
emilia.shape("turtle")
emilia.color("violet")
emilia.goto(-325, -110)
emilia.pendown()

for step in range(10):
    bobby.left(36)
    glorb.right(36)
    randy.left(36)
    alex.right(36)
    paul.left(36)
    tarzo.right(36)
    emilia.left(36)


for step in range(125):
    bobby.forward(randint(2,8))
    glorb.forward(randint(2,8))
    randy.forward(randint(2,8))
    alex.forward(randint(2,8))
    paul.forward(randint(2,8))
    tarzo.forward(randint(2,8))
    emilia.forward(randint(2,8))





done()
