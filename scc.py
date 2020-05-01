from PyQt5 import QtCore, QtGui, QtWidgets
from ui_scc import  Ui_MainWindow
import sys
import json
import socket
import requests
import configparser
import zmq
import time


class scc(Ui_MainWindow):
    def __init__( self ):
        super().__init__()

    def closeEvent(self, event):
        print("event")
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def setup(self):
        self.model = {"name" : "name", "level": "level", "created": 1, "message" : "msg"}
        self.tcpconnected = False
        self.zmqconnected = False

        self.config = configparser.ConfigParser()
        self.config.read('scc_conf.ini')

        self.lineEditHostTCP.setText(self.config['TCP']['HOST'])
        self.lineEditPortTCP.setText(self.config['TCP']['PORT'])
        self.checkBoxUseTCP.setChecked(self.config['TCP'].getboolean('USE'))
        self.lineEditHostZMQ.setText(self.config['ZMQ']['HOST'])
        self.lineEditPortZMQ.setText(self.config['ZMQ']['PORT'])
        self.checkBoxUseZMQ.setChecked(self.config['ZMQ'].getboolean('USE'))

        self.lineEditHostTCP.textChanged.connect(self.updateCfgTCP)
        self.lineEditPortTCP.textChanged.connect(self.updateCfgTCP)
        self.checkBoxUseTCP.stateChanged.connect(self.updateCfgTCP)

        self.lineEditHostZMQ.textChanged.connect(self.updateCfgZMQ)
        self.lineEditPortZMQ.textChanged.connect(self.updateCfgZMQ)
        self.checkBoxUseZMQ.stateChanged.connect(self.updateCfgZMQ)

        self.lineEditName.textChanged.connect(self.updatemsg)
        self.comboBoxMSGLevel.currentTextChanged.connect(self.updatemsg)
        self.lineEditMSGmessage.textChanged.connect(self.updatemsg)

        self.pushButtonSend.clicked.connect(self.send)

        #self.sendtimer = QtCore.QTimer(self)
        #self.sendtimer.start(2000)
        #self.sendtimer.timeout.connect(self.send) 

    def setupUi( self, Ui_Dialog ):
        super().setupUi( Ui_Dialog )
        self.setup()

    def close(self):
        if self.tcpconnected:
            self.tcpconnected = False
            self.tcpsocket.close()

        self.updateconfigfile()

    def updateCfgTCP(self):
        if self.tcpconnected:
            self.tcpsocket.close()
            self.tcpconnected = False

        self.config['TCP']['HOST'] = self.lineEditHostTCP.text()
        self.config['TCP']['PORT'] = self.lineEditPortTCP.text()
        self.config['TCP']['USE'] = str(bool(self.checkBoxUseTCP.checkState()))

    def updateCfgZMQ(self):
        if self.zmqconnected:
            self.zmqsocket.close()
            self.zmqcontext.destroy()
            self.zmqconnected = False
        self.config['ZMQ']['HOST'] = self.lineEditHostZMQ.text()
        self.config['ZMQ']['PORT'] = self.lineEditPortZMQ.text()
        self.config['ZMQ']['USE'] = str(bool(self.checkBoxUseZMQ.checkState()))
    
    def updatemsg(self):    
        self.model['name'] = self.lineEditName.text()
        self.model['level'] = self.comboBoxMSGLevel.currentText()
        self.model['created'] = self.lineEditMSGCreated.text()
        self.model['message'] = self.lineEditMSGmessage.text()

    def send(self):
        self.updatemsg()
        self.model['created'] = time.time()

        log = json.dumps(self.model)
        head = bytearray(len(log).to_bytes(4, 'big'))
        payload = bytearray(log, 'utf-8')
        arr = head + payload
        print("sending: " + str(arr))
        if self.checkBoxUseTCP.checkState():
            print("Sending TCP")
            if not self.tcpconnected:
                self.tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.tcpsocket.connect((self.config['TCP']['HOST'], int(self.config['TCP']['PORT'])))
                self.tcpconnected = True
            self.tcpsocket.send(arr)
            #self.tcpsocket.close()
            
        if self.checkBoxUseZMQ.checkState():
            print("Sending ZMQ")
            if not self.zmqconnected:
                self.zmqcontext = zmq.Context()
                self.zmqsocket = self.zmqcontext.socket(zmq.PUB)
                self.zmqsocket.connect("tcp://" + self.config['ZMQ']['HOST'] + ":" + self.config['ZMQ']['Port'])
                self.zmqconnected = True
                time.sleep(0.1)

            self.zmqsocket.send(arr)

    def updateconfigfile(self):
        with open('scc_conf.ini', 'w') as configfile:  
            self.config.write(configfile)