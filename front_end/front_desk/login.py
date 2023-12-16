from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon



class Ui_login_window(object):
    def setupUi(self, login_window):
        login_window.setObjectName("login_window")
        login_window.setFixedSize(QtCore.QSize(890, 1150))
        self.picture = QtWidgets.QLabel(login_window)
        self.picture.setGeometry(QtCore.QRect(0, 0, 890, 500))
        self.picture.setObjectName("picture")

        pix = QPixmap('login.jpg')
        self.picture.setPixmap(pix)
        self.picture.setScaledContents(True)

        self.username_lable = QtWidgets.QLabel(login_window)
        self.username_lable.setGeometry(QtCore.QRect(245, 670, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.username_lable.setFont(font)
        self.username_lable.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.username_lable.setObjectName("username_lable")
        self.password_lable = QtWidgets.QLabel(login_window)
        self.password_lable.setGeometry(QtCore.QRect(245, 810, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.password_lable.setFont(font)
        self.password_lable.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
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
        self.password_edit.setClearButtonEnabled(True)
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
        self.login_button.setStyleSheet("QPushButton{color:rgb(255,255,255,255);\
                                        background-color:rgb(28,186,28,255);border-radius:6px}\
                                        QPushButton:hover{background-color:rgb(32,208,32,255)}\
                                        QPushButton:pressed{background-color:rgb(22,148,22,255)}")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
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
        login_window.setWindowTitle(_translate("login_window", "登录"))
        self.username_lable.setText(_translate("login_window", "Username"))
        self.password_lable.setText(_translate("login_window", "Password"))
        self.login_button.setText(_translate("login_window", "Login"))
        self.welcome_lable.setText(_translate("login_window", "Welcome!"))
        login_window.setWindowIcon(QIcon('Logo.webp'))



