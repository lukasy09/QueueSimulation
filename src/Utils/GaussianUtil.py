import numpy as np
from random import *
from random import random

class GaussianUtil:

    def generate_integer_in_range(self, low=0, high=1):
        return randrange(low, high)


    def decide(self, probability):
        return random() < probability


    def generate_in_distribution(self, mu, sigma, n=1):
        return np.random.normal(mu, sigma, n)


    def generate_uniform_random(self):
        return random()