import numpy as np
from random import *
from random import random


class GeneratorUtil:

    @staticmethod
    def generate_integer_in_range(low=0, high=1):
        return randrange(low, high)

    @staticmethod
    def decide(probability):
        return random() < probability

    @staticmethod
    def generate_in_distribution(mu, sigma, n=1):
        return np.random.normal(mu, sigma, n)

    @staticmethod
    def generate_uniform_random():
        return random()

    @staticmethod
    def get_next_appear_time(low, high, current_time):
        return GeneratorUtil.generate_integer_in_range(low + current_time, high + current_time + 1)
