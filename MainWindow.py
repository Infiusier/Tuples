# coding: utf-8
import argparse

from PySide2.QtCore import (QPropertyAnimation, QCoreApplication, QDate, QDateTime, QMetaObject,QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2 import QtWidgets, QtCore    
from PySide2.QtCore import *
from screen import Ui_MainWindow
from Application import *

class Object_Type():
    CLOUD = "CLOUD"
    HOST = "HOST"
    VM = "VM"
    PROCESS = "PROCESS"
    

class ProcessWindow(QWidget,QtCore.QObject):
    def __init__(self,process: Process):
        super().__init__()
        self.process = process
        self.setWindowTitle('%s Window' % self.process.name)
        
        mainLayout = QVBoxLayout()        
#------------------------------ Create widgets ----------------------------------------------
        self.destination_label = QLabel("Message Destination:")
        self.destination_combobox = QComboBox()
        
        self.message_label = QLabel("Message:")
        self.message_input = QLineEdit()
        
        self.send_button = QPushButton("Send")
        
        mainLayout.addWidget(self.destination_label)
        mainLayout.addWidget(self.destination_combobox)
        
        mainLayout.addWidget(self.message_label)
        mainLayout.addWidget(self.message_input)
        
        mainLayout.addWidget(self.send_button)
        
#------------------------- Configure Widgets -------------------------------------
        self.send_button.clicked.connect(self.send_callback)
        self.setLayout(mainLayout)
        
    def send_callback(self):
        self.process.send_message(self.message_input.text(),self.destination_combobox.currentText())
        self.message_input.clear()
        
    def display_window(self):
        self.show()
        
    def close_window(self):
        self.close()
    

class CreationWindow(QWidget,QtCore.QObject):
    create_signal=QtCore.Signal(object)
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Creation Window')
        
        mainLayout = QVBoxLayout()
        
#---------------------------- Return values ----------------------------------
        self.object_type = None
        self.object_name = None
        self.object_parent = None
#----------------------------- Variables ---------------------------------------        
        self.list_of_clouds = []
        self.list_of_hosts = []
        self.list_of_vms = []
        self.list_of_process = []

        self.active_combobox = None
#------------------------------ Create widgets ----------------------------------------------
        self.object_type_label = QLabel("Object Type:")
        self.object_type_combobox = QComboBox()
        
        self.object_name_label = QLabel("Object Name:")
        self.object_name_input = QLineEdit()
        
        self.object_parent_cloud_label = QLabel("Parent Cloud:")
        self.object_parent_cloud_combobox = QComboBox()
        
        self.object_parent_host_label = QLabel("Parent Host:")
        self.object_parent_host_combobox = QComboBox()
        
        self.object_parent_vm_label = QLabel("Parent VM:")
        self.object_parent_vm_combobox = QComboBox()
        
        self.create_object_button = QPushButton("Create")
        
        mainLayout.addWidget(self.object_type_label)
        mainLayout.addWidget(self.object_type_combobox)
        
        mainLayout.addWidget(self.object_name_label)
        mainLayout.addWidget(self.object_name_input)
        
        mainLayout.addWidget(self.object_parent_cloud_label)
        mainLayout.addWidget(self.object_parent_cloud_combobox)
        
        mainLayout.addWidget(self.object_parent_host_label)
        mainLayout.addWidget(self.object_parent_host_combobox)
        
        mainLayout.addWidget(self.object_parent_vm_label)
        mainLayout.addWidget(self.object_parent_vm_combobox)
        
        mainLayout.addWidget(self.create_object_button)
#------------------------ Hide Elements --------------------------------------
        self.object_parent_cloud_label.hide()
        self.object_parent_cloud_combobox.hide()
        
        self.object_parent_host_label.hide()
        self.object_parent_host_combobox.hide()
        
        self.object_parent_vm_label.hide()
        self.object_parent_vm_combobox.hide()
        
#------------------------- Configure Widgets -------------------------------------
        self.object_type_combobox.addItems(["",Object_Type.HOST,Object_Type.PROCESS,Object_Type.CLOUD,Object_Type.VM])
        self.object_type_combobox.currentTextChanged.connect(self.object_type_callback)
        self.create_object_button.clicked.connect(self.create_callback)
        self.setLayout(mainLayout)
        
        self.object_type_callback()
        
    def object_type_callback(self):
        self.object_type = self.object_type_combobox.currentText()
        
        self.object_parent_cloud_label.hide()
        self.object_parent_cloud_combobox.hide()
        self.object_parent_host_label.hide()
        self.object_parent_host_combobox.hide()
        self.object_parent_vm_label.hide()
        self.object_parent_vm_combobox.hide()
        
        self.active_combobox = None
        
        match self.object_type:
                
            case Object_Type.HOST:
                self.object_parent_cloud_label.show()
                self.object_parent_cloud_combobox.show()
                self.active_combobox = self.object_parent_cloud_combobox
                
            case Object_Type.VM:
                self.object_parent_host_label.show()
                self.object_parent_host_combobox.show()
                self.active_combobox = self.object_parent_host_combobox
                
            case Object_Type.PROCESS:
                self.object_parent_vm_label.show()
                self.object_parent_vm_combobox.show()
                self.active_combobox = self.object_parent_vm_combobox
        
    def create_callback(self):
        if self.object_type == "":
            print("Select object type!")
            return
        
        if self.object_type != Object_Type.CLOUD:
            if self.active_combobox.currentText() == "":
                print("Parent object is not set!")
                return
            
            self.object_parent = self.active_combobox.currentText()
            
        if len(self.object_name_input.text()) == 0:
            print("Enter object name!")
            return
        
        self.object_name = self.object_name_input.text()
        
        self.create_signal.emit(0)
        self.close_window()
    
            
    def update_info(self,**kwargs):
        for value in kwargs.keys():
            
            combobox = None
            if value == Object_Type.VM:
                self.list_of_vms = kwargs[value]
                combobox = self.object_parent_vm_combobox
                
            if value == Object_Type.HOST:
                self.list_of_hosts = kwargs[value]
                combobox = self.object_parent_host_combobox
                
            if value == Object_Type.PROCESS:
                self.list_of_process = kwargs[value]
                
            if value == Object_Type.CLOUD:
                self.list_of_clouds = kwargs[value]
                combobox = self.object_parent_cloud_combobox
                
            if combobox != None:
                for item in kwargs[value]:
                    combobox.addItem(item)
        
    def display_window(self):
        self.show()
        
    def close_window(self):
        self.close()

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow,QtCore.QObject):
    
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        
        self.list_of_clouds = []
        self.list_of_hosts = []
        self.list_of_vms = []
        self.list_of_process = []
        
        self.create_button.clicked.connect(self.launch_creation_window)
        self.open_process_button.clicked.connect(self.open_process_callback)
        self.p_clouds_combobox.currentIndexChanged.connect(self.p_clouds_combobox_callback)
        self.p_hosts_combobox.currentIndexChanged.connect(self.p_hosts_combobox_callback)
        self.p_vms_combobox.currentIndexChanged.connect(self.p_vms_combobox_callback)

