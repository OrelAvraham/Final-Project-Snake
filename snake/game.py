import pygame
import random
import numpy as np
from snake.player import AbstractPlayer, ShortcutPlayerAI, HumanPlayer

pygame.init()
SCORE_FONT = pygame.font.SysFont('calibri', 25)

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

# Game Constants
STARTING_LENGTH = 3
EMPTY = 0
SNAKE = 1
HEAD = 2
FOOD = 3
BLOCK_SIZE = 32
FRAME_RATE = 8  # for the pygame.Clock ticks


class Game():
    def __init__(self, size=16):
        # Technical settings
        self.size = size
        self.display = pygame.display.set_mode((size * BLOCK_SIZE, size * BLOCK_SIZE))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()

        # Game Settings
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.head = [random.randint(self.size // 4, 3 * self.size // 4),
                     random.randint(self.size // 4, 3 * self.size // 4)]
        self.snake = [self.head]
        for i in range(1, STARTING_LENGTH):
            shift_from_head = [e * i for e in self.direction]
            new_node = [a - b for a, b in zip(self.head, shift_from_head)]
            self.snake.insert(0, new_node)

        self.food = None
        self._place_food()

        self.score = 0
        self.iteration = 0

    def play_game_step(self, player: AbstractPlayer):
        self.iteration += 1
        self._update_ui()
        new_direction = player.action(self.snake, self.direction, self.size, self.food)

        if new_direction != STAY:
            if abs(COMPASS_ROSE.index(self.direction) - COMPASS_ROSE.index(new_direction)) != 2:
                self.direction = new_direction
        self._move_snake()
        self.clock.tick(FRAME_RATE)
        game_over = self._check_collision()

        return self.iteration, game_over, self.score, self.snake.copy(), self.food

    # Helper functions

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
                    # TODO: maybe try add eyes to the snakes head
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
        score_text = SCORE_FONT.render("Score: " + str(self.score), True, BLACK)
        self.display.blit(score_text, [0, 0])
        pygame.display.flip()

    def _move_snake(self):
        self.head = [a + b for a, b in zip(self.head, self.direction)]
        self.snake.append(self.head)
        if self.head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.pop(0)

    def _check_collision(self):
        x, y = self.head
        return (not (0 <= x < self.size and 0 <= y < self.size)) or (list((x, y)) in self.snake[:-1])

    # Strings

    def _str_board(self):
        board = [[0 for _ in range(self.size)] for __ in range(self.size)]
        for node in self.snake:
            board[node[1]][node[0]] = SNAKE

        board[self.food[1]][self.food[0]] = FOOD
        board[self.head[1]][self.head[0]] = HEAD
        return str(np.matrix(board))

    def __str__(self):
        s_snake = f'SNAKE {self.snake}\n'
        s_food = f'FOOD {self.food}\n'
        s_board = f'BOARD:\n{self._str_board()}'
        return s_snake + s_food + s_board

