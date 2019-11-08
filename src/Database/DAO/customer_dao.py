from Database.config import db_config
import mysql.connector


class CustomerDao:

    def __init__(self):
        self.cnx = mysql.connector.connect(user=db_config["user"],
                                           password=db_config["password"],
                                           host=db_config["host"],
                                           database=db_config["db"])
        self.cursor = self.cnx.cursor()

    """"""
    def initialise_customers_table(self):
        query = "TRUNCATE TABLE customers;"
        self.cursor.execute(query)

    def save_customer(self, customer=None):
        biometric = str(customer.biometric)
        status = customer.customer_status
        query = "INSERT INTO customers (biometric, customer_status) VALUES(%s, %s);"
        self.cursor.execute(query, (biometric, status))
        self.cnx.commit()