from turtle import Turtle

class Ball(Turtle):  # Inheriting from Turtle
    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        self.shape("circle")
        self.color("white")
        self.penup()  # Prevent drawing a trail
        self.goto(0, 0)
        self.dx = 0.3  # Horizontal movement
        self.dy = -0.3  # Vertical movement

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.dx *= -1

    def bounce_y(self):
        self.dy *= -1
