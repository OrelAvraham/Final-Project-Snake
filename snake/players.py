from abc import ABC
import math

from snake.game_constants import *
import random
from utils.data_structures import *


class AbstractPlayer(ABC):
    # An abstract class that that represents a snake player
    def action(self, snake, direction, food):
        """
        A snake player action
        :param snake: a list represents the snakes body [tail, ..., head]
        :param direction: the current snakes direction, from the COMPASS_ROSE
        :param food: the place of the food on the board
        :return: the direction the player decided the snake should move
        """
        ...

    def __str__(self):
        """
        A string function for a player
        :return: the player's name, to distinguish between different players
        """
        ...


class HumanPlayer(AbstractPlayer):
    """
    Human controlled player that moves the snake according to the arrows
    the arrows represent moves relative to the board (for instance up is not necessarily straight)
    """

    def action(self, snake, direction, food):

        # looping over the game events to check for keyboard input
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # checking if the current event is a key pressing
                if event.key == pygame.K_LEFT:  # left arrow -> return LEFT direction
                    return LEFT
                elif event.key == pygame.K_RIGHT:  # right arrow -> return RIGHT direction
                    return RIGHT
                elif event.key == pygame.K_UP:  # up arrow -> return UP direction
                    return UP
                elif event.key == pygame.K_DOWN:  # down arrow -> return DOWN direction
                    return DOWN

        return STAY  # if no arrow was detected return the stay direction

    def __str__(self):
        return 'human_player'


class RandomPlayerAI(AbstractPlayer):
    """
    Software controlled agent that takes random actions in the game
    """

    def action(self, snake, direction, food):

        # Returning a random direction from the Compass Rose
        return random.choice(COMPASS_ROSE)

    def __str__(self):
        return 'ai_random'


class ShortcutPlayerAI(AbstractPlayer):
    """
    Software controlled agent that goes to the point (out of the 3 optional points) that is closest to the apple
    """

    def action(self, snake, direction, food):
        head = snake[-1]

        # Find the 3 possible directions
        curr_direction_index = COMPASS_ROSE.index(direction)
        left = COMPASS_ROSE[(curr_direction_index - 1) % 4]
        straight = direction
        right = COMPASS_ROSE[(curr_direction_index + 1) % 4]
        directions = []

        # Calculate the points of those directions
        left_point = [a + b for a, b in zip(head, left)]
        straight_point = [a + b for a, b in zip(head, straight)]
        right_point = [a + b for a, b in zip(head, right)]
        points = []


        # inner function for checking the validity of the function
        def _valid_point(p):
            """
            inner function for checking the validity of a point - if its in the board and not on the snake
            :param p: a point
            :return: if the point is valid
            """
            return 0 <= p[0] < SIZE and 0 <= p[1] < SIZE and p not in snake

        # Adding the valid points into the points list and the directions to theme to the directions list

        if _valid_point(left_point):
            directions.append(left)
            points.append(left_point)

        if _valid_point(straight_point):
            directions.append(straight)
            points.append(straight_point)

        if _valid_point(right_point):
            directions.append(right)
            points.append(right_point)

        dists = []
        for point in points:  # appeding the distances of the point to a distances list
            dists.append(math.dist(point, food))

        # finding the point which is closest to the apple
        if len(dists) == 0:
            return STAY

        min_dist = min(dists)

        return directions[dists.index(min_dist)] # returning the

    def __str__(self):
        return 'ai_shortcut'


