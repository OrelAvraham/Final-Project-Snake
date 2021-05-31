import pygame
from abc import ABC
import math
from snake.game_constants import *
import random
import numpy as np


class AbstractPlayer(ABC):
    # An abstract class that that represents a snake player
    def action(self, snake, direction, size, food):
        """
        A snake player action
        :param snake: a list represents the snakes body [tail, ..., head]
        :param direction: the current snakes direction, from the COMPASS_ROSE
        :param size: the size of the board
        :param food: the place of the food on the board
        :return: the direction the player decided the snake should move
        """
        ...

    def __str__(self):
        """
        A string function fot a player
        :return: the player's name, to distinguish between different players
        """
        ...


class HumanPlayer(AbstractPlayer):
    # A kind of player controlled by a human player with the arrow keys
    # the keys directions are absolute - relative to the board and not the snake
    def action(self, snake, direction, size, food):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    return LEFT
                elif event.key == pygame.K_RIGHT:
                    return RIGHT
                elif event.key == pygame.K_UP:
                    return UP
                elif event.key == pygame.K_DOWN:
                    return DOWN

        return STAY

    def __str__(self):
        return 'human_player'


class RandomPlayerAI(AbstractPlayer):
    # A kind of player controlled by software
    # takes random moves
    def action(self, snake, direction, size, food):
        return random.choice(COMPASS_ROSE)

    def __str__(self):
        return 'ai_random'


class ShortcutPlayerAI(AbstractPlayer):
    # A kind of player controlled by the software
    # that goes to an available spot that is the closest to the apple (not very smart)
    def action(self, snake, direction, size, food):
        head = snake[-1]

        # Find the 3 possible directions
        curr_direction_index = COMPASS_ROSE.index(direction)
        left = COMPASS_ROSE[(curr_direction_index - 1) % 4]
        straight = direction
        right = COMPASS_ROSE[(curr_direction_index + 1) % 4]
        directions = []

        # Calculate the points of those directions
        left_point = [a + b for a, b in zip(head, left)]
        straight_point = [a + b for a, b in zip(head, straight)]
        right_point = [a + b for a, b in zip(head, right)]
        points = []

        # save the noes ones on the snake

        def _valid_point(p):
            return 0 <= p[0] < size and 0 <= p[1] < size and p not in snake

        if _valid_point(left_point):
            directions.append(left)
            points.append(left_point)

        if _valid_point(straight_point):
            directions.append(straight)
            points.append(straight_point)

        if _valid_point(right_point):
            directions.append(right)
            points.append(right_point)

        dists = []
        for point in points:
            dists.append(math.dist(point, food))

        # find the one which is closest to the apple
        if len(dists) == 0:
            return STAY

        min_dist = min(dists)

        return directions[dists.index(min_dist)]

    def __str__(self):
        return 'ai_shortcut'


class Hamilton(AbstractPlayer):
    # FIXME: "something is wrong i can feel it"/ Eminem, for some reason the path is empty
    def __init__(self):  # TODO: maybe calc the path in the init' think how implement this in main
        self.path = []
        self.idx = 0

    def action(self, snake, direction, size, food):
        self.path = []
        if not self.path:
            start = snake[-1]
            dest = snake[-2]

            np_board = np.zeros((size, size))
            board = []
            for e in np_board:
                board.append(list(e))

            for node in snake:
                x,y = node
                board[x][y] = 1

            path = []
            self.path = self._hamiltonian_path(start, dest, board, path, size)
            print(path)

        p1 = path[self.idx]
        p2 = path[(self.idx + 1) % len(path)]

        direction = [a - b for a, b in zip(p2, p1)]

        return tuple(direction)

    def _hamiltonian_path(self, start, dest, board, path, size):
        # calculate all points around the starting point
        up = [a + b for a, b in zip(start, UP)]
        right = [a + b for a, b in zip(start, RIGHT)]
        down = [a + b for a, b in zip(start, DOWN)]
        left = [a + b for a, b in zip(start, LEFT)]

        optional_points = [up, right, down, left]  # list of all optional points
        points = []  # list of all valid points

        # appending only valid points to the points list
        for optional_point in optional_points:
            if self._valid_point(optional_point, board, size):
                points.append(optional_point)

        if len(points) == 0:
            return False
        print('OOF')

        for point in points:
            path.append(point)
            x, y = point
            board[x][y] = 1
            if point == dest:
                path.append(dest)
                return path

            new_path = self._hamiltonian_path(point, dest, board, path, size)

            if new_path:  # new_path != False
                return new_path

            popped_point = path.pop()
            x_, y_ = popped_point
            print(x_, y_)
            board[x_][y_] = 0

    def _valid_point(self, point, board, size):
        x, y = point
        return 0 <= x < size and 0 <= y < size and board[x][y] == 0

    def __str__(self):
        return 'ai_hamilton'
