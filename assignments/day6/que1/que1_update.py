
import mysql.connector
import datetime

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_data",
    use_pure = True
)

id=input("Enter temprature to be updated:")
temprature=input("Enter new temperature:")

query = f"update sensor_readings SET temprature='{temprature}' where id='{id}';"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()

