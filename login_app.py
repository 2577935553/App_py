# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login_MainWindow(object):
    def setupUi(self, Login_MainWindow):
        Login_MainWindow.setObjectName("Login_MainWindow")
        Login_MainWindow.resize(1122, 780)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Login_MainWindow.sizePolicy().hasHeightForWidth())
        Login_MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(Login_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(50, 50))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.verticalLayout.addWidget(self.widget)
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.widget_2 = QtWidgets.QWidget(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.horizontalLayout_10.addWidget(self.widget_2)
        self.widget_8 = QtWidgets.QWidget(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(15611561, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_7.addWidget(self.lineEdit_2)
        self.horizontalLayout_10.addWidget(self.widget_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.widget_7 = QtWidgets.QWidget(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.widget_7)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.horizontalLayout_11.addWidget(self.widget_7)
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(6156156, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_8.addWidget(self.lineEdit)
        self.horizontalLayout_11.addWidget(self.widget_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btn_SignUp = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_SignUp.sizePolicy().hasHeightForWidth())
        self.btn_SignUp.setSizePolicy(sizePolicy)
        self.btn_SignUp.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btn_SignUp.setObjectName("btn_SignUp")
        self.horizontalLayout_2.addWidget(self.btn_SignUp)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.widget_4)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        Login_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 23))
        self.menubar.setObjectName("menubar")
        Login_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login_MainWindow)
        self.statusbar.setObjectName("statusbar")
        Login_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Login_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Login_MainWindow)

    def retranslateUi(self, Login_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Login_MainWindow.setWindowTitle(_translate("Login_MainWindow", "MainWindow"))
        self.label_5.setText(_translate("Login_MainWindow", "??????"))
        self.label.setText(_translate("Login_MainWindow", "?????????"))
        self.label_2.setText(_translate("Login_MainWindow", "??????"))
        self.pushButton.setText(_translate("Login_MainWindow", "????????????"))
        self.label_6.setText(_translate("Login_MainWindow", "??????????????????"))
        self.btn_SignUp.setText(_translate("Login_MainWindow", "??????"))
