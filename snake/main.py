from snake.game import Game
from snake.players import *
from snake.recorder import Recorder

def main():
    snake_game: Game = Game()
    player: AbstractPlayer = Hamilton()
    dir_name: str = str(player) + '_history'
    recorder: Recorder = None
    while 1:
        iteration, game_over, score, snake_body, food, reward = snake_game.play_game_step(player)
        if not recorder:
            recorder = Recorder(snake_body, food)
        else:
            recorder.update(snake_body, food, reward)

        if game_over:
            break

    recorder.hard_save(dir_name=dir_name)


if __name__ == '__main__':
    main()
