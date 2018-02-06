import gym
from gym import spaces


class WindyGridworldEnv(gym.Env):
    def __init__(self):
        self.height = 7
        self.width = 10
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Tuple((
                spaces.Discrete(self.height),
                spaces.Discrete(self.width)
                ))
        self.moves = {
                0: (-1, 0),  # up
                1: (0, 1),   # right
                2: (1, 0),   # down
                3: (0, -1),  # left
                }

        # begin in start state
        self.reset()

    def step(self, action):
        if self.S[1] in (3, 4, 5, 8):
            self.S = self.S[0] - 1, self.S[1]
        elif self.S[1] in (6, 7):
            self.S = self.S[0] - 2, self.S[1]

        x, y = self.moves[action]
        self.S = self.S[0] + x, self.S[1] + y

        self.S = max(0, self.S[0]), max(0, self.S[1])
        self.S = (min(self.S[0], self.height - 1),
                  min(self.S[1], self.width - 1))

        if self.S == (3, 7):
            return self.S, -1, True, {}
        return self.S, -1, False, {}

    def reset(self):
        self.S = (3, 0)
        return self.S
