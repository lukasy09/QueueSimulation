"""
    The class represents the system's main actor
"""


class Customer:
    id = None
    index = None  # Informs about creation order of customers
    age = None
    sex = None
    disable = None
    pregnant = None
    hurry = None

    status = None

    def __init__(self, identifier, age, sex, disable, pregnant, hurry):
        self.id = identifier
        self.age = age
        self.sex = sex
        self.disable = disable
        self.pregnant = pregnant
        self.hurry = hurry

    def set_index(self, index):
        self.index = index


    def __str__(self):
        return "Customer:Index {}, Age:{}, Sex:{}, Disable:{}, Pregnant: {}, In hurry: {}".format(self.index, self.age,
                                                                                                  self.sex,
                                                                                                  self.disable,
                                                                                                  self.pregnant,
                                                                                                  self.hurry)
