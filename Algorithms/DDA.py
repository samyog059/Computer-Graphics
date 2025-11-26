# DDA Line Drawing Algorithm in Python

# Importing the graphics library
# You may need to install it using: pip install graphics.py
from graphics import *

def dda_line(x1, y1, x2, y2):
    # Create a window to display output
    win = GraphWin("DDA Line Drawing Algorithm", 500, 500)
    win.setBackground("white")

    # Calculate dx and dy (difference in x and y)
    dx = x2 - x1
    dy = y2 - y1

    # Find how many steps are needed
    # We take the larger of dx or dy for smoothness
    steps = int(max(abs(dx), abs(dy)))

    # Calculate the increment for each step
    x_inc = dx / steps
    y_inc = dy / steps

    # Starting point
    x = x1
    y = y1

    # Draw pixels for each step
    for i in range(steps):
        # Draw a small circle to represent a pixel
        pixel = Circle(Point(x, y), 1)
        pixel.setFill("black")
        pixel.draw(win)

        # Move to the next pixel
        x += x_inc
        y += y_inc

    win.getMouse()  # Wait for a mouse click to close
    win.close()

# Example: draw a line from (50, 60) to (400, 350)
dda_line(50, 60, 400, 350)
