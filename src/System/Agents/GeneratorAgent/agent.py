import uuid
import numpy as np
from random import *
from src.System.Actors.Customer.builder import CustomerBuilder
from random import choice, random


def generate_number_in_range(low=0, high=1):
    return randrange(low, high)


def decide(probability):
    return random() < probability


def generate_in_distribution(mu, sigma, n=1):
    return np.random.normal(mu, sigma, n)


class GeneratorAgent:
    minimal_age = 18
    maximal_age = 90
    sex_options = ["M", "F"]
    temp_mu = 36.6
    temp_sigma = 0.4
    disable_probability = 0.05
    pregnant_probability = 0.04
    hurry_probability = 0.15

    def generate_customer(self):
        customer_builder = CustomerBuilder(str(uuid.uuid1()))
        age = generate_number_in_range(self.minimal_age, self.maximal_age)
        sex = choice(self.sex_options)
        temp = generate_in_distribution(self.temp_mu, self.temp_sigma, 1)
        is_disabled = decide(self.disable_probability)
        in_hurry = decide(self.hurry_probability)

        if sex == "F":
            is_pregnant = decide(self.pregnant_probability)
        else:
            is_pregnant = False

        customer_builder.set_age(age)\
            .set_sex(sex) \
            .set_temperature(temp)\
            .set_is_disable(is_disabled)\
            .set_is_pregnant(is_pregnant)\
            .set_is_in_hurry(in_hurry)


        return customer_builder.build()


