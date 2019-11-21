import mysql.connector
db_config = {
    "user": "root",
    "password": "",
    "db": "queue_simulation",
    "host": "127.0.0.1",
}

cnx = mysql.connector.connect(user=db_config["user"],
                                   password=db_config["password"],
                                   host=db_config["host"],
                                   database=db_config["db"])
cursor = cnx.cursor(buffered = True)

query = ("SELECT * FROM customers where id = 29")
cursor.execute(query)

for (id, biometric, customer_status, is_new) in cursor:
        print(id, biometric, customer_status, is_new)


cursor.close()
cnx.close()