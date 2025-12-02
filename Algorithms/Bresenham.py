import pygame
import sys

def bresenham_line(screen, x1, y1, x2, y2):
    # Colors
    BLACK = (0, 0, 0)

    # Calculate dx & dy
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Direction of steps
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    p = 2 * dy - dx  # decision parameter

    x = x1
    y = y1

    # Plot the first point
    pygame.draw.rect(screen, BLACK, (x, y, 2, 2))

    # Draw pixels along x
    for _ in range(dx):
        if p < 0:
            p = p + 2 * dy
        else:
            p = p + 2 * (dy - dx)
            y = y + sy

        x = x + sx

        # Draw the pixel
        pygame.draw.rect(screen, BLACK, (x, y, 2, 2))


def main():
    pygame.init()

    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Bresenham Line Drawing Algorithm")

    screen.fill((255, 255, 255))  # white background

    # Example line
    bresenham_line(screen, 30, 40, 460, 300)

    pygame.display.update()

    # Wait until window closed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
