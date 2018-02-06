import pytest


@pytest.fixture
def cliff():
    import gym
    import gym_gridworlds   # noqa
    return gym.make('Cliff-v0')


def test_cliff_action_space(cliff):
    assert cliff.action_space.n == 4


def test_cliff_step_on_cliff(cliff):
    S = cliff.reset()
    # check that in start state
    assert S == (3, 0)
    # move right
    S, R, _, _ = cliff.step(1)
    assert R == -100
    # check movement to start state
    assert S == (3, 0)
