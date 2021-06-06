import os

class Recorder:
    def __init__(self, snake, food):
        self.snakes = [snake]
        self.foods = [food]

    def update(self, snake, food):
        self.snakes.append(snake)
        self.foods.append(food)

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