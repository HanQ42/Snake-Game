# Snake Snape Skape Skate

import turtle
import time
import random


gameWindow = turtle.Screen()
gameWindow.title("Snake")
gameWindow.setup(width = 800, height = 600)
gameWindow.bgcolor("#2A363B")
gameWindow.tracer(0)
delay = 0.2

# Color Palette
foodColor = "#E84A5F"
borderColor = "#99B898"
headColor = "#FFFFFF"
bodyColor = "#E0E0E0"

# Game border
gameFrame = turtle.Turtle()
gameFrame.penup()
gameFrame.goto(0,290)
gameFrame.shape("square")
gameFrame.color(borderColor)
gameFrame.shapesize(1, 40)

gameFrame = turtle.Turtle()
gameFrame.penup()
gameFrame.goto(0,-280)
gameFrame.shape("square")
gameFrame.color(borderColor)
gameFrame.shapesize(1, 40)

gameFrame = turtle.Turtle()
gameFrame.penup()
gameFrame.goto(-390,0)
gameFrame.shape("square")
gameFrame.color(borderColor)
gameFrame.shapesize(30,1)

gameFrame = turtle.Turtle()
gameFrame.penup()
gameFrame.goto(380,0)
gameFrame.shape("square")
gameFrame.color(borderColor)
gameFrame.shapesize(30,1)

#Upper border line
gameFrame = turtle.Turtle()
gameFrame.penup()
gameFrame.goto(0,200)
gameFrame.shape("square")
gameFrame.color(borderColor)
gameFrame.shapesize(1, 40)


# Snake head
snakeHead = turtle.Turtle()
snakeHead.speed(0)
snakeHead.shape("square")
snakeHead.color("white")
snakeHead.penup()
snakeHead.goto(0,0)
snakeHead.direction = "up"

# Snake body
snakeSeg = []

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color(foodColor)
food.penup()

food.goto(random.randrange(-360, 360, 20), random.randrange(-260, 160, 20))
while food.xcor() == snakeHead.xcor() and food.ycor() == snakeHead.ycor():
    food.goto(random.randrange(-360, 360, 20), random.randrange(-260, 160, 20))

# Scoring
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.shape("square")
pen.color("white")
pen.hideturtle()
pen.goto(0, 228)
pen.write("Score: 0          High Score: 0", align="center", font=("Myriad", 33, "normal"))
score = 0
highScore = 0

# set the snake head direction
def goUp():
    if snakeHead.direction != "down":
        snakeHead.direction = "up"
def goDown():
    if snakeHead.direction != "up":
        snakeHead.direction = "down"
def goLeft():
    if snakeHead.direction != "right":
        snakeHead.direction = "left"
def goRight():
    if snakeHead.direction != "left":
        snakeHead.direction = "right"

# inputs from keyboard
gameWindow.listen()
gameWindow.onkey(goUp, "w")
gameWindow.onkey(goDown, "s")
gameWindow.onkey(goLeft, "a")
gameWindow.onkey(goRight, "d")

def movement():
    if snakeHead.direction == "up":
        snakeHead.sety(snakeHead.ycor() + 20)
    if snakeHead.direction == "down":
        snakeHead.sety(snakeHead.ycor() - 20)
    if snakeHead.direction == "left":
        snakeHead.setx(snakeHead.xcor() - 20)
    if snakeHead.direction == "right":
        snakeHead.setx(snakeHead.xcor() + 20)

# game loop
while True:

    if snakeHead.xcor() > 360 or snakeHead.xcor() < -370 or snakeHead.ycor() < -260 or snakeHead.ycor() > 180:
        time.sleep(1)
        delay = 0.2
        snakeHead.goto(0,0)
        food.goto(random.randrange(-360,360,20), random.randrange(-260,160,20))
        snakeHead.direction = "up"
        for index in snakeSeg:
            index.goto(1000,1000)
        snakeSeg = []
        # score clear
        score = 0
        pen.clear()
        pen.write("Score: {}          High Score: {}".format(score, highScore), align="center", font=("Myriad", 33, "normal"))

    for index in range(len(snakeSeg)-1, 0, -1):
        snakeSeg[index].goto(snakeSeg[index-1].xcor(),snakeSeg[index-1].ycor())
    # seg0
    if len(snakeSeg) > 0:
        snakeSeg[0].goto(snakeHead.xcor(), snakeHead.ycor())

    movement()
    gameWindow.update()
    if food.distance(snakeHead) < 20:
        food.goto(random.randrange(-360,360,20), random.randrange(-260,160,20))

        newSeg = turtle.Turtle()
        newSeg.speed(0)
        newSeg.shape("square")
        newSeg.color(bodyColor)
        newSeg.penup()
        snakeSeg.append(newSeg)

        delay -= 0.001
        score += 1
        if score > highScore:
            highScore = score
        pen.clear()
        pen.write("Score: {}          High Score: {}".format(score, highScore), align="center", font=("Myriad", 33, "normal"))

    # died
    for seg in snakeSeg:
        if seg.distance(snakeHead) < 20:
            time.sleep(1)
            delay = 0.2
            snakeHead.goto(0,0)
            food.goto(random.randrange(-360,360,20), random.randrange(-260,160,20))
            snakeHead.direction = "up"
            score = 0
            pen.clear()
            pen.write("Score: {}          High Score: {}".format(score, highScore), align="center", font=("Myriad", 33, "normal"))
            for index in snakeSeg:
                index.goto(1000, 1000)
            snakeSeg = []
    time.sleep(delay)

turtle.mainloop()