from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game ")
screen.tracer(0)
ball=Ball()

l_paddle=Paddle(350,0)

r_paddle=Paddle(-350,0)


screen.listen()
screen.onkey(l_paddle.mov_up, "Up")
screen.onkey(l_paddle.mov_down, "Down")
screen.onkey(r_paddle.mov_up, "w")
screen.onkey(r_paddle.mov_down, "s")



gameis_ON = True
while gameis_ON:
    time.sleep(0.1)
    screen.update()
    ball.mov()

    # Detect the collision
    if ball.ycor()>280 or ball.ycor()<-280:
        # Need to bounce
         ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and r_paddle.xcor() > 320 or ball.distance(l_paddle) < 50 and r_paddle.xcor() < -320:
        ball.bounce_x()

screen.exitonclick()

