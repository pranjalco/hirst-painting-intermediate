import turtle
import random

"P13"


def starting_point():
    tim.hideturtle()
    tim.penup()
    tim.goto(-250, -225)


def draw_line():
    tim.showturtle()
    tim.pendown()
    tim.forward(0)
    for _ in range(9):
        tim.penup()
        tim.color(random.choice(color_list))
        tim.forward(50)
        tim.pendown()
        tim.forward(0)


def turn_and_move():
    global distance
    tim.left(90)
    distance += 50
    tim.forward(distance)
    tim.right(90)


turtle.colormode(255)
color_list = [(2, 30, 9), (122, 41, 95), (72, 22, 32), (237, 72, 212), (220, 59, 81), (225, 100, 117), (93, 21, 1),
              (178, 170, 140), (150, 115, 92), (34, 26, 90), (7, 73, 154), (205, 91, 63), (168, 77, 129), (1, 147, 64),
              (4, 218, 221), (3, 28, 78), (220, 218, 178), (79, 179, 135), (124, 178, 154), (80, 138, 110),
              (121, 164, 185), (10, 221, 214), (121, 33, 13), (243, 7, 204), (133, 208, 222), (229, 165, 174)]
distance = 0

tim = turtle.Turtle()
tim.pensize(20)
tim.speed("fastest")
screen = turtle.Screen()
screen.title("Hirst Painting by Pranjal Sarnaik")

starting_point()
last_step = 0
for _ in range(10):
    draw_line()
    starting_point()
    if last_step != 9:
        turn_and_move()
        tim.showturtle()
        last_step += 1

screen.exitonclick()
