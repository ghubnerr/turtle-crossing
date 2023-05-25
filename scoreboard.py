from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Inherits from the Turtle class to create an object that can write on the screen"""
    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()  # Hides the object
        self.goto(-260, 260)  # Fixed scoreboard positioning
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears previous score (if any) and writes the most recent one"""
        self.clear()
        self.write(f"Level: {self.score}", font=FONT)

    def add_score(self):
        """Increases the score attribute and calls for an update"""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Prints game over on top of the screen"""
        self.goto(-75, 250)
        self.write("GAME OVER", font=FONT)
