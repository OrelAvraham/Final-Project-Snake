from snake.game import Game
from snake.players import *
import os


class Recorder:
    # TODO: use Iziks technic of saving long list of the snake and lengths instead of saving the snake of each turn
    def __init__(self, snake, food, reward=0):
        self.snakes = [snake]
        # self.lengths = [len(snake)]
        self.foods = [food]
        self.rewards = [reward]

    def update(self, snake, food, reward):
        self.snakes.append(snake)
        # self.lengths.append(len(snake))
        self.foods.append(food)
        self.rewards.append(reward)

    def hard_save(self, game_name=None, dir_name='game_history'):
        if not game_name:
            n = len(os.listdir(f'../game_viewer/{dir_name}/'))
            game_name = f'Game{n}'
        path = f'../game_viewer/{dir_name}/{game_name}.RAZ'
        while os.path.exists(path):
            name = input('Name already exists, enter another one:')
            path = f'{name}.snake'

        with open(path, 'w') as f:
            f.write(str(self.snakes))
            f.write('\n')
            f.write(str(self.foods))
            f.write('\n')
            f.write(str(self.rewards))


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
