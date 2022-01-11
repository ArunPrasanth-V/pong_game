from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")


    def mov(self):
        self.goto(self.xcor()+10,self.ycor()+10)