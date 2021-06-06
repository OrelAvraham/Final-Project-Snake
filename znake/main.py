from znake.game import Game
from znake.players import *
from znake.recorder import Recorder

def main():
    znake_game: Game = Game()
    game_over, score, snake, direction, food = znake_game.game_state()

    player: AbstractPlayer = AStarAI()

    dir_name: str = str(player) + '_history'
    recorder: Recorder = Recorder(snake, food)
    while 1:
        action = player.action(snake, direction, food)
        game_over, score, snake, direction, food = znake_game.play_game_step(action)
        recorder.update(snake, food)

        if game_over:
            break

    recorder.hard_save(dir_name=dir_name)


if __name__ == '__main__':
    main()
