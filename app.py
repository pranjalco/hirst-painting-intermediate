import turtle
import random

"""
# Project 13: Hirst Painting

## Author
- **Name**: Pranjal Sarnaik
- **Date**: 2024-12-18

## Description
This project involves creating a Hirst painting using extracted colors from an image file (`image.jpg`). 
The program uses the `colorgram` library to extract 30 colors and then utilizes those colors to create a 10x10 
grid of colorful dots resembling a Hirst painting. 

### Key Functionalities:
1. The `create_color_list.py` file extracts colors from the image and generates a list of RGB values. This list 
is manually copied and pasted into the `app.py` file for further use.
2. The `app.py` file uses the `turtle` module to generate the Hirst painting based on the extracted colors.

## How to Use
1. Run `create_color_list.py` to generate the list of colors from `image.jpg`.
2. Copy the generated color list and paste it into the `app.py` file.
3. Run `app.py` to create the Hirst painting.

## Level
- **Level**: Intermediate
- **Skills**: Python programming, Turtle graphics, Color extraction using `colorgram`
- **Domain**: Creative Programming, GUI-based Projects

## Features
- Extracts colors from an image using the `colorgram` library.
- Creates a Hirst-style painting with 100 dots (10x10 grid) using the `turtle` and `random` modules.
- Three functions are used to build the painting:
  1. **`starting_point()`**: Fixes the starting position of the painting.
  2. **`draw_line()`**: Draws a straight line of 10 dots.
  3. **`turn_and_move()`**: Moves the turtle to the next row.

## Running the Program
1. Ensure Python 3.9 or later is installed on your system.
2. To generate the color list:
   - Run `create_color_list.py` using an IDE or terminal:
     ```bash
     python create_color_list.py
     ```
3. Copy the color list output from the console and paste it into the `app.py` file.
4. To create the Hirst painting:
   - Run `app.py` using an IDE or terminal:
     ```bash
     python app.py
     ```
5. View the final output image (`hirst_painting_final_output.PNG`) located in the `./screenshots` folder.

## Final Output
You can see the Hirst painting output in the file:
- **Path**: `./screenshots/hirst_painting_final_output.PNG`
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
