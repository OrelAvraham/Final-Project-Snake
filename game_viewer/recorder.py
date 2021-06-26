import os

class Recorder:
    def __init__(self, snake, food):
        """
        Constructor for the recorder, initializes it's variables
        :param snake: the starting snake of the game - to be recorded
        :param food:  the starting food of the game - to be recorded
        """
        self.snakes = [snake]  # list of the snakes
        self.foods = [food]  # list of the foods

    def update(self, snake, food):
        """
        updates the lists of the recorded information
        :param snake: the current snake to be recorded
        :param food: the current food (of the same state) to be recorded
        :return: None
        """
        # updating the lists with the new information - the next state of the game
        self.snakes.append(snake)
        self.foods.append(food)

    def hard_save(self, game_name=None, dir_name='human_history'):
        """
        saves a RAZ file of the recording
        :param game_name: the name of the game, if None will automativally be "Game{number}.RAZ"
        :param dir_name: the directory to save the game in, automatically set to "human_history"
        :return:
        """
        if not game_name:
            n = len(os.listdir(os.path.join(os.path.dirname(__file__), f'{dir_name}')))
            game_name = f'Game{n}'
        path = os.path.join(os.path.dirname(__file__), f'{dir_name}/{game_name}.RAZ')
        while os.path.exists(path):
            name = input('Name already exists, enter another one:')
            path = os.path.join(os.path.dirname(__file__), f'{dir_name}/{game_name}.RAZ')

        with open(path, 'w') as f:
            f.write(str(self.snakes))
            f.write('\n')
            f.write(str(self.foods))