import time
# import pitch
import gym
from array import array
import numpy as np
from gym_robo_soccer.envs.goal_env import GoalEnv

# env = gym.make('Goal-v0')
TEAM1_PLAYERS = 4
TEAM2_PLAYERS = 3
env = GoalEnv(TEAM1_PLAYERS, TEAM2_PLAYERS)



done = False
while not done:
    # print(env.action_space)
    env.render()
    env.external_input()
    env.step(TEAM1_PLAYERS-1, [1, [-1.2, 12, 60.5, 1.2]])
    # env.step([1, [-1.2, 12, 60.5, 1.2]])
