import pygame
import random
import numpy as np

pygame.init()
SCORE_FONT = pygame.font.SysFont('calibri', 25)

# Direction Constants
UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)

# Color Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

# Game Constants
STARTING_LENGTH = 3
EMPTY = 0
SNAKE = 1
HEAD = 2
FOOD = 3
BLOCK_SIZE = 32
SPEED = 20  # for the pygame.Clock ticks


class Game():
    def __init__(self, size=16):
        # Technical settings
        self.size = size
        self.display = pygame.display.set_mode((size * BLOCK_SIZE, size * BLOCK_SIZE))
        pygame.display.set_caption('Snake')
        self.cloc = pygame.time.Clock()

        # TODO: add recording mechanism - records the lengths instead of deleting nodes
        # self._lengths = [STARTING_LENGTH]
        # self.record = record

        # Game Settings
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

        if self.direction == UP:
            print('UP')
        elif self.direction == DOWN:
            print('DOWN')
        elif self.direction == LEFT:
            print('LEFT')
        elif self.direction == RIGHT:
            print('RIGHT')

        self.head = [random.randint(2, self.size - 3), random.randint(2, self.size - 3)]
        self.snake = [self.head]
        for i in range(1, STARTING_LENGTH):
            shift_from_head = [e * i for e in self.direction]
            new_node = [a - b for a, b in zip(self.head, shift_from_head)]
            self.snake.insert(0, new_node)

        self.food = None
        self._place_food()

        self.score = 0
        self.iteration = 0  # to keep count on the number of game iterations:
        # to kill the if it haven't ate for a long time

    def play_game_step(self):
        self._update_ui()

    # Helper functions
    def str_board(self):
        board = [[0 for _ in range(self.size)] for __ in range(self.size)]
        for node in self.snake:
            board[node[1]][node[0]] = SNAKE

        board[self.food[1]][self.food[0]] = FOOD
        board[self.head[1]][self.head[0]] = HEAD
        return str(np.matrix(board))

    def _place_food(self):
        x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
        while [x, y] in self.snake:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)

        self.food = [x, y]

    def _update_ui(self):
        self.display.fill(BLACK)
        for x in range(self.size):
            for y in range(self.size):
                if [x, y] == self.head:
                    # TODO: mayeb add eyes to snake
                    pygame.draw.rect(self.display, BLACK, pygame.Rect(x * 32, y * 32, 32, 32))
                    pygame.draw.rect(self.display, MAGENTA, pygame.Rect(x * 32 + 1, y * 32 + 1, 31, 31))
                    pygame.draw.rect(self.display, CYAN, pygame.Rect(x * 32 + 6, y * 32 + 6, 20, 20))
                elif [x, y] in self.snake:
                    pygame.draw.rect(self.display, BLACK, pygame.Rect(x * 32, y * 32, 32, 32))
                    pygame.draw.rect(self.display, BLUE, pygame.Rect(x * 32 + 1, y * 32 + 1, 31, 31))
                    pygame.draw.rect(self.display, CYAN, pygame.Rect(x * 32 + 6, y * 32 + 6, 20, 20))
                elif [x, y] == self.food:
                    pygame.draw.rect(self.display, BLACK, pygame.Rect(x * 32, y * 32, 32, 32))
                    pygame.draw.rect(self.display, RED, pygame.Rect(x * 32 + 1, y * 32 + 1, 31, 31))
                    pygame.draw.rect(self.display, GREEN, pygame.Rect(x * 32 + 13, y * 32 + 13, 6, 6))
                else:
                    pygame.draw.rect(self.display, BLACK, pygame.Rect(x * 32, y * 32, 32, 32))
                    pygame.draw.rect(self.display, WHITE, pygame.Rect(x * 32 + 1, y * 32 + 1, 31, 31))

        score_text = SCORE_FONT.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(score_text, [0, 0])
        pygame.display.flip()

    def __str__(self):
        s_snake = f'SNAKE {self.snake}\n'
        s_food = f'FOOD {self.food}\n'
        s_board = f'BOARD:\n{self.str_board()}'
        return s_snake + s_food + s_board


if __name__ == '__main__':
    snake: Game = Game()
    print(snake)
    while 1:
        snake.play_game_step()
