from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.all_cars=[]

    def cars(self):
        random_chance= random.randint(1,3)
        if random_chance == 1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.pu()
            new_car.color(random.choice(COLORS))
            new_car.goto(320, random.randint(-220, 250))
            self.all_cars.append(new_car)

    def move(self):
        for cars in self.all_cars:
            cars.backward(STARTING_MOVE_DISTANCE)

    def speed_inc(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        print(STARTING_MOVE_DISTANCE)