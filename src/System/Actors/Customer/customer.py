class Customer:
    id = None
    age = None
    sex = None
    is_disable = None
    is_pregnant = None
    is_in_hurry = None

    def __init__(self, identifier):
        self.id = identifier

    def __str__(self):
        return "Customer: Age:{}, Sex:{}, Disable:{}, Pregnant: {}, In hurry: {}".format(self.age, self.sex,
                                                                                         self.is_disable,
                                                                                         self.is_pregnant,
                                                                                         self.is_in_hurry)
