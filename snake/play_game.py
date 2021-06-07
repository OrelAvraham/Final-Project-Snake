from snake.game import Game
from snake.players import *
from game_viewer.recorder import Recorder


def main(wanted_player: AbstractPlayer, display=pygame.display.set_mode((SIZE * BLOCK_SIZE, SIZE * BLOCK_SIZE))):
    player: AbstractPlayer = wanted_player
    player_name = str(player)

    fps = SLOW_FPS
    if player_name in ['ai_shortcut', 'ai_bfs', 'ai_astar']:
        fps = FAST_FPS
    elif player_name == 'ai_dfs':
        fps = SPEEEED_FPS

    snake_game: Game = Game(display, fps=fps)
    game_over, score, snake, direction, food = snake_game.game_state()

    dir_name: str = str(player) + '_history'
    recorder: Recorder = Recorder(snake, food)
    while 1:
        action = player.action(snake, direction, food)
        game_over, score, snake, direction, food = snake_game.play_game_step(action)
        recorder.update(snake, food)

        if game_over:
            break

    recorder.hard_save(dir_name=dir_name)


if __name__ == '__main__':
    main()