class DfsAI(AbstractPlayer):
    """
    Software controlled agent that calculates the rout to the food using bfs algorithm and follows it
    """

    def __init__(self):
        self.path = []
        self.ctr = 0
        self.snake = []

    def action(self, snake, direction, food):
        self.snake = snake
        if self.ctr == len(self.path):
            self.ctr = 1
            self.path = self._dfs(snake[-1], food)

        if self.path == None:
            self.path = []
            self.ctr = 0

            head = snake[-1]

            # Find the 3 possible directions
            curr_direction_index = COMPASS_ROSE.index(direction)
            left = COMPASS_ROSE[(curr_direction_index - 1) % 4]
            straight = direction
            right = COMPASS_ROSE[(curr_direction_index + 1) % 4]
            directions = []

            # Calculate the points of those directions
            left_point = [a + b for a, b in zip(head, left)]
            straight_point = [a + b for a, b in zip(head, straight)]
            right_point = [a + b for a, b in zip(head, right)]
            points = []

            # Save the ones that are valid

            if self._valid_point(left_point, self.snake):
                points.append(left_point)
                directions.append(left)

            if self._valid_point(straight_point, self.snake):
                points.append(straight_point)
                directions.append(straight)

            if self._valid_point(right_point, self.snake):
                points.append(right_point)
                directions.append(right)


            if len(directions) == 0:
                return STAY
            return random.choice(directions)


        else:
            p1 = self.path[self.ctr - 1]
            p2 = self.path[self.ctr]
            self.ctr += 1
            return tuple([a - b for a, b in zip(p2, p1)])

    def _valid_point(self, point, snake):
        x, y = point
        return 0 <= x < SIZE and 0 <= y < SIZE and point not in snake[:-1]

    def _expand(self, point, snake):
        surrounding_points = []
        up = [a + b for a, b in zip(point, UP)]
        right = [a + b for a, b in zip(point, RIGHT)]
        down = [a + b for a, b in zip(point, DOWN)]
        left = [a + b for a, b in zip(point, LEFT)]

        if self._valid_point(up, snake):
            surrounding_points.append(up)

        if self._valid_point(right, snake):
            surrounding_points.append(right)

        if self._valid_point(down, snake):
            surrounding_points.append(down)

        if self._valid_point(left, snake):
            surrounding_points.append(left)

        return surrounding_points

    def _dfs(self, start, goal):
        stack = Stack()
        stack.push((start, [start]))
        explored = []
        while not stack.is_empty():
            papa, path = stack.pop()
            if papa == goal:
                return path
            if papa not in explored:
                explored.append(papa)
                for child in self._expand(papa, self.snake):
                    stack.push((child, path + [child]))

        return None

    def __str__(self):
        return 'ai_dfs'


class BfsAI(AbstractPlayer):
    """
    Software controlled agent that calculates the rout to the food using dfs algorithm and follows it
    """

    def __init__(self):
        self.path = []
        self.ctr = 0
        self.snake = []

    def action(self, snake, direction, food):
        self.snake = snake
        if self.ctr == len(self.path):
            self.ctr = 1
            self.path = self._bfs(snake[-1], food)

        if self.path == None:
            self.path = []
            self.ctr = 0

            head = snake[-1]

            # Find the 3 possible directions
            curr_direction_index = COMPASS_ROSE.index(direction)
            left = COMPASS_ROSE[(curr_direction_index - 1) % 4]
            straight = direction
            right = COMPASS_ROSE[(curr_direction_index + 1) % 4]
            directions = []

            # Calculate the points of those directions
            left_point = [a + b for a, b in zip(head, left)]
            straight_point = [a + b for a, b in zip(head, straight)]
            right_point = [a + b for a, b in zip(head, right)]
            points = []

            # Save the ones that are valid

            if self._valid_point(left_point, self.snake):
                points.append(left_point)
                directions.append(left)

            if self._valid_point(straight_point, self.snake):
                points.append(straight_point)
                directions.append(straight)

            if self._valid_point(right_point, self.snake):
                points.append(right_point)
                directions.append(right)

            if len(directions) == 0:
                return STAY
            return random.choice(directions)

        else:
            p1 = self.path[self.ctr - 1]
            p2 = self.path[self.ctr]
            self.ctr += 1
            return tuple([a - b for a, b in zip(p2, p1)])

    def _valid_point(self, point, snake):
        x, y = point
        return 0 <= x < SIZE and 0 <= y < SIZE and point not in snake[:-1]

    def _expand(self, point, snake):
        surrounding_points = []
        up = [a + b for a, b in zip(point, UP)]
        right = [a + b for a, b in zip(point, RIGHT)]
        down = [a + b for a, b in zip(point, DOWN)]
        left = [a + b for a, b in zip(point, LEFT)]

        if self._valid_point(up, snake):
            surrounding_points.append(up)

        if self._valid_point(right, snake):
            surrounding_points.append(right)

        if self._valid_point(down, snake):
            surrounding_points.append(down)

        if self._valid_point(left, snake):
            surrounding_points.append(left)

        return surrounding_points

    def _bfs(self, start, goal):
        queue = Queue()
        queue.push((start, [start]))
        explored = []
        while not queue.is_empty():
            papa, path = queue.pop()
            if papa == goal:
                return path
            if papa not in explored:
                explored.append(papa)
                for child in self._expand(papa, self.snake):
                    queue.push((child, path + [child]))

        return None

    def __str__(self):
        return 'ai_bfs'


