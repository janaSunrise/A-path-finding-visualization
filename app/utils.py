from queue import PriorityQueue

import pygame

from .colors import Colors
from .spot import Spot


def calculate_distance(point_1, point_2):
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


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))

    came_from = {}

    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0

    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = calculate_distance(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + calculate_distance(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False
