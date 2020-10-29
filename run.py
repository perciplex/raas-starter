import gym
import gym_raas
# pick your poison
import numpy as np
import tensorflow as tf
import torch

env = gym.make('RaasPendulum-v0')
env.reset()
obs = []
for i in range(50):
    print("Step {}: moving forward".format(i))
    observation, reward, done, info = env.step([1])
    print("\tObs: {}\tRew: {}".format(observation, reward))
    obs.append(observation)

for i in range(50):
    print("Step {}: moving backwards".format(i))
    observation, reward, done, info = env.step([-1])
    print("\tObs: {}\tRew: {}".format(observation, reward))
    obs.append(observation)
