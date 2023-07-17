from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self, move_distance=20):
        y_cor = self.ycor()
        self.goto(self.xcor(), y_cor + move_distance)

    def down(self, move_distance=20):
        y_cor = self.ycor()
        self.goto(self.xcor(), y_cor - move_distance)

    # def down(self):
    #     if self.head.heading() != UP:
    #         self.head.setheading(DOWN)
