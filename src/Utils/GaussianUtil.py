import numpy as np
from random import *
from random import random


def generate_integer_in_range(low=0, high=1):
    return randrange(low, high)


def decide(probability):
    return random() < probability


def generate_in_distribution(mu, sigma, n=1):
    return np.random.normal(mu, sigma, n)


def generate_uniform_random():
    return random()