import mysql.connector
from Database.config import db_config


class CustomerDao:

    def __init__(self):
        self.cnx = mysql.connector.connect(user=db_config["user"],
                                           password=db_config["password"],
                                           host=db_config["host"],
                                           database=db_config["db"])
        self.cursor = self.cnx.cursor(buffered=True)

    """Setting up the environment"""
    def initialise_customers_table(self):
        query = "TRUNCATE TABLE customers;"
        self.cursor.execute(query)

    def save_customer(self, customer=None, customer_status = None, is_new=None):
        biometric = str(customer.biometric)
        customer_status = str(customer_status)
        is_new = bool(is_new)
        query = "INSERT INTO customers (biometric, customer_status, is_new) VALUES(%s, %s, %s);"
        self.cursor.execute(query, (biometric, customer_status, is_new))
        self.cnx.commit()

    def get_customer_by_biometric(self, biometric):
        query = "SELECT * FROM customers where biometric = '{}' LIMIT 1".format(biometric)
        self.cursor.execute(query)

        customer = self.cursor.fetchone()
        print(customer)

