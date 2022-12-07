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
        self.space.run()
        
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
    def __init__(self,name,parent_vm : Vm):
        self.parent_vm = parent_vm
        self.space = self.parent_vm.space
        self.name = name
        self.is_running = False
        self.window = None
        
    def run(self):
        print("Process %s running!" % self.name)

        self.is_running = True
        
        while self.is_running:
            message = yield self.space.in_((object, object))
            print(message) 
            
    def update_space(self,space):
        self.space = space
        
    def stop(self):
        self.is_running = False
             
    def send_message(self,message,id):
        print(message)
        yield self.space.timeout(1)
        yield self.space.out((id, message))
        
        
def main():
     
    cloud = Cloud("Cloud")
    host = Host("Host", cloud)
    vm = Vm("Vm", host)
    p1 = Process("P1", vm)
    p2 = Process("P2", vm)
    
    vm.append(p1)
    vm.append(p2)
    
    p2.send_message("TESTE", "P1")
    print("oi")

if __name__ == "__main__":
    main()