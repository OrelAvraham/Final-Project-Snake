from snake.game import Game
from snake.players import *
from game_viewer.recorder import Recorder


def main(wanted_player: AbstractPlayer = None, display=pygame.display.set_mode((SIZE * BLOCK_SIZE, SIZE * BLOCK_SIZE))):
    """
    A main code that runs the game
    :param wanted_player: the wanted player to play the game
    :param display: the display to display the game on
    :return: None
    """
    # Initializing the player and saving it's name
    if wanted_player == None:
        # Instead of automatically initiating the wanted player to be a human player
        # I decided to initiate it to None and than changing it so I could also
        # print it was automatically initiated to a human player
        player: AbstractPlayer = HumanPlayer
        print('________________________________________________________________________\n\n'
              'None player given, automatically initiated to a human player'
              '\n________________________________________________________________________')
    else:
        player: AbstractPlayer = wanted_player

    player_name = str(player)

    # choosing the game FPS - for bots faster FPS
    fps = SLOW_FPS
    if player_name in ['ai_shortcut', 'ai_bfs', 'ai_astar']:
        fps = FAST_FPS
    elif player_name == 'ai_dfs':
        fps = SPEEEED_FPS

    # Creating the game
    snake_game: Game = Game(display, fps=fps)
    game_over, score, snake, direction, food = snake_game.game_state()

    # Initializing the game recorder with the starting game state
    dir_name: str = str(player) + '_history'  # the name of the directory to save the game in
    recorder: Recorder = Recorder(snake, food)

    # Game loop - loops till game over
    while 1:
        action = player.action(snake, direction, food)  # getting the action from the player according the current state
        game_over, score, snake, direction, food = snake_game.play_game_step(action)
        recorder.update(snake, food)  # updating the new game state into the record

        # breaking from the main loop if the game is over
        if game_over:
            break

    # Setting the "Game Over" image to end the game
    image = pygame.image.load('images/game_over.png')  # loading the image
    image = pygame.transform.scale(image, (SIZE * BLOCK_SIZE, SIZE * BLOCK_SIZE))  # rescaling the image
    display.fill(BLACK)  # filling the display with BLACK color
    display.blit(image, [0, 0])  # displaying the image on the display
    pygame.display.flip()  # flipping the image from the graphic card to the computer screen

    keep_game_over_screen = True

    # keeping the script running and showing the "Game Over" screen while the user hasn't asked to stop
    while keep_game_over_screen:
        # looping over the events occurring and filtering out the relevant ones
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # checking if the event is a press on a key
                if event.key == pygame.K_SPACE:  # checking if the pressed key was the space bar
                    keep_game_over_screen = False  # stopping the "Game Over" Screen

    # saving the record
    recorder.hard_save(dir_name=dir_name)


if __name__ == '__main__':
    main()
