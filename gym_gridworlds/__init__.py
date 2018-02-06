from gym.envs.registration import register

register(
        id='Gridworld-v0',
        entry_point='gym_gridworlds.envs:GridworldEnv',
        )
register(
        id='WindyGridworld-v0',
        entry_point='gym_gridworlds.envs:WindyGridworldEnv',
        )
register(
        id='Cliff-v0',
        entry_point='gym_gridworlds.envs:CliffEnv',
        )
