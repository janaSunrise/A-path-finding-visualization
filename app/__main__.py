import math
from queue import PriorityQueue

import pygame

SIDE = 800  # The side of the GUI
WINDOW = pygame.display.set_mode((SIDE, SIDE))

pygame.display.set_caption("A-star Path finding visualization")
