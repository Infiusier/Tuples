# coding: utf-8
import time,threading,os,json
from datetime import datetime
from queue import Queue
from enum import Enum,auto
import random

import linsimpy

class Cloud():
    def __init__(self,name):
        self.list_of_hosts = []
        self.name = name
        
    def append(self,host):
        self.list_of_hosts.append(host)
        
    def remove(self,host):
        if len(host.list_of_vms) != 0:
            print("Cant remove Host because it still have Vms running!")
            return False
        self.list_of_hosts.remove(host)

class Host():
    def __init__(self,name,parent_cloud : Cloud):
        self.list_of_vms = []
        self.parent_cloud = parent_cloud
        self.name = name
        
    def append(self,vm):
        self.list_of_vms.append(vm)
        
    def remove(self,vm):
        if len(vm.list_of_process) != 0:
            print("Cant remove VM because it still have process running!")
            return False
        self.list_of_vms.remove(vm)

class Vm():
    def __init__(self,name,parent_host : Host):
        self.list_of_process = []
        self.parent_host = parent_host
        self.space = linsimpy.TupleSpaceEnvironment()
        self.is_running = False
        self.name = name
        self.run()
        
    def append(self,process):
        self.list_of_process.append(process)
        self.space.eval((process.name,process.run()))
        
    def remove(self,process):
        self.list_of_process.remove(process)
        
    def run(self):
        print("Vm %s running!" % self.name)
        t = threading.Thread(target = self.loop,args=())
        t.start()
        
    def stop(self):
        self.is_running = False
        
    def loop(self):
        self.is_running = True
        
        while self.is_running:
            time.sleep(0.1)
            self.space.run()

class Process():
    def __init__(self,name,parent_vm : Vm):
        self.parent_vm = parent_vm
        self.space = self.parent_vm.space
        self.name = name
        self.is_running = False
        
    def run(self):
        print("Process %s running!" % self.name)

        self.is_running = True
        
        while self.is_running:
            message = yield self.space.in_((self.name, str))
            print(message) 
            
    def update_space(self,space):
        self.space = space
        
    def stop(self):
        self.is_running = False
             
    def send_message(self,message,id):
        yield self.space.out((id, message))

class Application():
    
    def __init__(self,sensor_type,sensor_name,current_value,max_value,min_value,discover_topic,topic,mqtt_broker,mqtt_port):
        super(Application,self).__init__()
        
        self.sensor_type = sensor_type
        self.sensor_name = sensor_name
        self.current_value = current_value
        self.max_value = max_value
        self.min_value = min_value
        
        self.discover_topic = discover_topic
        self.topic = topic
        
        self.mqtt_broker = mqtt_broker
        self.mqtt_port = mqtt_port
        
        client_id = f'MoM-{random.randint(0, 10000)}'
        username = ''
        password = ''
        
        self.mqtt = Mqtt(client_id, username, password, self.mqtt_broker, self.mqtt_port)
        #self.mqtt.loop_forever()
        
        
    def start(self):
        thread = threading.Thread(target=self.run,args=())
        thread.start()
        
    def run(self):
        '''Função que roda o loop principal'''
        self.stop=False

        while self.stop == False:
            delay = random.randint(1,5)
            time.sleep(delay)
            
            self.send_discover_signal()
            self.send_current_value()
            
        print("Stopping")
            
    def send_discover_signal(self):
        json_payload = {}
        json_payload["sensor_type"] = self.sensor_type
        json_payload["sensor_name"] = self.sensor_name
        
        str_payload = "{}".format(json_payload)
        
        self.mqtt.publish(self.discover_topic,str_payload)
    
    def send_current_value(self):
        
        if not (self.current_value > self.max_value or self.current_value < self.min_value):
            return
        
        if self.current_value > self.max_value:
            warning_msg = "Sensor beyond threshold!"
            
        elif self.current_value < self.min_value:
            warning_msg = "Sensor bellow threshold!"    
        
        json_payload = {}
        json_payload["sensor_name"] = self.sensor_name
        json_payload["sensor_type"] = self.sensor_type
        json_payload["sensor_value"] = self.current_value
        json_payload["warning"] = warning_msg
        
        str_payload = "{}".format(json_payload)
        
        self.mqtt.publish(self.topic,str_payload)
        
        