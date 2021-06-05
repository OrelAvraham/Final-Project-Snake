import os

class Recorder:
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