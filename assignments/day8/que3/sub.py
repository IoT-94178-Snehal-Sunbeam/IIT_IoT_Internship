import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe("health/data")   # SAME topic as publisher

def on_message(client, userdata, message):
    print("Received from program:")
    print("Topic:", message.topic)
    print("Message:", message.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

print("Subscriber running...")
client.loop_forever()
