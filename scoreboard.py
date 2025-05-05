from turtle import Turtle

class Scoreboard:
    def __init__(self, high):
        self.score = 0
        self.high_score = high
        self.display = Turtle()
        self.display.color("white")
        self.display.penup()
        self.display.hideturtle()
        self.display.goto(-250, 250)
        self.update_score()
        

    def update_score(self):
        self.display.clear()
        self.display.write(f"Score: {self.score}\n"
                           f"HighScore: {self.high_score}", align="left", font=("Arial", 16, "bold"))
        self.high_score = max(self.score, self.high_score)
        

    def increase_score(self):
        self.score += 1
        self.update_score()


