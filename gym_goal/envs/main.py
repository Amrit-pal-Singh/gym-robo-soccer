import time
# import pitch
import gym
from array import array
import numpy as np
import gym_goal 
import gym_goal
from gym_goal.envs.goal_env import GoalEnv

# env = gym.make('Goal-v0')
env = GoalEnv()



done = False
while not done:
    # print(env.action_space)
    env.step([1, [-1.2, 12, 60.5, 1.2]])
    env.step([2, [-1.2, 12, 60.5, 1.2]])
    env.render()