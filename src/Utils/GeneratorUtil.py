import numpy as np
from random import *
from random import random
from System.Agents.ManagingAgent.agent import *


class GeneratorUtil:

    age_distribution = (35.6, 25)
    temperature_distribution = (36.8, 0.4)

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

    @staticmethod
    def generate_thermal_data():
        dist = GeneratorUtil.temperature_distribution
        temp = GeneratorUtil.generate_in_distribution(dist[0], dist[1])[0]
        return {
            "temperature": temp
        }

    @staticmethod
    def generate_service_time(dist):
        time = GeneratorUtil.generate_in_distribution(dist[0], dist[1], n=1)[0]
        if time < 0:
            return 0
        return int(time)

