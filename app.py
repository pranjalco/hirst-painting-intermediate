import turtle
import random

"""
# Hirst Painting
A Python program that generates a Hirst-style painting by extracting colors from an image using `colorgram` and creating a 10x10 grid of colorful dots with `turtle`.  

## Author
Pranjal Sarnaik

## Features
- Extracts colors from an image using `colorgram`.  
- Uses `turtle` to create a 10x10 grid of randomly selected dots.  
- Functions handle positioning and drawing for an organized layout.  
- Separate script to extract and manually transfer colors.  
- Simple and visually appealing artistic output.  

## Level
Intermediate

## Tech Stack
Python | Turtle | Colorgram | Random | GUI-based Programming | Automation | Image Processing

## How to Run
1. Clone the repo:  
   ```bash  
   git clone https://github.com/pranjalco/hirst-painting-intermediate.git

2. Install the required dependencies:
   ```bash
   pip install colorgram.py

3. Run:
    ```bash  
   python app.py

## Final Output Path:  `./screenshots/hirst_painting_final_output.PNG`
"""


def starting_point():
    """Fixes the starting position of the painting."""
    tim.hideturtle()
    tim.penup()
    tim.goto(-250, -225)


def draw_line():
    """Draws a straight line of 10 dots."""
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
    """Moves the turtle to the next row."""
    global DISTANCE
    tim.left(90)
    DISTANCE += 50
    tim.forward(DISTANCE)
    tim.right(90)


turtle.colormode(255)
color_list = [(2, 30, 9), (122, 41, 95), (72, 22, 32), (237, 72, 212), (220, 59, 81), (225, 100, 117), (93, 21, 1),
              (178, 170, 140), (150, 115, 92), (34, 26, 90), (7, 73, 154), (205, 91, 63), (168, 77, 129), (1, 147, 64),
              (4, 218, 221), (3, 28, 78), (220, 218, 178), (79, 179, 135), (124, 178, 154), (80, 138, 110),
              (121, 164, 185), (10, 221, 214), (121, 33, 13), (243, 7, 204), (133, 208, 222), (229, 165, 174)]
DISTANCE = 0

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
