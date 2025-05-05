import time
import turtle
import random

FONT = ("Courier", 52, "normal")
FONT2 = ("Courier", 32, "normal")
ALIGNMENT = 'center'
COLOR = "white"
COLOR_LIST = ['light blue', 'royal blue',
              'light steel blue', 'steel blue',
              'light cyan', 'light sky blue',
              'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink',
              'medium sea green', 'khaki']

class UI:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Breakout Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=600, height=600)

    def game_over(self):
        message = turtle.Turtle()
        message.color("white")
        message.hideturtle()
        message.write("Game Over!", align="center", font=("Arial", 24, "bold"))

    def smashed_all(self):
        message = turtle.Turtle()
        message.color("white")
        message.hideturtle()
        message.write("You BreakOut All Bricks🔥!", align="center", font=("Arial", 24, "bold"))