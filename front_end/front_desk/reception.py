"""
@ 文件名：reception.py
@ 文件功能描述：前台界面显示
@ 创建人：孟祥超
@ 创建日期：2023年12月8日

@ 修改描述：界面美化：调整字体、背景色和美化按钮样式等
@ 修改人：孟祥超、杨欣悦
@ 修改日期：2023年12月13日

@ 修改描述：固定显示界面窗口大小
@ 修改人：孟祥超
@ 修改日期：2023年12月14日

"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(981, 547)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/前台/图标.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(230, 245, 255);")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(150, 200, 801, 291))
        self.tableView.setObjectName("tableView")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 230, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.room_id = QtWidgets.QLineEdit(Form)
        self.room_id.setGeometry(QtCore.QRect(30, 280, 91, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.room_id.setFont(font)
        self.room_id.setTabletTracking(False)
        self.room_id.setClearButtonEnabled(False)
        self.room_id.setObjectName("room_id")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 360, 101, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    font: 12pt \"黑体\";\n"
"    background-color: rgb(129, 211, 255);\n"
"\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"   \n"
"}\n"
"QPushButton:hover {\n"
"\n"
"border:2px outset rgba(36, 36, 36,0);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"border:4px outset rgba(36, 36, 36,0);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 430, 101, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    font: 12pt \"黑体\";\n"
"    background-color: rgb(129, 211, 255);\n"
"\n"
"    border-radius: 10px;\n"
"       color: white;\n"
"}\n"
"QPushButton:hover {\n"
"\n"
"border:2px outset rgba(36, 36, 36,0);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"border:4px outset rgba(36, 36, 36,0);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(530, 70, 72, 15))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../15201/Desktop/图片空调/示例1.png"))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(320, 30, 421, 171))
        self.label_3.setStyleSheet("image: url(:/前台/空调.png);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../../15201/Desktop/图片空调/大空调new.jpg"))
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(60, 40, 181, 141))
        self.frame_2.setStyleSheet("image: url(:/前台/前台2.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.tableView.raise_()
        self.room_id.raise_()
        self.frame_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">房间号：</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "输出账单"))
        self.pushButton_2.setText(_translate("Form", "输出详单"))

import photo_rc
