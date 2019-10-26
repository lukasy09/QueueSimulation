from src.System.Actors.Customer.customer import Customer


class CustomerBuilder:
    customer = None

    def __init__(self, identifier):
        self.customer = Customer(identifier)

    """Building methods"""

    def set_age(self, age):
        self.customer.age = age
        return self

    def set_sex(self, sex):
        self.customer.sex = sex
        return self

    def set_temperature(self, temp):
        self.customer.temperature = temp
        return self

    def set_is_disable(self, is_disable):
        self.customer.is_disable = is_disable
        return self

    def set_is_pregnant(self, pregnant):
        self.customer.is_pregnant = pregnant
        return self

    def set_is_in_hurry(self, hurry):
        self.customer.is_in_hurry = hurry
        return self

    def build(self):
        return self.customer
