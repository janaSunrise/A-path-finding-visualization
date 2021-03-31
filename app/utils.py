from queue import PriorityQueue

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


def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))

    start.g_score = 0
    start.g_score = heuristic(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = current.g_score + 1

            if temp_g_score < neighbor.g_score:
                neighbor.came_from = current

                neighbor.g_score = temp_g_score
                neighbor.f_score = temp_g_score + heuristic(neighbor.get_pos(), end.get_pos())

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((neighbor.f_score, count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()
        if current != start:
            current.make_closed()

    return False
