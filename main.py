from turtle import Screen, Turtle

screen = Screen()
paddle1 = Turtle()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game ")
screen.tracer(0)


def mov_up():
    paddle1.goto(paddle1.xcor(), 30 + paddle1.ycor())


def mov_down():
    paddle1.goto(paddle1.xcor(), paddle1.ycor() - 30)


paddle1.penup()
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.goto(350, 0)

screen.listen()
screen.onkey(mov_up, "Up")
screen.onkey(mov_down, "Down")
gameis_ON = True
while gameis_ON:
    screen.update()

screen.exitonclick()
