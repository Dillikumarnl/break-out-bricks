import time
import turtle
from ui import UI
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from bricks import Bricks

with open("highestScore.txt", mode='r') as highscore:
    high = int(highscore.read())


# Initialize the game window
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Create game elements
ui = UI()
paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard(high)
bricks = Bricks()

screen.listen()
screen.onkey(paddle.move_right, "Up")
screen.onkey(paddle.move_left, "Down")
screen.onkey(paddle.move_right, "Right")
screen.onkey(paddle.move_left, "Left")


# method to call on drag
def fxn(x, y):
    paddle.paddle.ondrag(None)
    if 290 > paddle.paddle.xcor():
        paddle.paddle.goto(x, y=paddle.paddle.ycor())
        paddle.paddle.goto(x=paddle.paddle.xcor() - 10, y=paddle.paddle.ycor())
    if paddle.paddle.xcor() > -290:
        paddle.paddle.goto(x, y=paddle.paddle.ycor())
        paddle.paddle.goto(x=paddle.paddle.xcor() + 10, y=paddle.paddle.ycor())
    paddle.paddle.ondrag(fxn)


# Game loop
game_on = True
while game_on:
    screen.update()
    ball.move()

    # Detect collision with paddle
    if ball.ycor() < -240 and ball.distance(paddle.paddle) < 80:
        ball.bounce_y()

    # Detect collision with wall
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.bounce_x()
    if ball.ycor() > 290:
        ball.bounce_y()

    # Detect collision with bricks
    for brick in bricks.bricks:
        if ball.distance(brick) < 30:
            ball.bounce_y()
            bricks.remove_brick(brick)
            scoreboard.increase_score()

    # Detect game over condition
    if ball.ycor() < -290:
        game_on = False
        ui.game_over()

    paddle.paddle.ondrag(fxn)

    # Wish them congrats Who Breaks all Bricks.
    if bricks.bricks_count == 0:
        game_on = False
        ui.smashed_all()

with open("highestScore.txt", mode='w') as highscore:
    highscore.write(str(scoreboard.high_score))


screen.exitonclick()
