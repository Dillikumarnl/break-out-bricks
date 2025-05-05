from turtle import Turtle

class Bricks:
    def __init__(self):
        self.bricks = []
        self.create_bricks()

    def create_bricks(self):
        colors = ["red", "orange", "yellow", "green", "blue"]
        for i in range(5):
            for j in range(8):
                brick = Turtle()
                brick.shape("square")
                brick.color(colors[i])
                brick.shapesize(stretch_wid=1, stretch_len=2)
                brick.penup()
                brick.goto(-210 + (j * 60), 200 - (i * 30))
                self.bricks.append(brick)
                self.bricks_count = len(self.bricks)

    def remove_brick(self, brick):
        brick.hideturtle()
        self.bricks.remove(brick)
        self.bricks_count -= 1

