import random
import numpy as np

from snake.game_constants import *

pygame.init()


class Game:
    def __init__(self, display, size=SIZE, fps=NORMAL_FPS):
        # Technical settings
        self.size = size
        self.display = display
        pygame.display.set_caption('snake')
        self.clock = pygame.time.Clock()
        self.fps = fps

        # Game Settings
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.head = [random.choice([self.size // 2, self.size // 2 - 1]),
                     random.choice([self.size // 2, self.size // 2 - 1])]
        self.snake = [self.head]
        for i in range(1, STARTING_LENGTH):
            shift_from_head = [e * i for e in self.direction]
            new_node = [a - b for a, b in zip(self.head, shift_from_head)]
            self.snake.insert(0, new_node)

        self.food = None
        self._place_food()

        self.score = 0

    def game_state(self):
        return self._check_collision(), self.score, self.snake.copy(), self.direction, self.food

    def play_game_step(self, action):
        self._update_ui()
        new_direction = action

        if new_direction != STAY:
            if abs(COMPASS_ROSE.index(self.direction) - COMPASS_ROSE.index(new_direction)) != 2:
                self.direction = new_direction

        self._move_snake()
        self.clock.tick(self.fps)
        game_over = self._check_collision()

        return self.game_state()

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
                    pygame.draw.rect(self.display, GREEN, pygame.Rect(x * 32 + 11, y * 32 + 11, 10, 10))
                else:
                    pygame.draw.rect(self.display, BLACK, pygame.Rect(x * 32, y * 32, 32, 32))
                    pygame.draw.rect(self.display, WHITE, pygame.Rect(x * 32 + 1, y * 32 + 1, 31, 31))
        score_text = FONT.render("Score: " + str(self.score), True, BLACK)
        self.display.blit(score_text, [0, 0])
        pygame.display.flip()

    def _move_snake(self):  # returns if the snake have eaten
        self.head = [a + b for a, b in zip(self.head, self.direction)]
        self.snake.append(self.head)

        if self.head == self.food:
            self.score += 1
            self._place_food()
            return True

        self.snake.pop(0)
        return False

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
