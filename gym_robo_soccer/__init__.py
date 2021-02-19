from gym.envs.registration import register

register(
    id='Goal-Robo-Soccer-v0',
    entry_point='gym_robo_soccer.envs:GoalEnv',
)