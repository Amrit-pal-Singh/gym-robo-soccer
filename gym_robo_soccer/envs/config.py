"""
This file contains all the constant configurations
taken from the robot soccer server manual 7.07.
"""
import numpy as np

PLAYER_CONFIG = {
    'POWER_RATE': 0.006,
    'SIZE': 0.9,
    'RAND': 0.1,
    'ACCEL_MAX': 30.0,
    'SPEED_MAX': 30.0,
    'DECAY': 0.4,
    'MASS': 60
}

BALL_CONFIG = {
    'POWER_RATE': 0.027,
    'SIZE': 0.4,
    'RAND': 0.05,
    'ACCEL_MAX': 20.7,
    'SPEED_MAX': 20.7,
    'DECAY': 0.94,
    'MASS': 0.2
}

MINPOWER = -100
MAXPOWER = 100
KICKABLE = PLAYER_CONFIG['SIZE'] + 0.7
CATCHABLE = 2.0
CATCH_PROBABILITY = 1.0
INERTIA_MOMENT = 5.0
PITCH_LENGTH = 105  # 105
PITCH_START = 2
PITCH_WIDTH = 30  # 68
CENTRE_CIRCLE_RADIUS = 9.15
PENALTY_AREA_LENGTH = 16.5
PENALTY_AREA_WIDTH = 40.32
GOAL_AREA_LENGTH = 5.5
GOAL_AREA_WIDTH = 18.32
GOAL_WIDTH = 14.02
GOAL_DEPTH = 2.44
SPEED_PLAYER = 30
SPEED_GOALIE1 = 30
SPEED_GOALIE2 = 20

SCALE_VECTOR = np.array([PITCH_LENGTH / 2, PITCH_WIDTH, 2.0, 2.0, 2 * np.pi,
                         PITCH_LENGTH / 2, PITCH_WIDTH, 2.0, 2.0, 2 * np.pi,
                         PITCH_LENGTH / 2, PITCH_WIDTH, 6.0, 6.0])
SHIFT_VECTOR = np.array([0.0, PITCH_WIDTH / 2, 1.0, 1.0, np.pi,
                         0.0, PITCH_WIDTH / 2, 1.0, 1.0, np.pi,
                         0.0, PITCH_WIDTH / 2, 3, 3])
LOW_VECTOR = -SHIFT_VECTOR
HIGH_VECTOR = np.array(SCALE_VECTOR-SHIFT_VECTOR)
