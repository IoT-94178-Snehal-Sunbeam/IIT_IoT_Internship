
import mysql.connector
import datetime

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_soilmoisture",
    use_pure = True
)

sensor_id= (input("Enter moisture to be updated : "))
moisture= (input("Enter new moisture : "))


query = f"update moisture SET moisture='{moisture}' where sensor_id='{sensor_id}';"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()

