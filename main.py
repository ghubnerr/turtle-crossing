import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

# Set up the screen size, background and event listening
screen = Screen()
screen.bgpic("road.png")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Create objects
cars = CarManager()
turtle = Player()
scoreboard = Scoreboard()

# Set keys for moving the turtle
screen.onkey(turtle.move_up, "Up")
screen.onkey(turtle.move_down, "Down")
screen.onkey(turtle.move_left, "Left")
screen.onkey(turtle.move_right, "Right")

# Loops while the game is on to generate cars and move them
game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)

    # Generates a car every 7 ticks
    if counter % 7 == 0:
        cars.add_car()
    cars.move_cars()
    screen.update()
    counter += 1

    # Detecting if turtle reached the finish line and increasing difficulty
    if turtle.ycor() == FINISH_LINE_Y:
        turtle.reset_turtle()
        scoreboard.add_score()
        cars.change_speed()

    # Detecting collision with cars
    for car in cars.cars:
        if turtle.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()


