from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x = 10
        self.move_y = 10
    def move(self):
        self.goto(self.xcor()+self.move_x, self.ycor()+self.move_y)

    def bounce(self):
        self.move_y *= -1

