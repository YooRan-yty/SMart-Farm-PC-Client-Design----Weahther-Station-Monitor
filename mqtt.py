import time
import paho.mqtt.client as mqtt_client
import json
import threading

class Mqtt(object):
    def __init__(self,host="  ",port=1883,keepalive=10,topic=" ",username=" ",password=" ",on_connect=None,on_message=None):
        self.client = mqtt_client.Client()
        self.client.username_pw_set(" "," ")
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.host = host
        self.port = port
        self.topic = topic
        self.keepalive = keepalive
        self.thread = None
        self.username  = username
        self.password  = password

    def start(self):      
        # time.sleep(1)
        self.client.connect(host=self.host,port=self.port,keepalive=self.keepalive)
        self.client.subscribe(topic=self.topic,qos=0)
        self.client.loop_forever()

    def start_thread(self):
        t = threading.Thread(target=Mqtt.start,args=(self,))
        self.thread = t
        t.setDaemon(True)
        t.start()

    def close(self):
        self.client.disconnect()






