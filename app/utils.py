import pygame

from .colors import Colors
from .spot import Spot


def heuristic(point_1, point_2):
    x_1, y_1 = point_1
    x_2, y_2 = point_2
    
    return abs(x_1 - x_2) + abs(y_1 - y_2)


def make_grid(rows, width):
    gap = width // rows

    grid = [[Spot(i, j, gap, rows) for j in range(rows)] for i in range(rows)]
    return grid


def draw_grid(window, rows, width):
    gap = width // rows

    for i in range(rows):
        pygame.draw.line(window, Colors.GREY, (0, i*gap), (width, i*gap))

        for j in range(rows):
            pygame.draw.line(window, Colors.GREY, (j * gap, 0), (j * gap, width))


def draw(window, grid, rows, width):
    window.fill(Colors.WHITE)

    for row in grid:
        for spot in row:
            spot.draw(window)

    draw_grid(window, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def reconstruct_path(current, draw):
    while current.came_from:
        current = current.came_from
        current.make_path()
        draw()
