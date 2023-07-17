from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong game")
screen.tracer(0)


paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

screen.update()

screen.exitonclick()