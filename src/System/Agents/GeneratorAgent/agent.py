import uuid
from random import choice
from src.System.Actors.Customer.customer import Customer
from src.Utils.GaussianUtil import generate_number_in_range, decide


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

