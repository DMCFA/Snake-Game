from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        square = Turtle('square')
        square.color('white')
        square.penup()
        square.goto(position)
        self.segments.append(square)

    def grow_snake(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[segment - 1].xcor()
            y_cor = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x_cor, y_cor)
        self.head.forward(MOVE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)