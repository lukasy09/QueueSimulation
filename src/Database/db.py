import mysql.connector
from config import db_config

cnx = mysql.connector.connect(user=db_config["user"],
                              password=db_config["password"],
                              host=db_config["host"],
                              database=db_config["db"])


try:
   cursor = cnx.cursor()
   cursor.execute("""
      select * from customers
   """)
   result = cursor.fetchall()
   print (result)
finally:
    cnx.close()