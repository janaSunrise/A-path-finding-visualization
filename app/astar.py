from queue import PriorityQueue

import pygame

from .utils import heuristic, reconstruct_path


def a_star_algorithm(draw, start, end):
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
