import turtle
import os
import math
import random

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# register shapes
wn.register_shape("tank.gif")
wn.register_shape("alien.gif")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Set score to 0
score = 0

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False,align="left",font=("Arial",14, "normal"))
score_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.color("green")
player.shape("tank.gif")
player.speed(0)
player.penup()
player.setposition(0,-250)
player.setheading(90)

player.speed = 0

# Create projectile
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20
# Bullet projectile will have two states, ready and active
bulletstate = "ready"

# Choose number of enemies
number_of_enemies = 15
# Create empty list of enemies
enemies = []

# Add enemies to list
for i in range(number_of_enemies) :
    # Create one enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("alien.gif")
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(random.randint(-200,200),random.randint(100,250))
    enemyspeed = 1
    
# move the player horizontal
def move_left():
    player.speed = -15
    
def move_right():
    player.speed = 15

def move_player():
    x = player.xcor() + player.speed
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.setx(x)
    

# Fire missile
def fire_proj():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "active"
        bullet.setposition(player.xcor() , player.ycor() + 10)
        bullet.showturtle()

# Check for collisions
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2) + math.pow(t1.ycor() - t2.ycor(),2))
    if distance < 15:
        return True
    else : return False
    
# Create key bindings
wn.listen()
wn.onkeypress(move_left,"a")
wn.onkeypress(move_right,"d")
wn.onkeypress(fire_proj, "space")
gameover = False

# Main game loop
while not gameover:

    move_player()

    # For each enemy move and check for collisions
    for enemy in enemies:
        
        x = enemy.xcor() + enemyspeed
        if x < -280:
            # Move all enemies down
            for e in enemies:
                e.sety(e.ycor() - 40)
            # Change enemy direction
            enemyspeed *= -1
        if x > 280:
            # Move all enemies down
            for e in enemies:
                e.sety(e.ycor() - 40)
            # Change enemy direction
            enemyspeed *= -1
        # Move enemy to new x position
        enemy.setx(x)
        
        if isCollision(bullet , enemy):
            bullet.hideturtle
            bulletstate = "ready"
            bullet.setposition(0,-400)
            enemy.setposition(random.randint(-200,200),random.randint(100,250))
            # Update score
            score += 10
            score_pen.clear()
            scorestring = "Score: {}".format(score)
            score_pen.write(scorestring, False,align="left",font=("Arial",14, "normal"))

        if isCollision(player , enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            print("You Died")
            gameover = True
    
    # move projectile
    if bulletstate == "active":
        bullet.sety(bullet.ycor() + bulletspeed)
        
    # Check if projectile has reached border
    if bullet.ycor() > 280:
        bullet.hideturtle()
        bulletstate = "ready"

        
    
    
