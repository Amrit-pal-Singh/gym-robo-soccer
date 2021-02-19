import time
# import pitch
import gym
from array import array
import numpy as np
from gym_robo_soccer.envs.goal_env import GoalEnv

# env = gym.make('Goal-v0')
env = GoalEnv()



done = False
while not done:
    # print(env.action_space)
    env.render()
    env.step([1, [-1.2, 12, 60.5, 1.2]])
    # env.step([1, [-1.2, 12, 60.5, 1.2]])
