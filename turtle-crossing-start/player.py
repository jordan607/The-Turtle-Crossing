from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.setheading(90)
        self.reset_position()
        self.shape("turtle")
        self.color("red")

    def go_up(self):
        self.forward(20)

    def reset_position(self):
        self.goto(STARTING_POSITION)
