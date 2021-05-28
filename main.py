import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

game_on = True

starting_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_position:
    square = Turtle('square')
    square.color('white')
    square.penup()
    square.goto(position)
    segments.append(square)

while game_on:
    screen.update()
    time.sleep(0.1)
    for segment in range(len(segments) - 1, 0, -1):
        x_cor = segments[segment - 1].xcor()
        y_cor = segments[segment - 1].ycor()
        segments[segment].goto(x_cor, y_cor)
    segments[0].forward(20)

screen.exitonclick()
