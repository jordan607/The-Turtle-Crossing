from car_manager import CarManager
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.level=1
        self.update_score()

    def update_score(self):
        self.goto(-290,260)
        self.write(f"Level:{self.level}", "center", font=FONT)

    def score(self):
            self.level+=1
            self.clear()
            self.update_score()
            CarManager().speed_inc()

    def game_over(self):
        self.goto(-100, 0)
        self.write("Game Over", "center", font=FONT)

