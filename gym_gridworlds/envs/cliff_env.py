import gym
from gym import spaces


class CliffEnv(gym.Env):
    def __init__(self):
        self.height = 4
        self.width = 12
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Tuple((
                spaces.Discrete(self.height),
                spaces.Discrete(self.width)
                ))
        self.moves = {
                0: (-1, 0),   # up
                1: (0, 1),   # right
                2: (1, 0),  # down
                3: (0, -1),  # left
                }

        # begin in start state
        self.reset()

    def step(self, action):
        x, y = self.moves[action]
        self.S = self.S[0] + x, self.S[1] + y

        self.S = max(0, self.S[0]), max(0, self.S[1])
        self.S = (min(self.S[0], self.height - 1),
                  min(self.S[1], self.width - 1))

        if self.S == (self.height - 1, self.width - 1):
            return self.S, -1, True, {}
        elif self.S[1] != 0 and self.S[0] == self.height - 1:
            # the cliff
            return self.reset(), -100, False, {}
        return self.S, -1, False, {}

    def reset(self):
        self.S = (3, 0)
        return self.S
