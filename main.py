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
from scoreboard import Scoreboard
import time


# screen setup
screen = Screen()
screen.screensize(800, 600, "black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "o")
screen.onkey(r_paddle.go_down, "l")


game_is_on = True

while game_is_on == True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detecting collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        # need to bounce
        ball.bounce_y()
        ball.move_speed *= 0.9

    # detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 0.9

    # detect R paddle misses
    if ball.xcor() > 360:
        ball.reset_position()
        scoreboard.l_point()

    # detect L paddle misses
    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.r_point()

    scoreboard.update_score()
screen.exitonclick()
