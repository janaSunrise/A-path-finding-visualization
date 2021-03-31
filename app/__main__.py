from tkinter import messagebox, Tk

import pygame

from .utils import algorithm, draw, get_clicked_pos, make_grid

SIDE = 800  # The side of the GUI, Keeping it to be a square.
WINDOW = pygame.display.set_mode((SIDE, SIDE))

pygame.display.set_caption("A-star Path finding visualization")


def main(window, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start, end = None, None
    run = True

    while run:
        draw(window, grid, ROWS, SIDE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]

                if not start:
                    start = spot
                    start.make_start()
                elif not end:
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()

                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    res = algorithm(lambda: draw(window, grid, ROWS, width), grid, start, end)

                    if not res:
                        Tk().wm_withdraw()
                        messagebox.showinfo("No Solution", "There was no solution")

    pygame.quit()


if __name__ == '__main__':
    main(WINDOW, SIDE)
