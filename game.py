import pygame
import random

# Direction Constants
UP = (0, 1)
RIGHT = (1, 0)
DOWN = (0, -1)
LEFT = (-1, 0)

# Color Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
REG = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

# Game Constants
STARTING_LENGTH = 3
BLOCK_SIZE = 32
SPEED = 20  # for the pygame.Clock ticks


class Game():
    def __init__(self, size):
        # Technical settings
        self.size = size
        self.display = pygame.display.set_mode((size, size))
        pygame.display.set_caption('Snake')
        self.cloc = pygame.time.Clock()
        # self._lengths = [STARTING_LENGTH] TODO: add recording mechanism -
        #                                         records the lengths instead of deleting nodes

        # Game Settings
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.head = [random.randint(0, self.size - 1), random.randint(0, self.size - 1)]
        self.snake = [self.head]
        for i in range(1, STARTING_LENGTH):
            shift_from_head = [e * i for e in self.direction]
            new_node = [a + b for a, b in zip(self.head, shift_from_head)]
            self.snake.insert(0, new_node)

        self.food = None
        self._place_food()

        self.score = 0
        self.iteration = 0  # to keep count on the number of game iterations:
        #                     to kill the if it haven't ate for a long time

    # Helper functions

    def _place_food(self):
        x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
        while [x, y] in self.snake:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)

        self.food = [x, y]
