import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)

value = input("Enter sensor value: ")

client.publish("health/pulse", value)
print("Value sent successfully")

client.disconnect()
