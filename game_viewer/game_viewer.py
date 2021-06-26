from snake.game_constants import *
import os
pygame.init()


def main(display=pygame.display.set_mode((SIZE * BLOCK_SIZE, SIZE * BLOCK_SIZE)), player_name=None, game_number=None):
    """
    Min function for running
    :param display: the display to view the game in
    :param player_name: the name of the player we want to watch his game,
                        the players name is part of it history directory name
    :param game_number: the number of game to watch
    :return: None
    """
    pygame.display.set_caption('game_viewer')

    if player_name == None or game_number == None: # if one of the file parts is None ask again for them (both)
        player_name = input('Enter agent name to view ')
        game_number = input('Enter game number of the selected agent ')

    # Creating the path itself
    path = os.path.join(os.path.dirname(__file__), f'{player_name}_history/Game{game_number}.RAZ')

    # Making sure the path exists
    while not os.path.exists(path):
        player_name = input('Enter agent name to view ')
        game_number = input('Enter game number of the selected agent ')
        path = os.path.join(os.path.dirname(__file__), f'{player_name}_history/Game{game_number}.RAZ')

    # Reading the file
    with open(path, 'r') as f:
        lines = f.read().split('\n')
        snakes = eval(lines[0])
        # lengths = eval(lines[1])
        foods = eval(lines[1])
    turns = len(snakes)  # calculating the amount of turns (= the length of snakes = the length of foods)
    index = 0  # initializing the index of the current turn to 0

    # Showing the direction - feature
    show_direction = False # starting with the feature off
    direction_block = None  # initializing the direction block to None

    # Showing the path - feature
    show_path = False # starting with the feature off
    path = []  # initializing the path to an empty list

    run = True
    # The main loop that runs the viewing
    while run:
        draw(display, snakes[index], foods[index], direction_block, path)  # draw the board

        for event in pygame.event.get():  # check for events
            if event.type == pygame.QUIT:  # check for quit
                    pygame.quit()
                    quit()
            elif event.type == pygame.KEYDOWN:  # check for key pressing (user input)
                if event.key == pygame.K_q:  # q -> stopping the viewing
                    run = False
                elif event.key == pygame.K_RIGHT:  # right arrow -> go to next turn
                    index += 1
                    index %= turns
                elif event.key == pygame.K_LEFT:  # left arrow -> go to previous turn
                    index -= 1
                    index %= turns
                elif event.key == pygame.K_SPACE:  # space -> show snake's direction
                    show_direction = not show_direction
                elif event.key == pygame.K_UP:  # up arrow -> show\reset path
                    if show_path:
                        path = []
                    show_path = True
                elif event.key == pygame.K_DOWN:  # down arrow -> hide path
                    show_path = False

        # Updating the path
        if show_path:
            path.append(snakes[index][-1])
        else:
            path = []

        # Updating the direction block
        if show_direction and index < turns - 1:
            direction_block = snakes[index + 1][-1]
        else:
            direction_block = None


def draw(display, snake, food, direction_block, path):
    """
    Drawing the game board
    :param display: the display to draw on
    :param snake: the snake's body
    :param food: the foods coordinates
    :param direction_block: the direction block
    :param path: the path to draw
    :return: None
    """

    # filling the dis[lay
    display.fill(BLACK)
    bs = BLOCK_SIZE  # saving the block size in a shorter var name

    # looping over all the board
    for x in range(SIZE):
        for y in range(SIZE):
            if [x, y] == snake[-1]:  # if block in head draw head block
                pygame.draw.rect(display, HEAD_COLOR, pygame.Rect(x * bs + bs*(1/32), y * bs + bs*(1/32), bs - bs*(1/32), bs - bs*(1/32)))
            elif [x, y] in snake:  # else if block in snake draw snake block
                pygame.draw.rect(display, SNAKE_COLOR, pygame.Rect(x * bs + bs*(1/32), y * bs + bs*(1/32), bs - bs*(1/32), bs - bs*(1/32)))
            elif [x, y] == food:  # else if block is food draw food block
                pygame.draw.rect(display, RED, pygame.Rect(x * bs + bs*(1/32), y * bs + bs*(1/32), bs - bs*(1/32), bs - bs*(1/32)))
            if [x, y] in path:  # if block in path draw a dot for path
                pygame.draw.circle(display, PATH_COLOR, (x * bs + bs/2, y * bs + bs/2), bs/8)
            if direction_block:  # if block is direction block it
                if [x, y] == direction_block:
                    pygame.draw.circle(display, DIRECTION_COLOR, (x * bs + bs/2, y * bs + bs/2), bs/8)

    # Write the score on the display
    score_text = FONT.render("Score: " + str(len(snake) - 3), True, WHITE)
    display.blit(score_text, [0, 0])
    pygame.display.flip()  # flip the display from the graphics card to the screen


if __name__ == '__main__':
    main()
