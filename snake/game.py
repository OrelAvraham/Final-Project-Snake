import random
import numpy as np
import os
from snake.game_constants import *
from pygame import  mixer

class Game:
    def __init__(self, display=pygame.display.set_mode((SIZE * BLOCK_SIZE, SIZE * BLOCK_SIZE)), size=SIZE,
                 fps=NORMAL_FPS):
        """
        Constructor for the game, initializes the game's variables and prepares it to be played
        :param display: a pygame display for the game to be played on
        :param size:the size of the game board, automatically sets to SIZE - I recommend no t o change it
        :param fps: the fps of the game - used in the game clocks ticks
        """
        # Technical initializations
        self.size = size  # board size, shoud be changes from the game constants file
        self.display = display  # game display
        pygame.display.set_caption('snake')
        self.clock = pygame.time.Clock()  # game clock
        self.fps = fps

        # Game related initializations
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])  # choosing random starting direction
        self.head = [random.choice([self.size // 2, self.size // 2 - 1]),
                     random.choice([self.size // 2, self.size // 2 - 1])]  # choosing random head position

        # generating the snake according to the starting head and direction
        self.snake = [self.head]
        for i in range(1, STARTING_LENGTH):
            shift_from_head = [e * i for e in self.direction]
            new_node = [a - b for a, b in zip(self.head, shift_from_head)]
            self.snake.insert(0, new_node)

        # spawning food
        self.food = None
        self._place_food()

        self.score = 0  # initiating the score to zero

    def game_state(self):
        """
        :return: the current game state - useful information for the agents
                    if the game ended, the current score, copy of the snake, the direction and the food
        """
        return self._check_collision(), self.score, self.snake.copy(), self.direction, self.food.copy()

    def play_game_step(self, action):
        """
        :param action: an action to perform on the snake, has to be in [UP, RIGHT, DOWN, LEFT, STAY]
        :return: the current game state (self.game_state())
        """
        self._update_ui()  # updating the graphics

        if action != STAY:  # If the action is STAY we want to keep the last direction
            # avoiding from moving 180 degrees, if snake do goes there we want to stay
            if abs(COMPASS_ROSE.index(self.direction) - COMPASS_ROSE.index(action)) != 2:
                self.direction = action

        self._move_snake()  # moving the snake
        self.clock.tick(self.fps)  # ticking

        return self.game_state()  # returning game state

    # Helper functions

    def _update_ui(self):
        """
        draws the game
        :return: None
        """
        self.display.fill(BLACK)
        bs = BLOCK_SIZE
        for x in range(self.size):
            for y in range(self.size):
                if [x, y] == self.head:  # draw the head
                    pygame.draw.rect(self.display, HEAD_COLOR,
                                     pygame.Rect(x * bs + bs * (1 / 32), y * bs + bs * (1 / 32), bs - bs * (1 / 32),
                                                 bs - bs * (1 / 32)))
                elif [x, y] in self.snake:  # draw the body
                    pygame.draw.rect(self.display, SNAKE_COLOR,
                                     pygame.Rect(x * bs + bs * (1 / 32), y * bs + bs * (1 / 32), bs - bs * (1 / 32),
                                                 bs - bs * (1 / 32)))
                elif [x, y] == self.food:  # draw the food
                    pygame.draw.rect(self.display, FOOD_COLOR,
                                     pygame.Rect(x * bs + bs * (1 / 32), y * bs + bs * (1 / 32), bs - bs * (1 / 32),
                                                 bs - bs * (1 / 32)))

        # drawing the score on the board
        score_text = FONT.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(score_text, [0, 0])
        pygame.display.flip()

    def _move_snake(self):  # returns if the snake have eaten
        """
        moves the snake in the current direction
        :return: if snake have eaten
        """
        self.head = [a + b for a, b in zip(self.head, self.direction)]
        self.snake.append(self.head)

        if self.head == self.food:
            self.score += 1
            self._place_food()
            mixer.Sound.play(FOOD_SOUND)
            return True

        self.snake.pop(0)
        return False

    def _place_food(self):
        """
        places random food, use only when food has eaten - therefore private
        :return: None
        """
        x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
        while [x, y] in self.snake:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)

        self.food = [x, y]

    def _check_collision(self):
        """
        checks for collisions
        :return: if snake is dead
        """
        x, y = self.head
        return (not (0 <= x < self.size and 0 <= y < self.size)) or (list((x, y)) in self.snake[:-1])

    # Strings

    def __repr__(self):
        """
        representation function for the game board
        :return: the representation
        """
        board = [[0 for _ in range(self.size)] for __ in range(self.size)]
        for node in self.snake:
            board[node[1]][node[0]] = SNAKE

        board[self.food[1]][self.food[0]] = FOOD
        board[self.head[1]][self.head[0]] = HEAD
        return str(np.matrix(board))

    def __str__(self):
        """
        string functions for useful information about the game
        :return: the string
        """
        s_snake = f'SNAKE {self.snake}\n'
        s_food = f'FOOD {self.food}\n'
        s_dir = f'DIRECTOIN {self.direction}\n'
        return s_snake + s_food + s_dir
