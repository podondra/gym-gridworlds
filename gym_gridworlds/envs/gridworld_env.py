import gym
from gym import spaces
import numpy


class GridworldEnv(gym.Env):
    reward_range = (-1, 0)
    action_space = spaces.Discrete(4)
    # although there are 2 terminal squares in the grid
    # they are considered as 1 state
    # therefore observation is between 0 and 14
    observation_space = spaces.Discrete(15)

    def __init__(self):
        gridworld = numpy.arange(
                self.observation_space.n + 1
                ).reshape((4, 4))
        gridworld[-1, -1] = 0
        # state transition matrix
        self.P = numpy.zeros((self.action_space.n,
                              self.observation_space.n,
                              self.observation_space.n))
        # any action taken in terminal state has no effect
        self.P[:, 0, 0] = 1

        for s in gridworld.flat[1:-1]:
            row, col = numpy.argwhere(gridworld == s)[0]
            for a, d in zip(
                    range(self.action_space.n),
                    [(-1, 0), (0, 1), (1, 0), (0, -1)]
                    ):
                next_row = max(0, min(row + d[0], 3))
                next_col = max(0, min(col + d[1], 3))
                s_prime = gridworld[next_row, next_col]
                self.P[a, s, s_prime] = 1

        self.R = numpy.full((self.action_space.n,
                             self.observation_space.n), -1)
        self.R[:, 0] = 0
