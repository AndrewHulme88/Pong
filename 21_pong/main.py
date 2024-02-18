import turtle
import paddle
import ball
import time
import score

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong - Python Edition")
screen.tracer(0)

right_paddle = paddle.Paddle((350, 0))
left_paddle = paddle.Paddle((-350, 0))
ball = ball.Ball()
score = score.Score()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_running = True
while game_is_running:
    time.sleep(0.1)
    screen.update()
    ball.launch_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 360:
        score.left_point()
        game_is_running = False
        ball.reset_ball()
        left_paddle.goto(-350, 0)
        right_paddle.goto(350, 0)
        ball.x_move *= -1
        screen.update()
        time.sleep(1)
        time.sleep(0.1)
        game_is_running = True

    if ball.xcor() < -360:
        score.right_point()
        game_is_running = False
        ball.reset_ball()
        left_paddle.goto(-350, 0)
        right_paddle.goto(350, 0)
        ball.x_move *= -1
        screen.update()
        time.sleep(1)
        time.sleep(0.1)
        game_is_running = True


screen.exitonclick()
