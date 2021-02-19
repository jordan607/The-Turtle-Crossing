import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
level = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.cars()
    car.move()

    if player.ycor() > 280:
        player.reset_position()
        level.score()

    for cars in car.all_cars:
        if player.distance(cars)<25:
            level.game_over()
            game_is_on = False

screen.exitonclick()