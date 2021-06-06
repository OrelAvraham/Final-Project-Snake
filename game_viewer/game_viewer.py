import pygame
from znake.game_constants import *
import keyboard

pygame.init()
SCORE_FONT = pygame.font.SysFont('calibri', 25)  # font to print the score on board

def main():
    display = pygame.display.set_mode((SIZE * BLOCK_SIZE, SIZE * BLOCK_SIZE))
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()
    # TODO: add file explorer gui
    path = 'ai_bfs_history/Game0.RAZ'
    with open(path, 'r') as f:
        lines = f.read().split('\n')
        snakes = eval(lines[0])
        # lengths = eval(lines[1])
        foods = eval(lines[1])
    turns = len(snakes)
    index = 0
    show_direction = False
    direction_block = None
    show_path = False
    path = []

    while True:
        # FIXME: after added the reward ot here it is anfry on me, maybe bcs of the reward printing on the board
        draw(display, snakes[index], foods[index], direction_block, path)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_RIGHT:
                    if index < turns - 1:
                        index += 1
                elif event.key == pygame.K_LEFT:
                    if index > 0:
                        index -= 1
                elif event.key == pygame.K_SPACE:
                    show_direction = not show_direction
                elif event.key == pygame.K_UP:
                    if show_path:
                        path = []
                    show_path = True
                elif event.key == pygame.K_DOWN:
                    show_path = False
        if show_path:
            path.append(snakes[index][-1])
        else:
            path = []
        if show_direction and index < turns - 1:
            direction_block = snakes[index + 1][-1]
        else:
            direction_block = None


def draw(display, snake, food, direction_block, path):
    display.fill(BLACK)
    for x in range(SIZE):
        for y in range(SIZE):
            if [x, y] == snake[-1]:
                pygame.draw.rect(display, BLACK, pygame.Rect(x * 32, y * 32, 32, 32))
                pygame.draw.rect(display, MAGENTA, pygame.Rect(x * 32 + 1, y * 32 + 1, 31, 31))
                pygame.draw.rect(display, CYAN, pygame.Rect(x * 32 + 6, y * 32 + 6, 20, 20))
            elif [x, y] in snake:
                pygame.draw.rect(display, BLACK, pygame.Rect(x * 32, y * 32, 32, 32))
                pygame.draw.rect(display, BLUE, pygame.Rect(x * 32 + 1, y * 32 + 1, 31, 31))
                pygame.draw.rect(display, CYAN, pygame.Rect(x * 32 + 6, y * 32 + 6, 20, 20))
            elif [x, y] == food:
                pygame.draw.rect(display, BLACK, pygame.Rect(x * 32, y * 32, 32, 32))
                pygame.draw.rect(display, RED, pygame.Rect(x * 32 + 1, y * 32 + 1, 31, 31))
                pygame.draw.rect(display, GREEN, pygame.Rect(x * 32 + 11, y * 32 + 11, 10, 10))
            else:
                pygame.draw.rect(display, BLACK, pygame.Rect(x * 32, y * 32, 32, 32))
                pygame.draw.rect(display, WHITE, pygame.Rect(x * 32 + 1, y * 32 + 1, 31, 31))
            if [x, y] in path:
                pygame.draw.circle(display, BLACK, (x * 32 + 16, y * 32 + 16), 4)
            if direction_block:
                if [x, y] == direction_block:
                    pygame.draw.circle(display, RED, (x * 32 + 16, y * 32 + 16), 4)

    score_text = SCORE_FONT.render("Score: " + str(len(snake) - 3), True, BLACK)
    display.blit(score_text, [0, 0])
    pygame.display.flip()
    pygame.display.flip()


if __name__ == '__main__':
    main()