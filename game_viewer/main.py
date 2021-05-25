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


def main():
    display = pygame.display.set_mode((SIZE * BLOCK_SIZE, SIZE * BLOCK_SIZE))
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()

    path = 'game_history/Game2.RAZ'
    with open(path, 'r') as f:
        lines = f.read().split('\n')
        snake_history = eval(lines[0])
        lengths = eval(lines[1])
        foods = eval(lines[2])

    turns = len(lengths)
    index = 0
    curr_snake = snake_history[index: index + lengths[index]]
    show_direction = False
    direction_block = None
    while True:
        draw(display, curr_snake, foods[index], direction_block)
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

        curr_snake = snake_history[index: index + lengths[index]]
        if show_direction and index < turns - 1:
            direction_block = snake_history[index + lengths[index]]
        else:
            direction_block = None


def draw(display, snake, food, direction_block):
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
                pygame.draw.rect(display, GREEN, pygame.Rect(x * 32 + 13, y * 32 + 13, 6, 6))
            else:
                pygame.draw.rect(display, BLACK, pygame.Rect(x * 32, y * 32, 32, 32))
                pygame.draw.rect(display, WHITE, pygame.Rect(x * 32 + 1, y * 32 + 1, 31, 31))
            if direction_block:
                if [x, y] == direction_block:
                    pygame.draw.circle(display, RED, (x * 32 + 16, y * 32 + 16), 4)

    pygame.display.flip()


if __name__ == '__main__':
    main()
