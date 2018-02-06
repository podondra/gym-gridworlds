import pytest
import numpy


@pytest.fixture
def gridworld():
    import gym
    import gym_gridworlds   # noqa
    return gym.make('Gridworld-v0')


def test_gridworld_action_space(gridworld):
    assert gridworld.action_space.n == 4


def test_gridworld_observation_space(gridworld):
    assert gridworld.observation_space.n == 15


def test_gridworld_transition_probabilities(gridworld):
    assert gridworld.P.shape == (4, 15, 15)
    # ensure that probabilities sum to 1
    assert numpy.all(gridworld.P.sum(axis=-1) == 1)


def test_gridworld_rewards(gridworld):
    assert gridworld.R.shape == (4, 15)
    # assert that there is 0 reward when moving in terminal state
    assert numpy.all(gridworld.R[:, 0] == 0)
    # all other rewards are -1
    assert numpy.all(gridworld.R[:, 1:] == -1)