class AStarAI(AbstractPlayer):
    def __init__(self):
        self.path = []
        self.ctr = 0
        self.snake = []

    def action(self, snake, direction, food):
        self.snake = snake
        if self.ctr == len(self.path):
            self.ctr = 1
            self.path = self._a_star(snake[-1], food, self.manhattan_distance)

            # print('Path:', self.path)
        if self.path == None:
            self.path = []
            self.ctr = 0

            head = snake[-1]

            # Find the 3 possible directions
            curr_direction_index = COMPASS_ROSE.index(direction)
            left = COMPASS_ROSE[(curr_direction_index - 1) % 4]
            straight = direction
            right = COMPASS_ROSE[(curr_direction_index + 1) % 4]
            directions = []

            # Calculate the points of those directions
            left_point = [a + b for a, b in zip(head, left)]
            straight_point = [a + b for a, b in zip(head, straight)]
            right_point = [a + b for a, b in zip(head, right)]
            points = []

            # save the noes ones on the snake

            if self._valid_point(left_point, self.snake):
                points.append(left_point)
                directions.append(left)

            if self._valid_point(straight_point, self.snake):
                points.append(straight_point)
                directions.append(straight)

            if self._valid_point(right_point, self.snake):
                points.append(right_point)
                directions.append(right)


            if len(directions) == 0:
                return STAY
            return random.choice(directions)

        else:
            p1 = self.path[self.ctr - 1]
            p2 = self.path[self.ctr]
            self.ctr += 1
            return tuple([a - b for a, b in zip(p2, p1)])

    def _valid_point(self, point, snake):
        x, y = point
        return 0 <= x < SIZE and 0 <= y < SIZE and point not in snake[:-1]

    def _expand(self, point, snake):
        surrounding_points = []
        up = [a + b for a, b in zip(point, UP)]
        right = [a + b for a, b in zip(point, RIGHT)]
        down = [a + b for a, b in zip(point, DOWN)]
        left = [a + b for a, b in zip(point, LEFT)]

        if self._valid_point(up, snake):
            surrounding_points.append(up)

        if self._valid_point(right, snake):
            surrounding_points.append(right)

        if self._valid_point(down, snake):
            surrounding_points.append(down)

        if self._valid_point(left, snake):
            surrounding_points.append(left)

        return surrounding_points

    def manhattan_distance(self, start, goal):
        """
        Calculating the Manhattan distance between goal and start
        :param start: the starting point
        :param goal: the goal point
        :return: the Manhattan distance
        """
        x0, y0 = start
        x1, y1 = goal
        return (x1 - x0) + (y1 - y0)

    def euclidian_distance(self, start, goal):
        """
        Calculating the euclidean distance between the goal snd the start
        :param start: the starting point
        :param goal: the goal point
        :return: the euclidean distance
        """
        x0, y0 = start
        x1, y1 = goal
        return math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

    def zero(self, start, goal):
        """
        Returns Zero for any start and goal points. that makes the A* algorithm equivalent to Dijkstra
        which in Snake's case is equivalent to BFS
        :param start: the starting point
        :param goal: the goal point
        :return: 0
        """
        return 0

    def _a_star(self, start, goal, h):
        queue = PriorityQueue()
        queue.push((start, [start], 0), h(start, goal))
        explored = []

        while not queue.is_empty():
            papa, path, cost = queue.pop()
            if papa == goal:
                return path
            if papa not in explored:
                explored.append(papa)
                for child in self._expand(papa, self.snake):
                    queue.push((child, path + [child], cost + 1), cost + 1 + h(child, goal))

        return None

    def __str__(self):
        return 'ai_astar'


