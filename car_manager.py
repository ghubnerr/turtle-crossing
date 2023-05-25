from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
ROAD_Y_COORDINATES = [[220, 139], [100, 15], [-22, -100], [-145, -225]]  # Road gaps on background png photo


class CarManager:
    """Creates objects that store instances of the turtle class as cars and controls their speed"""
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def add_car(self):
        """Creates an instance of the Turtle class, gives it a random color and y-coordinate to move in the screen"""
        car = Turtle("square")
        car.color(random.choice(COLORS))
        car.penup()
        a, b = random.choice(ROAD_Y_COORDINATES)  # Randomly picks between 1 of the 4 road gaps
        car.goto(310, random.randint(b, a))
        car.shapesize(stretch_len=2)
        car.setheading(180)
        self.cars.append(car)

    def move_cars(self):
        """Moves all car object a set distance according to the speed (difficulty level)"""
        for car in self.cars:
            car.goto(car.xcor() - self.speed, car.ycor())

    def change_speed(self):
        """Increases the speed at which each car moves"""
        self.speed += MOVE_INCREMENT
