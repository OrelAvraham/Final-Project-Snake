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
FRAME_RATE = 64  # for the pygame.Clock ticks
EMPTY = 0
SNAKE = 1
HEAD = 2
FOOD = 3

# FIXME: they need to be swapped
BLOCK_SIZE = 32
SIZE = 16  # board size

GAME_CONSTS = [STARTING_LENGTH, FRAME_RATE]
BLOCK_CONSTS = [EMPTY, SNAKE, HEAD, FOOD, BLOCK_SIZE, SIZE]

