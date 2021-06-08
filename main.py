# Essential improts
from snake.players import *
from snake import play_game
from game_viewer import game_viewer

display = pygame.display.set_mode((SIZE * BLOCK_SIZE, SIZE * BLOCK_SIZE))  # Defining the game display

# loading the starting screen image
image = pygame.image.load('images/starting_screen.png')
image = pygame.transform.scale(image, (SIZE * BLOCK_SIZE, SIZE * BLOCK_SIZE))

# Initializing main loop flags
choosing_player = True  # A
view_game = False
player: AbstractPlayer = None

while True:
    while choosing_player and not view_game:
        display.fill(WHITE)
        display.blit(image, [0, 0])
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

                if event.key == pygame.K_0:
                    player = HumanPlayer()
                    choosing_player = False

                elif event.key == pygame.K_1:
                    player = RandomPlayerAI()
                    choosing_player = False

                elif event.key == pygame.K_2:
                    player = ShortcutPlayerAI()
                    choosing_player = False

                elif event.key == pygame.K_3:
                    player = DfsAI()
                    choosing_player = False

                elif event.key == pygame.K_4:
                    player = BfsAI()
                    choosing_player = False

                elif event.key == pygame.K_5:
                    player = AStarAI()
                    choosing_player = False

                elif event.key == pygame.K_SPACE:
                    print('0', view_game)
                    view_game = True
                    print('1', view_game)

    if not choosing_player:
        play_game.main(player, display)
        choosing_player = True

    elif view_game:
        view_game = False
        game_viewer.main(display)

    else:
        print('ERROR')

if __name__ == '__main__':
    pass
