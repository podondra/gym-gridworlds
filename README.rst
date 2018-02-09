OpenAI gym Gridworlds
=====================

Implementation of three gridworlds environments
from book `Reinforcement Learning: An Introduction
<http://incompleteideas.net/book/the-book-2nd.html>`_
compatible with `OpenAI gym <https://github.com/openai/gym>`_.

Usage
-----

.. code::

        $ import gym
        $ import gym_gridworlds
        $ env = gym.make('Gridworld-v0')  # substitute environment's name

``Gridworld-v0``
----------------

Gridworld is simple 4 times 4 gridworld from example 4.1 in the [book].
There are fout action in each state (up, down, right, left)
which deterministically cause the corresponding state transitions
but actions that would take an agent of the grid leave a state unchanged.
The reward is -1 for all tranistion until the terminal state is reached.
The terminal state is in top left and bottom right coners.

``WindyGridworld-v0``
---------------------

Windy gridworld is from example 6.5 in the book_.
Windy gridworld is a standard gridworld as described above
but there is a crosswind upward through the middle of the grid.
Action are standard but in the middle region the resultant states are
shifted upward by a wind which strength varies between columns.

.. _book: http://incompleteideas.net/book/the-book-2nd.html

``Cliff-v0``
------------

Cliff walking is a gridworld example 6.6 from the book_.
Again reward is -1 on all transition except those into region
that is cliff.
Stepping into this region incurs a reward of -100
and sends the agent instantly back to the start.
