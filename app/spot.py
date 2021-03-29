import pygame

from .colors import Colors


class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col

        self.x = row * width
        self.y = col * width

        self.color = Colors.WHITE

        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def __lt__(self, other):
        return False

    def get_pos(self):
        return self.row, self.col

    def is_open(self):
        return self.color == Colors.GREEN

    def is_closed(self):
        return self.color == Colors.RED

    def is_barrier(self):
        return self.color == Colors.BLACK

    def is_start(self):
        return self.color == Colors.ORANGE

    def is_end(self):
        return self.color == Colors.PURPLE

    def reset(self):
        self.color = Colors.WHITE

    def make_open(self):
        self.color = Colors.GREEN

    def make_closed(self):
        self.color = Colors.RED

    def make_barrier(self):
        self.color = Colors.BLACK

    def make_start(self):
        self.color = Colors.ORANGE

    def make_end(self):
        self.color = Colors.PURPLE

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

