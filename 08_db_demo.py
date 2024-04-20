import mysql.connector
from utilities.configuration import *

# Parameter :- host, database, user, password
# conn = mysql.connector.connect(host="localhost", database="APIDevelop", user="root", password="Gspl$#dc3")
# print(conn.is_connected())

conn = get_connection()
cursor = conn.cursor()

cursor.execute("select * from CustomerInfo;")
# row = cursor.fetchone()  # Fetch first row from the table
# print(row)
# print("location :-", row[-1])
row_all = cursor.fetchall()  # Fetch all row details from the table
print(row_all)
# Question - to add all amount
amount = 0
for i in row_all:
    amount = i[2] + amount
print("Addition of all amount :-", amount)

query = "update customerInfo set Location = %s where CourseName = %s"
data = ('UK', 'Jmeter')
cursor.execute(query, data)
conn.commit()
conn.close()
