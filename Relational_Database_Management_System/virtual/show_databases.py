import mysql.connector
from datetime import datetime
import uuid

cnx = mysql.connector.connect(user='root', 
    password='MyNewPass',
    host='127.0.0.1',
    database='',
    auth_plugin='mysql_native_password')

# create cursor
cursor = cnx.cursor()

#query
query = ("SHOW DATABASES")
cursor.execute(query)

for row in cursor.fetchasll():
    print(row)

#clean up
cursor.close()
cnx.close()