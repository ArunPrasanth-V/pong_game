from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.goto(xcor, ycor)
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def mov_up(self):
        self.goto(self.xcor(), 30 + self.ycor())

    def mov_down(self):
        self.goto(self.xcor(), self.ycor() - 30)
