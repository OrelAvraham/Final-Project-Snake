# Essential imports
from snake.players import *
from snake import play_game
from game_viewer import game_viewer
from pygame import mixer

pygame.init()

display = pygame.display.set_mode((SIZE * BLOCK_SIZE, SIZE * BLOCK_SIZE))  # Defining the game display
pygame.display.set_caption('Snake')
# loading the starting screen image
image = pygame.image.load('images/starting_screen.png')
image = pygame.transform.scale(image, (SIZE * BLOCK_SIZE, SIZE * BLOCK_SIZE))

mixer.music.load('images/bg.mp3')
mixer.music.play(-1)

# Initializing main loop flags
choosing_player = True
view_game = False
player: AbstractPlayer = None

# The main loop
while True:
    while choosing_player and not view_game:  # looping till the user chooses any option
        display.fill(WHITE)
        display.blit(image, [0, 0])
        pygame.display.flip()

        for event in pygame.event.get():  # checking the game events
            if event.type == pygame.QUIT:  # if event is quit -> quit the game
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:  # checking for key pressing events
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

                if event.key == pygame.K_0:  # key 0 -> choose Human player
                    player = HumanPlayer()
                    choosing_player = False

                elif event.key == pygame.K_1:  # key 1 -> choose Random player
                    player = RandomPlayerAI()
                    choosing_player = False

                elif event.key == pygame.K_2:  # key 2 -> choose Shortcut player
                    player = ShortcutPlayerAI()
                    choosing_player = False

                elif event.key == pygame.K_3:  # key 3 -> choose DFS player
                    player = DfsAI()
                    choosing_player = False

                elif event.key == pygame.K_4:  # key 4 -> choose BFS player
                    player = BfsAI()
                    choosing_player = False

                elif event.key == pygame.K_5:  # key 5 -> choose A* player
                    player = AStarAI()
                    choosing_player = False

                elif event.key == pygame.K_SPACE:  # key SPACE -> choose game viewer
                    print('0', view_game)
                    view_game = True
                    print('1', view_game)

    # Running the asked task
    if not choosing_player:
        mixer.music.stop()
        play_game.main(player, display)
        mixer.music.play(-1)
        choosing_player = True


    elif view_game:
        mixer.music.stop()
        game_viewer.main(display)
        mixer.music.play(-1)
        view_game = False

    else:  # the code shouldn't ever get to here, if got to here print "ERROR"
        print('ERROR')

if __name__ == '__main__':
    pass