class DfsSmarterAI(AbstractPlayer):
    """
    Software controlled agent that calculates the rout to the food using bfs algorithm and follows it
    """

    def __init__(self):
        self.path = []
        self.ctr = 0
        self.snake = []

    def action(self, snake, direction, food):
        self.snake = snake
        if self.ctr == len(self.path):
            self.ctr = 1
            self.path = self.dfs(snake[-1], food)

            # print('Path:', self.path)

        if self.path == None:
            self.path = []
            self.ctr = 0

            head = snake[-1]

            # Find the 3 possible directions
            curr_direction_index = COMPASS_ROSE.index(direction)
            left = COMPASS_ROSE[(curr_direction_index - 1) % 4]
            straight = direction
            right = COMPASS_ROSE[(curr_direction_index + 1) % 4]
            directions = []

            # Calculate the points of those directions
            left_point = [a + b for a, b in zip(head, left)]
            straight_point = [a + b for a, b in zip(head, straight)]
            right_point = [a + b for a, b in zip(head, right)]
            points = []

            # save the noes ones on the snake

            if self._valid_point(left_point, self.snake):
                points.append(left_point)
                directions.append(left)

            if self._valid_point(straight_point, self.snake):
                points.append(straight_point)
                directions.append(straight)

            if self._valid_point(right_point, self.snake):
                points.append(right_point)
                directions.append(right)

            # TODO: maybe there is a better way than random

            if len(directions) == 0:
                return STAY
            return random.choice(directions)
            """END of attempt"""

        else:
            p1 = self.path[self.ctr - 1]
            p2 = self.path[self.ctr]
            self.ctr += 1
            return tuple([a - b for a, b in zip(p2, p1)])

    def _valid_point(self, point, snake):
        x, y = point
        return 0 <= x < SIZE and 0 <= y < SIZE and point not in snake[:-1]

    def expand(self, point, snake):
        surrounding_points = []
        up = [a + b for a, b in zip(point, UP)]
        right = [a + b for a, b in zip(point, RIGHT)]
        down = [a + b for a, b in zip(point, DOWN)]
        left = [a + b for a, b in zip(point, LEFT)]

        if self._valid_point(up, snake):
            surrounding_points.append(up)

        if self._valid_point(right, snake):
            surrounding_points.append(right)

        if self._valid_point(down, snake):
            surrounding_points.append(down)

        if self._valid_point(left, snake):
            surrounding_points.append(left)

        return surrounding_points

    def dfs(self, start, goal,):
        stack = Stack()
        stack.push((start, [start], self.snake))
        explored = []
        while not stack.is_empty():
            papa, path, last_snake = stack.pop()
            new_snake = last_snake[1:] + path[-1]
            if papa == goal:
                return path
            if papa not in explored:
                explored.append(papa)
                for child in self.expand(papa, new_snake):
                    stack.push((child, path + [child], new_snake))

        return None

    def __str__(self):
        return 'ai_dfs'


class BfsSmarterAI(AbstractPlayer):
    """
    Software controlled agent that calculates the rout to the food using dfs algorithm and follows it
    """

    def __init__(self):
        self.path = []
        self.ctr = 0
        self.snake = []

    def action(self, snake, direction, food):
        self.snake = snake
        if self.ctr == len(self.path):
            self.ctr = 1
            self.path = self.bfs(snake[-1], food)

            # print('Path:', self.path)
        if self.path == None:
            self.path = []
            self.ctr = 0

            head = snake[-1]

            # Find the 3 possible directions
            curr_direction_index = COMPASS_ROSE.index(direction)
            left = COMPASS_ROSE[(curr_direction_index - 1) % 4]
            straight = direction
            right = COMPASS_ROSE[(curr_direction_index + 1) % 4]
            directions = []

            # Calculate the points of those directions
            left_point = [a + b for a, b in zip(head, left)]
            straight_point = [a + b for a, b in zip(head, straight)]
            right_point = [a + b for a, b in zip(head, right)]
            points = []

            # save the noes ones on the snake

            if self._valid_point(left_point, self.snake):
                points.append(left_point)
                directions.append(left)

            if self._valid_point(straight_point, self.snake):
                points.append(straight_point)
                directions.append(straight)

            if self._valid_point(right_point, self.snake):
                points.append(right_point)
                directions.append(right)

            # TODO: maybe there is a better way than random

            if len(directions) == 0:
                return STAY
            return random.choice(directions)
            """END of attempt"""

        else:
            p1 = self.path[self.ctr - 1]
            p2 = self.path[self.ctr]
            self.ctr += 1
            return tuple([a - b for a, b in zip(p2, p1)])

    def _valid_point(self, point, snake):
        x, y = point
        return 0 <= x < SIZE and 0 <= y < SIZE and point not in snake[:-1]

    def expand(self, point, snake):
        surrounding_points = []
        up = [a + b for a, b in zip(point, UP)]
        right = [a + b for a, b in zip(point, RIGHT)]
        down = [a + b for a, b in zip(point, DOWN)]
        left = [a + b for a, b in zip(point, LEFT)]

        if self._valid_point(up, snake):
            surrounding_points.append(up)

        if self._valid_point(right, snake):
            surrounding_points.append(right)

        if self._valid_point(down, snake):
            surrounding_points.append(down)

        if self._valid_point(left, snake):
            surrounding_points.append(left)

        return surrounding_points

    def bfs(self, start, goal):
        queue = Queue()
        queue.push((start, [start], self.snake))
        explored = []
        while not queue.is_empty():
            papa, path, last_sake = queue.pop()
            new_snake = last_sake[1:] + path[-1]
            if papa == goal:
                return path
            if papa not in explored:
                explored.append(papa)
                for child in self.expand(papa, new_snake):
                    queue.push((child, path + [child], new_snake))

        return None

    def __str__(self):
        return 'ai_bfs'


