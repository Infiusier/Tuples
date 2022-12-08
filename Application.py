# coding: utf-8
import time,threading,os,json
from datetime import datetime
from queue import Queue
from enum import Enum,auto
import random

from PySide2 import QtCore

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
        self.space.run()
        process.run()
        
    def remove(self,process):
        self.list_of_process.remove(process)
        
    def run(self):
        print("Vm %s running!" % self.name)
        
    def stop(self):
        self.is_running = False
        
    def loop(self):
        self.is_running = True
        
        while self.is_running:
            #time.sleep(0.1)
            self.space.run()

class Process():
    class GUI_Controller(QtCore.QObject):
        log_signal=QtCore.Signal(object)
        
        def append_to_log(self,message: str):
            self.log_signal.emit(message)
    
    def __init__(self,name,parent_vm : Vm):
        self.parent_vm = parent_vm
        self.space = self.parent_vm.space
        self.name = name
        self.is_running = False
        self.window = None
        self.gui_controller = Process.GUI_Controller()
        
        
    def run(self):
        print("Process %s running!" % self.name)

        self.is_running = True
        
        while self.is_running:
            print("Waiting...")
            message = yield self.space.in_((self.name, dict))
            print(f"Message received: {message}")
            msg = f"Id: {message[1]['id']} --> {message[1]['payload']}"
            self.gui_controller.append_to_log(msg)
            
        print("Process %s has stopped!" % self.name)

    def update_space(self,space):
        self.space = space
        
    def stop(self):
        self.is_running = False
        self.send_message_callback({},self.name)
        
    def send_message_callback(self,message: dict,id: str):
        print(message)
        self.space.eval((self.name,self.send_message(message,id)))
        self.space.run()
          
    def send_message(self,message,id):
        msg = {}
        msg['id'] = self.name
        msg['payload'] = message
        yield self.space.timeout(1)
        yield self.space.out((id, msg))
        
        
def main():
     
    cloud = Cloud("Cloud")
    host = Host("Host", cloud)
    vm = Vm("Vm", host)
    p1 = Process("P1", vm)
    p2 = Process("P2", vm)
    
    vm.append(p1)
    vm.append(p2)
    
    p2.send_message_callback("hello there", "P1")
    print(vm.space.items)
    
    while 1:
        pass

if __name__ == "__main__":
    main()