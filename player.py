from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    """Inherits from the Turtle class to create a player that can be moved around and reset to its starting position"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pencolor("black")
        self.fillcolor("forest green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        """Faces north and moves a set distance"""
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        """Faces south and moves a set distance"""
        self.setheading(270)
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        """Faces west and moves a set distance"""
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def move_right(self):
        """Faces east and moves a set distance"""
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def reset_turtle(self):
        """Returns to its starting position while also setting its heading to north"""
        self.goto(STARTING_POSITION)
        self.setheading(90)
