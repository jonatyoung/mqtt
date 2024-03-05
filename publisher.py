import paho.mqtt.client as mqtt
import random
import time

broker_adresses = "broker.hivemq.com"
username = "uname"
password = "pw"

topic = "jonathan/testing"

min = 20
max = 30

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected")
    else :
        print("connect returned result code: " + str(rc))

def on_message(client, userdata, msg):
    print("received message : " + msg.topic + " -> " + msg.payload.decode("utf-8"))

client = mqtt.Client()
client.on_message = on_message
client.on_connect = on_connect

client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set(username,password)
client.connect(broker_adresses, 8883)

wait = 20
while True:
    data = random.randint(min,max)
    print(data)
    client.publish(topic, data)
    time.sleep(wait)
