import pygame

pygame.init()
# Direction Constants
UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)
STAY = (0, 0)

COMPASS_ROSE = [UP, RIGHT, DOWN, LEFT]

# Color Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

COLORS = [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN]

# Game Constants
STARTING_LENGTH = 3

# fps for clock ticking
SLOW_FPS = 10
NORMAL_FPS = 16
FAST_FPS = 32
SPEEEED_FPS = 64

EMPTY = 0
SNAKE = 1
HEAD = 2
FOOD = 3

BLOCK_SIZE = 32
SIZE = 16  # board size

GAME_CONSTS = [STARTING_LENGTH, SLOW_FPS, NORMAL_FPS, FAST_FPS, SPEEEED_FPS]
BLOCK_CONSTS = [EMPTY, SNAKE, HEAD, FOOD, BLOCK_SIZE, SIZE]

FONT = pygame.font.SysFont('calibri', 25)  # font to print the score on board

