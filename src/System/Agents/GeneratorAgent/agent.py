from Database.DAO.customer_dao import CustomerDao
from System.Actors.Customer.customer import Customer
from System.Actors.Customer.customer_status import CustomerStatus
from Utils.GeneratorUtil import GeneratorUtil
import uuid


class GeneratorAgent:

    age_distribution = (45, 18)
    temperature_distribution = (36.6, 1)

    """Customers' parameters"""
    vip_probability = 0.12

    customer_pool = []
    path_length = (1, 20)

    def __init__(self, dao):
        self.dao = dao

    def generate_population(self, size):
        self.dao.initialise_customers_table()
        for i in range(0, size):
            biometric = self.generate_biometric()
            customer = self.generate_customer(index=i, biometric=biometric)
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

    @staticmethod
    def generate_service_time(dist):
        time = GeneratorUtil.generate_in_distribution(dist[0], dist[1], n=1)[0]
        if time < 0:
            return 0
        return int(time)

    @staticmethod
    def generate_next_nodetime(mu, sigma, offset, n=1):
        node_time = GeneratorUtil.generate_in_distribution(mu, sigma, n)[0]
        if node_time <= offset:
            return offset
        return int(node_time + offset)

    @classmethod
    def generate_path(cls, scene):
        nodes_index = [(0, 0)]
        path_length = GeneratorUtil.generate_integer_in_range(cls.path_length[0], cls.path_length[1])
        for i in range(path_length):
            current_node = nodes_index[i]
            if not scene.get_node(current_node).is_exit:
                neighbor = scene.get_random_neighbor_cords(current_node);
            nodes_index.append(neighbor)

        path_to_end = scene.generate_path_to_escape_node(nodes_index[-1])
        return nodes_index + path_to_end



    @staticmethod
    def get_next_appear_time(low, high, current_time):
        return GeneratorUtil.generate_integer_in_range(low + current_time, high + current_time + 1)


    @classmethod
    def generate_customer_data(cls):
        age_dist = cls.age_distribution
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

    @classmethod
    def generate_thermal_data(cls):
        dist = cls.temperature_distribution
        temp = GeneratorUtil.generate_in_distribution(dist[0], dist[1])[0]
        return {
            "temperature": temp
        }