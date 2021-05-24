from snake.game import Game
from snake.player import AbstractPlayer, ShortcutPlayerAI, HumanPlayer
import os

class Recorder:
    def __init__(self, snake_body, food):
        self.snake_history = snake_body
        self.lengths = [len(snake_body)]
        self.foods = [food]

    def update(self, snake_body, food):
        self.snake_history.append(snake_body[-1])
        self.lengths.append(len(snake_body))
        self.foods.append(food)

    def hard_save(self, name=None):
        if not name:
            n = len(os.listdir('game_history'))
            name = f'Game{n}'
        path = f'game_history/{name}.snake'
        while os.path.exists(path):
            name = input('Name already exists, enter another one:')
            path = f'{name}.snake'

        with open(path, 'w') as f:
            f.write(str(self.snake_history))
            f.write('\n')
            f.write(str(self.lengths))
            f.write('\n')
            f.write(str(self.foods))



def main():
    snake_game: Game = Game()
    player: AbstractPlayer = ShortcutPlayerAI()
    recorder: Recorder = None
    while 1:
        iteration, game_over, score, snake_body, food = snake_game.play_game_step(player)
        if not recorder:
            recorder = Recorder(snake_body, food)
        else:
            recorder.update(snake_body, food)

        if game_over:
            break

    recorder.hard_save()

if __name__ == '__main__':
    main()
