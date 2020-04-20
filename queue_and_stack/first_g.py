#Space invaders - Part 1
#Set up the screen


import turtle
import os

#Set up screen
f_s = turtle.Screen()
f_s.bgcolor("black")
f_s.title("Space Invaders")


#Draw border
border_pen  = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd( 600)
    border_pen.lt(90)
border_pen.hideturtle()

#Creat the player turetle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15
#create enemy
enemy = turtle.Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.penup()
enemy.speed(0)
enemy.setposition(-250, 250)

enemyspeed = 2

#Move the playere left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = + 280
    player.setx(x)
def move_up():
    y = player.ycor()
    y += playerspeed
    if y < + 3:
        y = +3
    player.sety(y)
def move_down():
    y = player.ycor()
    y -=playerspeed
    player.sety(y)

#Creat keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")

#main game loop
while True:

    #move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    #move the enemy back and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)
    
    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)


delay = input("Press enter to finish")