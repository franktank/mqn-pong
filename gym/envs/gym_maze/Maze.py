import logging
from utils import raycastLine
import numpy as np
import random

logger = logging.getLogger(__name__)

DARK_MAPPING = 0
PATH_MAPPING = 1
WALL_MAPPING = 2
REWARD_MAPPING = [3, -3]
INDICATOR_MAPPING = [5, -5]
ANIMAT_MARKER = 7


class Maze:
    """
    Creates new maze.
    
    Mapping:
    0 - path
    1 - wall
    9 - reward
    """

    def __init__(self, matrix):
        self.matrix = matrix
        self.max_x = self.matrix.shape[1]
        self.max_y = self.matrix.shape[0]

    def get_possible_insertion_coordinates(self):
        """
        Returns a list with coordinates in the environment where
        an agent can be placed (only on the path).
        :return: list of tuples (X,Y) containing coordinates
        """
        possible_cords = []
        for x in range(0, self.max_x):
            for y in range(0, self.max_y):
                if self.is_path(x, y):
                    possible_cords.append((x, y))

        return possible_cords
    '''
    def perception(self, pos_x, pos_y):
        #Run the Bresenham line algorithm in a square pattern,
        #along the boundary of the maze. This is to simulate 
        #line-of-sight.
        visible_points = set([])
        for x in range(self.max_x):
            visible_points.update(raycastLine(pos_x, pos_y, x, 0, self))
            visible_points.update(raycastLine(pos_x, pos_y, x, self.max_y, self))
        for y in range(self.max_y):
            visible_points.update(raycastLine(pos_x, pos_y, 0, y, self))
            visible_points.update(raycastLine(pos_x, pos_y, self.max_x, y, self))
            
        perception = np.copy(self.matrix)
        all_points = set([(x,y) for y in range(self.max_y) for x in range(self.max_x)])
        #print "Set of visible points\n", visible_points
        #print "Set of non-visible points\n", all_points - visible_points
        
        for point in (all_points - visible_points):
            perception[point[1], point[0]] = DARK_MAPPING
        
        #print perception
        perception[pos_y,pos_x] = ANIMAT_MARKER
        perception = np.expand_dims(perception, axis=2)

        return perception
    '''
    
    def perception(self, pos_x, pos_y):
        if not self._within_x_range(pos_x):
            raise ValueError('X position not within allowed range')

        if not self._within_y_range(pos_y):
            raise ValueError('Y position not within allowed range')

            # Position N
        if pos_y == 0:
            n = None
        else:
            n = str(self.matrix[pos_y - 1, pos_x])

            # Position NE
        if pos_x == self.max_x - 1 or pos_y == 0:
            ne = None
        else:
            ne = str(self.matrix[pos_y - 1, pos_x + 1])

            # Position E
        if pos_x == self.max_x - 1:
            e = None
        else:
            e = str(self.matrix[pos_y, pos_x + 1])

            # Position SE
        if pos_x == self.max_x - 1 or pos_y == self.max_y - 1:
            se = None
        else:
            se = str(self.matrix[pos_y + 1, pos_x + 1])

            # Position S
        if pos_y == (self.max_y - 1):
            s = None
        else:
            s = str(self.matrix[pos_y + 1, pos_x])

            # Position SW
        if pos_x == 0 or pos_y == self.max_y - 1:
            sw = None
        else:
            sw = str(self.matrix[pos_y + 1, pos_x - 1])

            # Position W
        if pos_x == 0:
            w = None
        else:
            w = str(self.matrix[pos_y, pos_x - 1])

            # Position NW
        if pos_x == 0 or pos_y == 0:
            nw = None
        else:
            nw = str(self.matrix[pos_y - 1, pos_x - 1])

        return n, ne, e, se, s, sw, w, nw
    

    def is_wall(self, pos_x, pos_y):
        return self.matrix[pos_y, pos_x] == WALL_MAPPING

    def is_path(self, pos_x, pos_y):
        return self.matrix[pos_y, pos_x] == PATH_MAPPING

    def is_reward(self, pos_x, pos_y):
        #choice = random.randint(0, 2)
        #if(self.matrix[pos_y, pos_x] == REWARD_MAPPING[choice])
        return self.matrix[pos_y, pos_x] in REWARD_MAPPING

    def _within_x_range(self, x):
        return 0 <= x < self.max_x

    def _within_y_range(self, y):
        return 0 <= y < self.max_y

    @staticmethod
    #def moved_north(start, destination) -> bool:
    def moved_north(start, destination):
        """
        :param start: start (X, Y) coordinates tuple
        :param destination: destination (X, Y) coordinates tuple
        :return: true if it was north move
        """
        return destination[1] + 1 == start[1]

    @staticmethod
    #def moved_east(start, destination) -> bool:
    def moved_east(start, destination):
        """
        :param start: start (X, Y) coordinates tuple
        :param destination: destination (X, Y) coordinates tuple
        :return: true if it was east move
        """
        return destination[0] - 1 == start[0]

    @staticmethod
    #def moved_south(start, destination) -> bool:
    def moved_south(start, destination):
        """
        :param start: start (X, Y) coordinates tuple
        :param destination: destination (X, Y) coordinates tuple
        :return: true if it was south move
        """
        return destination[1] - 1 == start[1]

    @staticmethod
    #def moved_west(start, destination) -> bool:
    def moved_west(start, destination):
        """
        :param start: start (X, Y) coordinates tuple
        :param destination: destination (X, Y) coordinates tuple
        :return: true if it was west move
        """
        return destination[0] + 1 == start[0]

    @staticmethod
    def distinguish_direction(start, end):
        direction = ''

        if Maze.moved_north(start, end):
            direction += 'N'

        if Maze.moved_south(start, end):
            direction += 'S'

        if Maze.moved_west(start, end):
            direction += 'W'

        if Maze.moved_east(start, end):
            direction += 'E'

        return direction

    @staticmethod
    #def get_possible_neighbour_cords(pos_x, pos_y) -> tuple:
    def get_possible_neighbour_cords(pos_x, pos_y):
        """
        Returns a tuple with coordinates for
        N, NE, E, SE, S, SW, W, NW neighbouring cells.
        """
        n = (pos_x, pos_y - 1)
        ne = (pos_x + 1, pos_y - 1)
        e = (pos_x + 1, pos_y)
        se = (pos_x + 1, pos_y + 1)
        s = (pos_x, pos_y + 1)
        sw = (pos_x - 1, pos_y + 1)
        w = (pos_x - 1, pos_y)
        nw = (pos_x - 1, pos_y - 1)

        return n, ne, e, se, s, sw, w, nw
