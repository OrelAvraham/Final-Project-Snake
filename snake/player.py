import pygame
from abc import ABC
import math

# Direction constants
UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)
STAY = (0, 0)

COMPASS_ROSE = [UP, RIGHT, DOWN, LEFT]


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


class HumanPlayer(AbstractPlayer):
    # A kind of player controlled by a human player with the arrow keys
    # the keys directions are absolut to the
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


class ShortcutPlayerAI(AbstractPlayer):
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

