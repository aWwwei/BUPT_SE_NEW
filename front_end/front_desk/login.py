"""
@ 文件名：  login.py
@ 文件功能描述： 前台登录界面
@ 创建人：   田健豪
@ 创建日期： 2023年12月16日
"""
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login_window(object):
    def setupUi(self, login_window):
        login_window.setObjectName("login_window")
        login_window.resize(890, 1150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login_window.sizePolicy().hasHeightForWidth())
        login_window.setSizePolicy(sizePolicy)
        login_window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/前台/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login_window.setWindowIcon(icon)
        self.picture = QtWidgets.QLabel(login_window)
        self.picture.setGeometry(QtCore.QRect(0, 0, 890, 500))

        self.picture.setStyleSheet("image: url(:/前台/登录图标.png);")
        self.picture.setObjectName("picture")
        self.username_lable = QtWidgets.QLabel(login_window)
        self.username_lable.setGeometry(QtCore.QRect(245, 670, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.username_lable.setFont(font)
        self.username_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.username_lable.setObjectName("username_lable")
        self.password_lable = QtWidgets.QLabel(login_window)
        self.password_lable.setGeometry(QtCore.QRect(245, 810, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.password_lable.setFont(font)
        self.password_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.password_lable.setObjectName("password_lable")
        self.username_edit = QtWidgets.QLineEdit(login_window)
        self.username_edit.setGeometry(QtCore.QRect(245, 710, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.username_edit.setFont(font)
        self.username_edit.setObjectName("username_edit")
        self.password_edit = QtWidgets.QLineEdit(login_window)
        self.password_edit.setGeometry(QtCore.QRect(245, 850, 401, 51))
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.password_edit.setFont(font)
        self.password_edit.setObjectName("password_edit")
        self.login_button = QtWidgets.QPushButton(login_window)
        self.login_button.setGeometry(QtCore.QRect(245, 970, 401, 51))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.login_button.setStyleSheet("QPushButton{color:rgba(255,255,255,255);\
                                                background-color:rgba(28,186,28,255);border-radius:6px}\
                                                QPushButton:hover{background-color:rgba(32,208,32,255)}\
                                                QPushButton:pressed{background-color:rgba(22,148,22,255)}")
        self.welcome_lable = QtWidgets.QLabel(login_window)
        self.welcome_lable.setGeometry(QtCore.QRect(245, 540, 401, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.welcome_lable.setFont(font)
        self.welcome_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_lable.setObjectName("welcome_lable")

        self.retranslateUi(login_window)
        QtCore.QMetaObject.connectSlotsByName(login_window)

    def retranslateUi(self, login_window):
        _translate = QtCore.QCoreApplication.translate
        login_window.setWindowTitle(_translate("login_window", "Form"))
        self.picture.setText(_translate("login_window", ""))
        self.username_lable.setText(_translate("login_window", "Username"))
        self.password_lable.setText(_translate("login_window", "Password"))
        self.login_button.setText(_translate("login_window", "Login"))
        self.welcome_lable.setText(_translate("login_window", "Welcome!"))

import photo_rc
