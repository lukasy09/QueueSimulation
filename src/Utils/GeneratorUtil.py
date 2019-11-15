import numpy as np
from random import *
from random import random


class GeneratorUtil:

    age_distribution = (35.6, 25)

    @staticmethod
    def generate_integer_in_range(low=0, high=1):
        return randrange(low, high)

    @staticmethod
    def decide(probability):
        return random() <= probability

    @staticmethod
    def generate_in_distribution(mu, sigma, n=1):
        return np.random.normal(mu, sigma, n)

    @staticmethod
    def generate_uniform_random():
        return random()

    @staticmethod
    def get_next_appear_time(low, high, current_time):
        return GeneratorUtil.generate_integer_in_range(low + current_time, high + current_time + 1)

    @staticmethod
    def generate_shopping_time(mu, sigma):
        return int(round(GeneratorUtil.generate_in_distribution(mu, sigma, n=1)[0]))

    @staticmethod
    def generate_customer_data():
        age_dist = GeneratorUtil.age_distribution
        age = GeneratorUtil.generate_in_distribution(age_dist[0], age_dist[1])[0]
        sex = GeneratorUtil.generate_uniform_random()
        disable = GeneratorUtil.generate_uniform_random()
        pregnant = GeneratorUtil.generate_uniform_random()

        return {
            "age": age,
            "sex": sex,
            "disable": disable,
            "pregnant": pregnant
        }