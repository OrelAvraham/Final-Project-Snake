import pygame
from snake.game_constants import *

pygame.init()
REWARD_FONR = pygame.font.SysFont('calibri', 25)  # font to print the reward on board


def main():
    display = pygame.display.set_mode((SIZE * BLOCK_SIZE, SIZE * BLOCK_SIZE))
    pygame.display.set_caption('Snake')

    # TODO: add file explorer gui
    path = 'ai_shortcut_history/Game4.RAZ'
    with open(path, 'r') as f:
        lines = f.read().split('\n')
        snakes = eval(lines[0])
        # lengths = eval(lines[1])
        foods = eval(lines[1])
        rewards = eval(lines[2])
    turns = len(snakes)
    index = 0
    show_direction = False
    direction_block = None

    while True:
        # FIXME: after added the reward ot here it is anfry on me, maybe bcs of the reward printing on the board
        draw(display, snakes[index], foods[index], rewards[index], direction_block)
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

        if show_direction and index < turns - 1:
            direction_block = snakes[index + 1][-1]
        else:
            direction_block = None


def draw(display, snake, food, reward, direction_block):
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
            if direction_block:
                if [x, y] == direction_block:
                    pygame.draw.circle(display, RED, (x * 32 + 16, y * 32 + 16), 4)

            score_text = REWARD_FONR.render("Score: " + str(reward), True, BLACK)
            display.blit(score_text, [0, 0])
            pygame.display.flip()

    pygame.display.flip()


if __name__ == '__main__':
    main()
