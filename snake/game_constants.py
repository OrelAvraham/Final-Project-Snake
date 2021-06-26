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

HEAD_COLOR = BLUE
SNAKE_COLOR = BLUE
FOOD_COLOR = RED

EMPTY_BLOCK_COLOR = BLACK
PATH_COLOR = WHITE
DIRECTION_COLOR = GREEN

COLORS = [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN]

# Game constants
STARTING_LENGTH = 3
GAME_CONSTS = [STARTING_LENGTH]

# FPS for clock ticking
SLOW_FPS = 10
NORMAL_FPS = 16
FAST_FPS = 32
SPEEEED_FPS = 64

FPS = [SLOW_FPS, NORMAL_FPS, FAST_FPS, SPEEEED_FPS]

# Block information
EMPTY = 0
SNAKE = 1
HEAD = 2
FOOD = 3

BLOCK_SIZE = 32
SIZE = 16  # board size

BLOCK_CONSTS = [EMPTY, SNAKE, HEAD, FOOD, BLOCK_SIZE, SIZE]

# Font
FONT = pygame.font.SysFont('calibri', 25)  # font to print the score on board

# Paths
prefix_path = r'C:/Users/orlav/PycharmProjects/Final-Project-Snake'

# Sounds
FOOD_SOUND = pygame.mixer.Sound(prefix_path + r'/images/food.mp3')
DEATH_SOUND = pygame.mixer.Sound(prefix_path + r'/images/food.mp3')
