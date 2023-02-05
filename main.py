# create the screen
# screen width = 800 and height = 600
# create and move a paddle
# create another paddle
# create the ball and make it move
# detect collision with
# detect collision with paddle
# detect when paddle misses
# keep score

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

# screen setup
screen = Screen()
screen.screensize(800, 600, "black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "o")
screen.onkey(r_paddle.go_down, "l")


game_is_on = True
while game_is_on == True:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
