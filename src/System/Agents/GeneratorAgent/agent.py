from Database.DAO.customer_dao import CustomerDao
from System.Actors.Customer.customer import Customer
from System.Actors.Customer.customer_status import CustomerStatus
from Utils.GeneratorUtil import GeneratorUtil
import uuid


class GeneratorAgent:


    """Customers' parameters"""
    regular_probability = 0.2
    vip_probability = 0.1

    customer_pool = []

    def __init__(self, dao):
        self.dao = dao

    def generate_population(self, size):
        self.dao.initialise_customers_table()
        for i in range(0, size):
            biometric = self.generate_biometric()
            customer = self.generate_customer(index=i, biometric=biometric)
            # The customer is a regular one. He will be saved to the main database.
            criteria = GeneratorUtil.generate_uniform_random()
            if criteria <= self.vip_probability:
                is_new = False
                customer_status = CustomerStatus.VIP
                customer.set_customer_status(customer_status)
                self.dao.save_customer(customer, customer_status, is_new)
            self.customer_pool.append(customer)
        return self.customer_pool


    """Generating a customer"""
    @staticmethod
    def generate_customer(index, biometric):
        return Customer(identifier=index, biometric=biometric)


    @staticmethod
    def generate_biometric():
        return uuid.uuid1()
