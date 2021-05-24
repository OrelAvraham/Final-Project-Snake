import pygame

# TODO: arrange the code in here a bit

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

BLOCK_SIZE = 32
SIZE = 16
SPEED = 8

class SnakeGameViewer:
    def __init__(self, path='../snake/game_history/Game0.snake'):
        self.display = pygame.display.set_mode((SIZE * BLOCK_SIZE, SIZE * BLOCK_SIZE))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()

        with open(path, 'r') as f:
            lines = f.read().split('\n')
            self.snake_history = eval(lines[0])
            self.lengths = eval(lines[1])
            self.foods = eval(lines[2])

        # Fixme: maybe bcs the index is in the class in will not increase form the main
        self.index = 0
        self.update_snake()

    def update_snake(self):
        self.curr_snake = self.snake_history[self.index: self.index + self.lengths[self.index]]

    def get_amount_of_turns(self):
        return len(self.lengths)

    def draw(self):
        self.display.fill(BLACK)
        for x in range(SIZE):
            for y in range(SIZE):
                if [x, y] == self.curr_snake[-1]:
                    pygame.draw.rect(self.display, BLACK, pygame.Rect(x * 32, y * 32, 32, 32))
                    pygame.draw.rect(self.display, MAGENTA, pygame.Rect(x * 32 + 1, y * 32 + 1, 31, 31))
                    pygame.draw.rect(self.display, CYAN, pygame.Rect(x * 32 + 6, y * 32 + 6, 20, 20))
                elif [x, y] in self.curr_snake:
                    pygame.draw.rect(self.display, BLACK, pygame.Rect(x * 32, y * 32, 32, 32))
                    pygame.draw.rect(self.display, BLUE, pygame.Rect(x * 32 + 1, y * 32 + 1, 31, 31))
                    pygame.draw.rect(self.display, CYAN, pygame.Rect(x * 32 + 6, y * 32 + 6, 20, 20))
                elif [x, y] == self.foods[self.index]:
                    pygame.draw.rect(self.display, BLACK, pygame.Rect(x * 32, y * 32, 32, 32))
                    pygame.draw.rect(self.display, RED, pygame.Rect(x * 32 + 1, y * 32 + 1, 31, 31))
                    pygame.draw.rect(self.display, GREEN, pygame.Rect(x * 32 + 13, y * 32 + 13, 6, 6))
                else:
                    pygame.draw.rect(self.display, BLACK, pygame.Rect(x * 32, y * 32, 32, 32))
                    pygame.draw.rect(self.display, WHITE, pygame.Rect(x * 32 + 1, y * 32 + 1, 31, 31))

        pygame.display.flip()


def main():
    # FIXME: maybe no need in game viewer class. its not that practice and in theory not so needed as well
    game_viewer = SnakeGameViewer()
    turns = game_viewer.get_amount_of_turns()
    for i in range(turns):
        game_viewer.index = i
        game_viewer.draw()
        game_viewer.clock.tick(SPEED)
        game_viewer.update_snake()



if __name__ == '__main__':
    main()
