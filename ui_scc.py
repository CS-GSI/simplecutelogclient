# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_scc.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(315, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 0, 301, 229))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelHostTCP = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.labelHostTCP.setObjectName("labelHostTCP")
        self.verticalLayout.addWidget(self.labelHostTCP)
        self.lineEditHostTCP = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEditHostTCP.setObjectName("lineEditHostTCP")
        self.verticalLayout.addWidget(self.lineEditHostTCP)
        self.labelHostZMQ = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.labelHostZMQ.setObjectName("labelHostZMQ")
        self.verticalLayout.addWidget(self.labelHostZMQ)
        self.lineEditHostZMQ = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEditHostZMQ.setObjectName("lineEditHostZMQ")
        self.verticalLayout.addWidget(self.lineEditHostZMQ)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelPortTCP = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.labelPortTCP.setObjectName("labelPortTCP")
        self.verticalLayout_2.addWidget(self.labelPortTCP)
        self.lineEditPortTCP = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEditPortTCP.setObjectName("lineEditPortTCP")
        self.verticalLayout_2.addWidget(self.lineEditPortTCP)
        self.labelPortZMQ = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.labelPortZMQ.setObjectName("labelPortZMQ")
        self.verticalLayout_2.addWidget(self.labelPortZMQ)
        self.lineEditPortZMQ = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEditPortZMQ.setObjectName("lineEditPortZMQ")
        self.verticalLayout_2.addWidget(self.lineEditPortZMQ)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.checkBoxUseTCP = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checkBoxUseTCP.setObjectName("checkBoxUseTCP")
        self.verticalLayout_3.addWidget(self.checkBoxUseTCP)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.checkBoxUseZMQ = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checkBoxUseZMQ.setObjectName("checkBoxUseZMQ")
        self.verticalLayout_3.addWidget(self.checkBoxUseZMQ)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelMSGName = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.labelMSGName.setObjectName("labelMSGName")
        self.verticalLayout_4.addWidget(self.labelMSGName)
        self.labelMSGLevel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.labelMSGLevel.setObjectName("labelMSGLevel")
        self.verticalLayout_4.addWidget(self.labelMSGLevel)
        self.labelMSGCreated = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.labelMSGCreated.setObjectName("labelMSGCreated")
        self.verticalLayout_4.addWidget(self.labelMSGCreated)
        self.labelMSGMessage = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.labelMSGMessage.setObjectName("labelMSGMessage")
        self.verticalLayout_4.addWidget(self.labelMSGMessage)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEditName = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEditName.setObjectName("lineEditName")
        self.verticalLayout_5.addWidget(self.lineEditName)
        self.comboBoxMSGLevel = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.comboBoxMSGLevel.setObjectName("comboBoxMSGLevel")
        self.comboBoxMSGLevel.addItem("")
        self.comboBoxMSGLevel.addItem("")
        self.comboBoxMSGLevel.addItem("")
        self.comboBoxMSGLevel.addItem("")
        self.comboBoxMSGLevel.addItem("")
        self.verticalLayout_5.addWidget(self.comboBoxMSGLevel)
        self.lineEditMSGCreated = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEditMSGCreated.setEnabled(False)
        self.lineEditMSGCreated.setObjectName("lineEditMSGCreated")
        self.verticalLayout_5.addWidget(self.lineEditMSGCreated)
        self.lineEditMSGmessage = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEditMSGmessage.setObjectName("lineEditMSGmessage")
        self.verticalLayout_5.addWidget(self.lineEditMSGmessage)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButtonSend = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.verticalLayout_7.addWidget(self.pushButtonSend)
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelHostTCP.setText(_translate("MainWindow", "Host / IP of TCP Socket"))
        self.lineEditHostTCP.setText(_translate("MainWindow", "127.0.0.1"))
        self.labelHostZMQ.setText(_translate("MainWindow", "Host / IP of ZMQ SUB Socket"))
        self.lineEditHostZMQ.setText(_translate("MainWindow", "127.0.0.1"))
        self.labelPortTCP.setText(_translate("MainWindow", "Port TCP"))
        self.lineEditPortTCP.setText(_translate("MainWindow", "19996"))
        self.labelPortZMQ.setText(_translate("MainWindow", "Port ZMQ"))
        self.lineEditPortZMQ.setText(_translate("MainWindow", "19997"))
        self.checkBoxUseTCP.setText(_translate("MainWindow", "Use TCP"))
        self.checkBoxUseZMQ.setText(_translate("MainWindow", "Use ZMQ PUB"))
        self.labelMSGName.setText(_translate("MainWindow", "Name"))
        self.labelMSGLevel.setText(_translate("MainWindow", "Level"))
        self.labelMSGCreated.setText(_translate("MainWindow", "Created"))
        self.labelMSGMessage.setText(_translate("MainWindow", "Message"))
        self.lineEditName.setText(_translate("MainWindow", "Name"))
        self.comboBoxMSGLevel.setItemText(0, _translate("MainWindow", "DEBUG"))
        self.comboBoxMSGLevel.setItemText(1, _translate("MainWindow", "INFO"))
        self.comboBoxMSGLevel.setItemText(2, _translate("MainWindow", "WARNING"))
        self.comboBoxMSGLevel.setItemText(3, _translate("MainWindow", "ERROR"))
        self.comboBoxMSGLevel.setItemText(4, _translate("MainWindow", "CRITICAL"))
        self.lineEditMSGCreated.setText(_translate("MainWindow", "19996"))
        self.lineEditMSGmessage.setText(_translate("MainWindow", "Message"))
        self.pushButtonSend.setText(_translate("MainWindow", "Send"))