class AStarSmarterAI(AbstractPlayer):
    def __init__(self):
        self.path = []
        self.ctr = 0
        self.snake = []

    def action(self, snake, direction, food):
        self.snake = snake
        if self.ctr == len(self.path):
            self.ctr = 1
            self.path = self.a_star(snake[-1], food, self.manhattan_distance)

            # print('Path:', self.path)
        if self.path == None:
            self.path = []
            self.ctr = 0

            """AN attempt to make the snake a bit smarter so it willnot kill itself unless no other option"""
            head = snake[-1]

            # Find the 3 possible directions
            curr_direction_index = COMPASS_ROSE.index(direction)
            left = COMPASS_ROSE[(curr_direction_index - 1) % 4]
            straight = direction
            right = COMPASS_ROSE[(curr_direction_index + 1) % 4]
            directions = []

            # Calculate the points of those directions
            left_point = [a + b for a, b in zip(head, left)]
            straight_point = [a + b for a, b in zip(head, straight)]
            right_point = [a + b for a, b in zip(head, right)]
            points = []

            # save the noes ones on the snake

            if self._valid_point(left_point, self.snake):
                points.append(left_point)
                directions.append(left)

            if self._valid_point(straight_point, self.snake):
                points.append(straight_point)
                directions.append(straight)

            if self._valid_point(right_point, self.snake):
                points.append(right_point)
                directions.append(right)

            # TODO: maybe there is a better way than random

            if len(directions) == 0:
                return STAY
            return random.choice(directions)
            """END of attempt"""

        else:
            p1 = self.path[self.ctr - 1]
            p2 = self.path[self.ctr]
            self.ctr += 1
            return tuple([a - b for a, b in zip(p2, p1)])

    def _valid_point(self, point, snake):
        x, y = point
        return 0 <= x < SIZE and 0 <= y < SIZE and point not in snake[:-1]

    def expand(self, point, snake):
        surrounding_points = []
        up = [a + b for a, b in zip(point, UP)]
        right = [a + b for a, b in zip(point, RIGHT)]
        down = [a + b for a, b in zip(point, DOWN)]
        left = [a + b for a, b in zip(point, LEFT)]

        if self._valid_point(up, snake):
            surrounding_points.append(up)

        if self._valid_point(right, snake):
            surrounding_points.append(right)

        if self._valid_point(down, snake):
            surrounding_points.append(down)

        if self._valid_point(left, snake):
            surrounding_points.append(left)

        return surrounding_points

    def manhattan_distance(self, start, goal):
        x0, y0 = start
        x1, y1 = goal
        return (x1 - x0) + (y1 - y0)

    def euclidian_distance(self, start, goal):
        x0, y0 = start
        x1, y1 = goal
        return math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

    def zero(self, start, goal):  # makes A* work like dijkstra, in our case equivalent to BFS
        return 0

    def a_star(self, start, goal, h):
        queue = PriorityQueue()
        queue.push((start, [start], 0, self.snake), h(start, goal))
        explored = []

        while not queue.is_empty():
            papa, path, cost, last_snake = queue.pop()
            new_snake = last_snake[1:] + path[-1]
            if papa == goal:
                return path
            if papa not in explored:
                explored.append(papa)
                for child in self.expand(papa, new_snake):
                    queue.push((child, path + [child], cost + 1, new_snake), cost + 1 + h(child, goal))

        return None

    def __str__(self):
        return 'ai_astar'