# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tuples.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(798, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 800, 600))
        self.frame.setStyleSheet(u"background-color: rgb(160, 160, 160);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 171, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color:#E5E5E5;\n"
"color: #313132;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 90, 221, 391))
        self.frame_2.setStyleSheet(u"background-color: rgb(196, 196, 196);\n"
"border-radius: 5px;\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.create_button = QPushButton(self.frame_2)
        self.create_button.setObjectName(u"create_button")
        self.create_button.setGeometry(QRect(24, 10, 171, 31))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.create_button.setFont(font1)
        self.create_button.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"background-color: #E5E5E5;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius:5px;\n"
"background-color: #605e5e;\n"
"border: 1px solid black;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-radius:5px;\n"
"background-color: #ebc000;\n"
"border: 1px solid black;\n"
"color: black;\n"
"}")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 80, 91, 21))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"background-color:#E5E5E5;\n"
"color: #313132;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.clouds_combobox = QComboBox(self.frame_2)
        self.clouds_combobox.setObjectName(u"clouds_combobox")
        self.clouds_combobox.setGeometry(QRect(10, 110, 191, 22))
        self.clouds_combobox.setStyleSheet(u"background-color:#E5E5E5;\n"
"color: #313132;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 150, 91, 21))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background-color:#E5E5E5;\n"
"color: #313132;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.hosts_combobox = QComboBox(self.frame_2)
        self.hosts_combobox.setObjectName(u"hosts_combobox")
        self.hosts_combobox.setGeometry(QRect(10, 180, 191, 22))
        self.hosts_combobox.setStyleSheet(u"background-color:#E5E5E5;\n"
"color: #313132;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 220, 91, 21))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"background-color:#E5E5E5;\n"
"color: #313132;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.vms_combobox = QComboBox(self.frame_2)
        self.vms_combobox.setObjectName(u"vms_combobox")
        self.vms_combobox.setGeometry(QRect(10, 250, 191, 22))
        self.vms_combobox.setStyleSheet(u"background-color:#E5E5E5;\n"
"color: #313132;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 290, 91, 21))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"background-color:#E5E5E5;\n"
"color: #313132;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.process_combobox = QComboBox(self.frame_2)
        self.process_combobox.setObjectName(u"process_combobox")
        self.process_combobox.setGeometry(QRect(10, 320, 191, 22))
        self.process_combobox.setStyleSheet(u"background-color:#E5E5E5;\n"
"color: #313132;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.delete_button = QPushButton(self.frame_2)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(20, 350, 171, 31))
        self.delete_button.setFont(font1)
        self.delete_button.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"background-color: #FF0000;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius:5px;\n"
"background-color: #605e5e;\n"
"border: 1px solid black;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-radius:5px;\n"
"background-color: #ebc000;\n"
"border: 1px solid black;\n"
"color: black;\n"
"}")
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 0, 800, 20))
        self.label_18.setStyleSheet(u"background-color: #ebc000;")
        self.log = QTextEdit(self.frame)
        self.log.setObjectName(u"log")
        self.log.setGeometry(QRect(600, 30, 191, 561))
        self.log.setStyleSheet(u"background-color:#ffffff;\n"
"color: #313132;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(240, 90, 171, 321))
        self.frame_3.setStyleSheet(u"background-color: rgb(196, 196, 196);\n"
"border-radius: 5px;\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.open_process_button = QPushButton(self.frame_3)
        self.open_process_button.setObjectName(u"open_process_button")
        self.open_process_button.setGeometry(QRect(26, 280, 121, 31))
        self.open_process_button.setFont(font1)
        self.open_process_button.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"background-color: #E5E5E5;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius:5px;\n"
"background-color: #605e5e;\n"
"border: 1px solid black;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-radius:5px;\n"
"background-color: #ebc000;\n"
"border: 1px solid black;\n"
"color: black;\n"
"}")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 10, 91, 21))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"background-color:#E5E5E5;\n"
"color: #313132;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.p_clouds_combobox = QComboBox(self.frame_3)
        self.p_clouds_combobox.addItem("")
        self.p_clouds_combobox.setObjectName(u"p_clouds_combobox")
        self.p_clouds_combobox.setGeometry(QRect(10, 40, 151, 22))
        self.p_clouds_combobox.setStyleSheet(u"background-color:#E5E5E5;\n"
"color: #313132;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 80, 91, 21))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"background-color:#E5E5E5;\n"
"color: #313132;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.p_hosts_combobox = QComboBox(self.frame_3)
        self.p_hosts_combobox.setObjectName(u"p_hosts_combobox")
        self.p_hosts_combobox.setGeometry(QRect(10, 110, 151, 22))
        self.p_hosts_combobox.setStyleSheet(u"background-color:#E5E5E5;\n"
"color: #313132;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 150, 91, 21))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"background-color:#E5E5E5;\n"
"color: #313132;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.p_vms_combobox = QComboBox(self.frame_3)
        self.p_vms_combobox.setObjectName(u"p_vms_combobox")
        self.p_vms_combobox.setGeometry(QRect(10, 180, 151, 22))
        self.p_vms_combobox.setStyleSheet(u"background-color:#E5E5E5;\n"
"color: #313132;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 220, 91, 21))
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"background-color:#E5E5E5;\n"
"color: #313132;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.p_process_combobox = QComboBox(self.frame_3)
        self.p_process_combobox.setObjectName(u"p_process_combobox")
        self.p_process_combobox.setGeometry(QRect(10, 250, 151, 22))
        self.p_process_combobox.setStyleSheet(u"background-color:#E5E5E5;\n"
"color: #313132;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tuples Creator", None))
        self.create_button.setText(QCoreApplication.translate("MainWindow", u"Create Object", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Clouds", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Hosts", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"VMs", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"Delete Object", None))
        self.label_18.setText("")
        self.open_process_button.setText(QCoreApplication.translate("MainWindow", u"Open Process", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Clouds", None))
        self.p_clouds_combobox.setItemText(0, "")

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Hosts", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"VMs", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Process", None))
    # retranslateUi

