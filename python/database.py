import mysql.connector

conn = mysql.connector.connect(
    host="localhost", port=3306, user="root", password="jaswanth_23", database="db"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM employees")


for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
