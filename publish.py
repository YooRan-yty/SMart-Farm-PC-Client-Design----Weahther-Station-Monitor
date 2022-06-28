import paho.mqtt.client as mqtt
import time
import json

def on_connect(client, userdata, flags, rc):
	print("Connected with result code: " + str(rc))
	client.subscribe(" ")

def on_message(client, userdata, msg):
	print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.username_pw_set(" "," ")
client.on_connect = on_connect
client.on_message = on_message

client.connect(host=" ",port=1883,keepalive=10)
time.sleep(1)
msg = [
	{"messageClass": "sensorData", "deviceID": "3010", "typeID": "106", "windspeed": 0.0, "voletage": 3.74, "timestamp": "2021-06-18 17:00:45"},
	{"messageClass":"sensorData","deviceID":"8011","typeID":"103","pm2.5":157.37,"voletage":3.548,"timestamp":"2021-06-18 16:59:31"},
	{"messageClass":"sensorData","deviceID":"4011","typeID":"107","winddirection":9.0,"voletage":3.792,"timestamp":"2021-06-18 16:59:05"},
	{"messageClass":"sensorData","deviceID":"7010","typeID":"108","rainsnow":5.0,"voletage":3.777,"timestamp":"2021-06-18 16:43:47"},
	{"messageClass":"sensorData","deviceID":"2012","typeID":"101","temperature":38,"humidity":59.54,"voletage":3.798,"timestamp":"2021-06-18 16:57:55"},
{"messageClass": "sensorData", "deviceID": "3010", "typeID": "106", "windspeed": 12.0, "voletage": 3.74, "timestamp": "2021-06-18 17:00:45"},
	{"messageClass":"sensorData","deviceID":"8011","typeID":"103","pm2.5":100.37,"voletage":3.548,"timestamp":"2021-06-18 16:59:31"},
	{"messageClass":"sensorData","deviceID":"4011","typeID":"107","winddirection":90.0,"voletage":3.792,"timestamp":"2021-06-18 16:59:05"},
	{"messageClass":"sensorData","deviceID":"7010","typeID":"108","rainsnow":10.0,"voletage":3.777,"timestamp":"2021-06-18 16:43:47"},
	{"messageClass":"sensorData","deviceID":"2012","typeID":"101","temperature":7.2,"humidity":59.54,"voletage":3.798,"timestamp":"2021-06-18 16:57:55"},
{"messageClass": "sensorData", "deviceID": "3010", "typeID": "106", "windspeed": 8.0, "voletage": 3.74, "timestamp": "2021-06-18 17:00:45"},
	{"messageClass":"sensorData","deviceID":"8011","typeID":"103","pm2.5":50.37,"voletage":3.548,"timestamp":"2021-06-18 16:59:31"},
	{"messageClass":"sensorData","deviceID":"4011","typeID":"107","winddirection":180.0,"voletage":3.792,"timestamp":"2021-06-18 16:59:05"},
	{"messageClass":"sensorData","deviceID":"7010","typeID":"108","rainsnow":15.0,"voletage":3.777,"timestamp":"2021-06-18 16:43:47"},
	{"messageClass":"sensorData","deviceID":"2012","typeID":"101","temperature":27.99,"humidity":59.54,"voletage":3.798,"timestamp":"2021-06-18 16:57:55"},
]

index = 0
while True:
	time.sleep(1)
	print('发送一条消息:')
	client.publish("testtopic/1", payload=json.dumps(msg[int(index % 15)]), qos=0)
	index += 1

