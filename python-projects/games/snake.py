import turtle

#set up the screen
win = turtle.Screen()
win.title("El Snake Game")
win.bgcolor("black")
win.setup(width=600,height=600)
win.tracer(0)

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor() #y coordinate of the turtle
        head.sety(y + 0.25)
 
    if head.direction == "down":
        y = head.ycor() #y coordinate of the turtle
        head.sety(y - 0.25)
 
    if head.direction == "right":
        x = head.xcor() #y coordinate of the turtle
        head.setx(x + 0.25)
 
    if head.direction == "left":
        x = head.xcor() #y coordinate of the turtle
        head.setx(x - 0.25)

def go_up():
    if head.direction != "down":
        head.direction = "up"
 
def go_down():
    if head.direction != "up":
        head.direction = "down"
 
def go_right():
    if head.direction != "left":
        head.direction = "right"
 
def go_left():
    if head.direction != "right":
        head.direction = "left"


# keyboard bindings
win.listen()
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.onkey(go_right, "Right")
win.onkey(go_left, "Left")

# Main game loop
while True:
    win.update()
    move()