#---------------------------------------------------CALLBACKS---------------------------------------------------
    def p_clouds_combobox_callback(self):
        if self.p_clouds_combobox.currentText() == "":
            return
        
        cloud_name = self.p_clouds_combobox.currentText()
        
        self.p_hosts_combobox.clear()
        self.p_vms_combobox.clear()
        self.p_process_combobox.clear()
        
        list_of_hosts = [host.name for host in self.list_of_hosts if host.parent_cloud.name == cloud_name]
        
        self.p_hosts_combobox.addItems(list_of_hosts)
        
    def p_hosts_combobox_callback(self):
        if self.p_hosts_combobox.currentText() == "":
            return
        
        host_name = self.p_hosts_combobox.currentText()
        
        self.p_vms_combobox.clear()
        self.p_process_combobox.clear()
        
        list_of_vms = [vm.name for vm in self.list_of_vms if vm.parent_host.name == host_name]
        
        self.p_vms_combobox.addItems(list_of_vms)
        
    def p_vms_combobox_callback(self):
        if self.p_vms_combobox.currentText() == "":
            return
        
        vm_name = self.p_vms_combobox.currentText()
        
        self.p_process_combobox.clear()
        
        list_of_process = [process.name for process in self.list_of_process if process.parent_vm.name == vm_name]
        
        self.p_process_combobox.addItems(list_of_process)
        
    def open_process_callback(self):
        if len(self.p_clouds_combobox.currentText()) == 0:
            return
        
        if len(self.p_hosts_combobox.currentText()) == 0:
            return
        
        if len(self.p_vms_combobox.currentText()) == 0:
            return
        
        if len(self.p_process_combobox.currentText()) == 0:
            return
        
    def create_callback(self):
        
        object_type = self.creation_window.object_type
        object_name = self.creation_window.object_name
        object_parent = self.creation_window.object_parent
        
        if self.check_if_name_exists_in_container(object_name,object_parent,object_type) == False:
            self.log.append("Name already exists in container!")
            return
        
        print("Object Type: %s" % self.creation_window.object_type)
        print("Object Name: %s" % self.creation_window.object_name)
        
        match object_type:
            case Object_Type.CLOUD:
                self.list_of_clouds.append(Cloud(object_name))
                
            case Object_Type.HOST:
                cloud_parent = [cloud for cloud in self.list_of_clouds if cloud.name == object_parent][0]
                host = Host(object_name,cloud_parent)
                cloud_parent.append(host)
                self.list_of_hosts.append(host)
                
            case Object_Type.VM:
                host_parent = [host for host in self.list_of_hosts if host.name == object_parent][0]
                vm = Vm(object_name,host_parent)
                host_parent.append(vm)
                self.list_of_vms.append(vm)
                
            case Object_Type.PROCESS:
                vm_parent = [vm for vm in self.list_of_vms if vm.name == object_parent][0]
                process = Process(object_name,vm_parent)
                vm_parent.append(process)
                process.run()
                self.list_of_process.append(process)
        
        self.update_open_process_comboboxes()
        
                
    def launch_creation_window(self):
        self.creation_window = CreationWindow()
        self.creation_window.create_signal.connect(self.create_callback)
        self.creation_window.update_info(CLOUD = [cloud.name for cloud in self.list_of_clouds],
                                         HOST = [host.name for host in self.list_of_hosts],
                                         VM = [vm.name for vm in self.list_of_vms],
                                         PROCESS = [process.name for process in self.list_of_process])
        self.creation_window.display_window()
#------------------------------------------------------ FUNCTIONS ----------------------------------------------------

    def update_open_process_comboboxes(self):
        self.p_clouds_combobox.clear()
        list_of_clouds = [cloud.name for cloud in self.list_of_clouds]
        self.p_clouds_combobox.addItems(list_of_clouds)
       
    def check_if_name_exists_in_container(self,object_name: str, object_parent: str,object_type: Object_Type):
        match object_type:
            case Object_Type.CLOUD:
                return False if object_name in [cloud.name for cloud in self.list_of_clouds] else True
                
            case Object_Type.HOST:
                list_of_hosts = [cloud for cloud in self.list_of_clouds if cloud.name == object_parent][0].list_of_hosts
                return False if object_name in [host.name for host in list_of_hosts] else True
                
            case Object_Type.VM:
                list_of_vms = [host for host in self.list_of_hosts if host.name == object_parent][0].list_of_vms
                return False if object_name in [vm.name for vm in list_of_vms] else True
                
            case Object_Type.PROCESS:
                list_of_process = [vm for vm in self.list_of_vms if vm.name == object_parent][0].list_of_process
                return False if object_name in [process.name for process in list_of_process] else True

    
    
    
        
#------------------------ GUI HANDLING -------------------------------------
        
            