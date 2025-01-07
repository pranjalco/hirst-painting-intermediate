# Project 13: Hirst Painting

## Author
- **Name**: Pranjal Sarnaik
- **Date**: 2024-12-18

## Description
This project involves creating a Hirst painting using extracted colors from an image file (`image.jpg`). The program uses the `colorgram` library to extract 30 colors and then utilizes those colors to create a 10x10 grid of colorful dots resembling a Hirst painting. 

### Key Functionalities:
1. The `create_color_list.py` file extracts colors from the image and generates a list of RGB values. This list is manually copied and pasted into the `app.py` file for further use.
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

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/pranjalco/hirst-painting-intermediate.git
   ```
2. Navigate to the project directory:
   ```bash
   cd hirst-painting-intermediate
   ```
3. Install the required dependencies:
   ```bash
   pip install colorgram.py
   ```

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

---

**Created by Pranjal Sarnaik**  
*© 2024. All rights reserved.*
```

Let me know if you'd like to make further adjustments! 😊