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

# screen setup
screen = Screen()
screen.screensize(800, 600, "black")
screen.title("Pong")
screen.tracer(0)

# create paddle
paddle = Turtle()
paddle.color("white")
paddle.shape("square")
paddle.shapesize(5, 1)
paddle.penup()
paddle.goto(350, 0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")

game_is_on = True
while game_is_on == True:
    screen.update()

screen.exitonclick()
