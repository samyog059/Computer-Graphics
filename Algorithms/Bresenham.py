# Bresenham's Line Drawing Algorithm in Python
# Uses graphics.py library (install using: pip install graphics.py)

from graphics import *

def bresenham_line(x1, y1, x2, y2):
    win = GraphWin("Bresenham Line Drawing Algorithm", 500, 500)
    win.setBackground("white")

    # Calculate dx and dy
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Determine in which direction to step
    sx = 1 if x2 > x1 else -1   # step for x
    sy = 1 if y2 > y1 else -1   # step for y

    # Decision parameter
    p = 2 * dy - dx

    x = x1
    y = y1

    # Plot the first point
    Circle(Point(x, y), 1).draw(win)

    # Loop for each step in x-direction (dx times)
    for _ in range(dx):
        # If p < 0, choose East pixel → x increases
        if p < 0:
            p = p + 2 * dy
        else:
            # If p >= 0, choose North-East pixel → x & y increase
            p = p + 2 * (dy - dx)
            y = y + sy

        x = x + sx

        # Draw the pixel
        pixel = Circle(Point(x, y), 1)
        pixel.setFill("black")
        pixel.draw(win)

    win.getMouse()  # wait for click
    win.close()

# Example: draw a line
bresenham_line(30, 40, 460, 300)
