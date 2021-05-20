import pygame
from abc import ABC

# Direction constants
UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)
STAY = (0, 0)


class AbstractPlayer(ABC):
    def action(self):
        ...


class HumanPlayer(AbstractPlayer):
    def action(self):
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