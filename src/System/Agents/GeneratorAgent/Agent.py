import uuid
import numpy as np
from random import *
from random import choice, random

from src.System.Actors.Customer.customer import Customer


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
    disable_probability = 0.05
    pregnant_probability = 0.04
    hurry_probability = 0.15

    customer_pool = []

    def generate_population(self, size):
        for i in range(0, size):
            customer = self.generate_customer()
            customer.set_index(i)
            self.customer_pool.append(customer)
        return self.customer_pool

    def generate_customer(self):

        age = generate_number_in_range(self.minimal_age, self.maximal_age)
        sex = choice(self.sex_options)
        disable = decide(self.disable_probability)
        hurry = decide(self.hurry_probability)

        if sex == "F":
            pregnant = decide(self.pregnant_probability)
        else:
            pregnant = False

        customer = Customer(identifier=str(uuid.uuid1()), age=age, sex=sex, disable=disable, pregnant=pregnant,
                            hurry=hurry)
        return customer

