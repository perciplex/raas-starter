import gym
import gym_raas
import numpy as np
import time


env = gym.make('raaspendulum-v0')
env.reset()
obs = []
for i in range(50):
    print("Step {}: moving forward".format(i))
    observation, reward, done, info = env.step([1])
    print("\tObs: {}\tRew: {}".format(observation, reward))
    time.sleep(0.01)
    obs.append(observation)

for i in range(50):
    print("Step {}: moving backwards".format(i))
    observation, reward, done, info = env.step([-1])
    print("\tObs: {}\tRew: {}".format(observation, reward))
    time.sleep(0.01)
    obs.append(observation)
