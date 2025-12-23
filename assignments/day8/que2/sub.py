import paho.mqtt.client as mqtt
import mysql.connector

pulse_value = None
spo2_value = None

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe("health/pulse")
    client.subscribe("health/spo2")
    client.subscribe("health/alert")

def on_message(client, userdata, message):
    global pulse_value, spo2_value

    topic = message.topic
    payload = message.payload.decode()
    print("Received:", topic, payload)

    if topic == "health/alert":
        print("Doctor Alert:", payload)
        return

    try:
        value = int(payload)
    except ValueError:
        print("Invalid payload:", payload)
        return

    if topic == "health/pulse":
        pulse_value = value
        print("Pulse =", pulse_value)

    elif topic == "health/spo2":
        spo2_value = value
        print("SpO2 =", spo2_value)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()
