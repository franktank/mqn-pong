import logging

#from gym.envs.registration import register

from .Maze import Maze
from .Maze import PATH_MAPPING, WALL_MAPPING, REWARD_MAPPING, \
                                DARK_MAPPING, INDICATOR_MAPPING, ANIMAT_MARKER

logger = logging.getLogger(__name__)

'''
Old action lookup for diagonal movement
ACTION_LOOKUP = {
    0: 'N',
    1: 'NE',
    2: 'E',
    3: 'SE',
    4: 'S',
    5: 'SW',
    6: 'W',
    7: 'NW'
}
'''
#Disabled diagonal movement.
ACTION_LOOKUP = {
    0: 'N',
    1: 'E',
    2: 'S',
    3: 'W'
}


def find_action_by_direction(direction):
    for key, val in ACTION_LOOKUP.items():
        if val == direction:
            return key

#Need to write a handler so that these don't get re-registered.
'''
register(
    id='MazeF1-v0',
    entry_point='gym_maze.envs:MazeF1',
    #max_episode_steps=50,
    #nondeterministic=False
)

register(
    id='MazeF2-v0',
    entry_point='gym_maze.envs:MazeF2',
    #max_episode_steps=50,
    #nondeterministic=False
)

register(
    id='MazeF3-v0',
    entry_point='gym_maze.envs:MazeF3',
    #max_episode_steps=50,
    #nondeterministic=False
)

register(
    id='MazeF4-v0',
    entry_point='gym_maze.envs:MazeF4',
    #max_episode_steps=50,
    #nondeterministic=True
)

register(
    id='Maze5-v0',
    entry_point='gym_maze.envs:Maze5',
    #max_episode_steps=50,
    #nondeterministic=True
)

register(
    id='BMaze4-v0',
    entry_point='gym_maze.envs:BMaze4',
    #max_episode_steps=50,
    #nondeterministic=False
)

register(
    id='IMaze2-v0',
    entry_point='gym_maze.envs:IMaze2',
    #max_episode_steps=50,
    #nondeterministic=False
)

register(
    id='IMaze3-v0',
    entry_point='gym_maze.envs:IMaze3',
    #max_episode_steps=50,
    #nondeterministic=False
)

register(
    id='IMaze6-v0',
    entry_point='gym_maze.envs:IMaze6',
    #max_episode_steps=50,
    #nondeterministic=False
)

register(
    id='IMaze8-v0',
    entry_point='gym_maze.envs:IMaze8',
    #max_episode_steps=50,
    #nondeterministic=False
)
'''



