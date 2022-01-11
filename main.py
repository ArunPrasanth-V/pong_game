from turtle import Screen, Turtle
from paddle import Paddle
screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game ")
screen.tracer(0)

l_paddle=Paddle(350,0)

r_paddle=Paddle(-350,0)


screen.listen()
screen.onkey(l_paddle.mov_up, "Up")
screen.onkey(l_paddle.mov_down, "Down")
screen.onkey(r_paddle.mov_up, "w")
screen.onkey(r_paddle.mov_down, "s")



gameis_ON = True
while gameis_ON:
    screen.update()
screen.exitonclick()

