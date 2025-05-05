import turtle

MOVE_X = 30
class Paddle:
    def __init__(self):
        self.paddle = turtle.Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.penup()
        self.paddle.goto(0, -250)

    def move_left(self):
        new_x = self.paddle.xcor() - MOVE_X
        self.paddle.goto(new_x, self.paddle.ycor())

    def move_right(self):
        new_x = self.paddle.xcor() + MOVE_X
        self.paddle.goto(new_x, self.paddle.ycor())

    def drag(self, new_x):
        if self.paddle.xcor() > new_x:
            self.move_left()
        else:
            self.move_right()

        turtle.ondrag(self.drag)

