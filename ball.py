from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self, move_distance=10):
        self.goto(self.xcor()+move_distance, self.ycor()+move_distance)
