from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            square = Turtle('square')
            square.color('white')
            square.penup()
            square.goto(position)
            self.segments.append(square)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[segment - 1].xcor()
            y_cor = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x_cor, y_cor)
        self.segments[0].forward(MOVE)
