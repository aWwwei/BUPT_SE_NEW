'''
@文件名：controller.py
@文件功能描述：用户界面：可以调节空调的开关状态、目标温度、风速；实时数据面板可以查看当前温度、当前费用及总费用
@创建日期：2023年12月15日
@创建人：杨欣悦

@ 修改描述：增加图标
@ 修改人：杨欣悦
@ 修改日期：2023年12月15日

@ 修改描述：修改拼写错误
@ 修改人：田健豪
@ 修改日期：2023年12月15日
'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controller.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Client(object):
    def setupUi(self, Client):
        Client.setObjectName("Client")
        Client.resize(440, 360)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Client.sizePolicy().hasHeightForWidth())
        Client.setSizePolicy(sizePolicy)
        Client.setMinimumSize(QtCore.QSize(440, 360))
        Client.setMaximumSize(QtCore.QSize(440, 360))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        Client.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/用户界面/用户界面.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/用户界面/用户界面.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Client.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(Client)
        self.frame.setGeometry(QtCore.QRect(0, 0, 440, 360))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(440, 360))
        self.frame.setMaximumSize(QtCore.QSize(440, 360))
        self.frame.setStyleSheet("background-color: rgb(237, 252, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(30, 30, 380, 300))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(380, 300))
        self.frame_2.setMaximumSize(QtCore.QSize(380, 300))
        self.frame_2.setStyleSheet("    background-color: rgb(234, 245, 255);\n"
"border-radius:15px ")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("#frame_3{\n"
"    background-color: rgb(234, 245, 255);\n"
"    background-color: rgb(234, 245, 255);\n"
"\n"
"    border-radius: 10px;\n"
"    border: 1px solid #cccccc;\n"
"\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_switch = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_switch.setGeometry(QtCore.QRect(250, 10, 91, 31))
        self.pushButton_switch.setStyleSheet("\n"
"QPushButton{\n"
"    font: 12pt \"黑体\";\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    \n"
"    \n"
"    border-radius: 10px;\n"
"\n"
"   \n"
"}\n"
"QPushButton:hover {\n"
"\n"
"border:2px outset rgba(36, 36, 36,0);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"border:4px outset rgba(36, 36, 36,0);\n"
"}\n"
"\n"
"")
        self.pushButton_switch.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/管理员界面/关机.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/管理员界面/开机.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_switch.setIcon(icon1)
        self.pushButton_switch.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_switch.setCheckable(True)
        self.pushButton_switch.setObjectName("pushButton_switch")
        self.widget = QtWidgets.QWidget(self.frame_3)
        self.widget.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.widget.setStyleSheet("image: url(:/用户界面/人.png);\n"
"background-color: rgb(234, 245, 255);\n"
"")
        self.widget.setObjectName("widget")
        self.label_RoomName = QtWidgets.QLabel(self.frame_3)
        self.label_RoomName.setGeometry(QtCore.QRect(50, 15, 61, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_RoomName.setFont(font)
        self.label_RoomName.setStyleSheet("\n"
"    background-color: rgb(234, 245, 255);")
        self.label_RoomName.setObjectName("label_RoomName")
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet("#frame_4{\n"
"    background-color: rgb(234, 245, 255);\n"
"\n"
"    border-radius: 10px;\n"
"    border: 1px solid #cccccc;\n"
"\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(20, 1, 51, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(234, 245, 255);")
        self.label.setObjectName("label")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 30, 341, 71))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_5 = QtWidgets.QFrame(self.layoutWidget_2)
        self.frame_5.setStyleSheet("\n"
"#frame_5{\n"
"\n"
"border:1px solid black;\n"
"border-radius:25px;\n"
"    background-color: rgb(234, 245, 255);\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 54, 31))
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 75 9pt \"微软雅黑\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_current_tem = QtWidgets.QLabel(self.frame_5)
        self.label_current_tem.setGeometry(QtCore.QRect(19, 27, 55, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_current_tem.setFont(font)
        self.label_current_tem.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_current_tem.setObjectName("label_current_tem")
        self.label_12 = QtWidgets.QLabel(self.frame_5)
        self.label_12.setGeometry(QtCore.QRect(78, 27, 31, 41))
        self.label_12.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.layoutWidget_2)
        self.frame_6.setStyleSheet("#frame_6{\n"
"border:1px solid black;\n"
"border-radius:25px;\n"
"    background-color: rgb(234, 245, 255);\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setGeometry(QtCore.QRect(10, 1, 54, 31))
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 75 9pt \"微软雅黑\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_current_fee = QtWidgets.QLabel(self.frame_6)
        self.label_current_fee.setGeometry(QtCore.QRect(21, 31, 76, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_current_fee.setFont(font)
        self.label_current_fee.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_current_fee.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_current_fee.setObjectName("label_current_fee")
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        self.label_13.setGeometry(QtCore.QRect(81, 27, 31, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.layoutWidget_2)
        self.frame_7.setStyleSheet("#frame_7{\n"
"border:1px solid black;\n"
"border-radius:25px;\n"
"    background-color: rgb(234, 245, 255);\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setGeometry(QtCore.QRect(10, 2, 54, 31))
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 75 9pt \"微软雅黑\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_Total_fee = QtWidgets.QLabel(self.frame_7)
        self.label_Total_fee.setGeometry(QtCore.QRect(21, 32, 85, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Total_fee.setFont(font)
        self.label_Total_fee.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_Total_fee.setObjectName("label_Total_fee")
        self.label_14 = QtWidgets.QLabel(self.frame_7)
        self.label_14.setGeometry(QtCore.QRect(78, 27, 31, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_8 = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setStyleSheet("#frame_8{\n"
"    background-color: rgb(234, 245, 255);\n"
"\n"
"    border-radius: 10px;\n"
"    border: 1px solid #cccccc;\n"
"\n"
"}\n"
"\n"
"")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.layoutWidget_3 = QtWidgets.QWidget(self.frame_8)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 10, 341, 91))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_9 = QtWidgets.QFrame(self.layoutWidget_3)
        self.frame_9.setStyleSheet("    background-color: rgb(234, 245, 255);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.pushButton_down = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_down.setGeometry(QtCore.QRect(15, 45, 30, 30))
        self.pushButton_down.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    font: 12pt \"黑体\";\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    \n"
"    \n"
"    border-radius: 10px;\n"
"image: url(:/管理员界面/向左.png);\n"
"   \n"
"}\n"
"QPushButton:hover {\n"
"\n"
"border:2px outset rgba(36, 36, 36,0);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"border:4px outset rgba(36, 36, 36,0);\n"
"}\n"
"")
        self.pushButton_down.setText("")
        self.pushButton_down.setObjectName("pushButton_down")
        self.pushButton_up = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_up.setGeometry(QtCore.QRect(65, 45, 30, 30))
        self.pushButton_up.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    font: 12pt \"黑体\";\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    \n"
"    \n"
"    border-radius: 10px;\n"
"image: url(:/管理员界面/向右.png);\n"
"   \n"
"}\n"
"QPushButton:hover {\n"
"\n"
"border:2px outset rgba(36, 36, 36,0);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"border:4px outset rgba(36, 36, 36,0);\n"
"}\n"
"")
        self.pushButton_up.setText("")
        self.pushButton_up.setObjectName("pushButton_up")
        self.layoutWidget_4 = QtWidgets.QWidget(self.frame_9)
        self.layoutWidget_4.setGeometry(QtCore.QRect(5, 5, 103, 31))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(61, 28))
        self.textBrowser.setMaximumSize(QtCore.QSize(61, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(234, 245, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_3.addWidget(self.textBrowser)
        self.textBrowser_target_tem = QtWidgets.QTextBrowser(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_target_tem.sizePolicy().hasHeightForWidth())
        self.textBrowser_target_tem.setSizePolicy(sizePolicy)
        self.textBrowser_target_tem.setMinimumSize(QtCore.QSize(40, 28))
        self.textBrowser_target_tem.setMaximumSize(QtCore.QSize(40, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser_target_tem.setFont(font)
        self.textBrowser_target_tem.setStyleSheet("background-color: rgb(234, 245, 255);")
        self.textBrowser_target_tem.setReadOnly(False)
        self.textBrowser_target_tem.setObjectName("textBrowser_target_tem")
        self.horizontalLayout_3.addWidget(self.textBrowser_target_tem)
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.layoutWidget_3)
        self.frame_10.setStyleSheet("    background-color: rgb(234, 245, 255);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.layoutWidget_5 = QtWidgets.QWidget(self.frame_10)
        self.layoutWidget_5.setGeometry(QtCore.QRect(15, 5, 82, 31))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_3.sizePolicy().hasHeightForWidth())
        self.textBrowser_3.setSizePolicy(sizePolicy)
        self.textBrowser_3.setMinimumSize(QtCore.QSize(40, 28))
        self.textBrowser_3.setMaximumSize(QtCore.QSize(40, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setStyleSheet("background-color: rgb(234, 245, 255);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.horizontalLayout_4.addWidget(self.textBrowser_3)
        self.textBrowser_mode = QtWidgets.QTextBrowser(self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_mode.sizePolicy().hasHeightForWidth())
        self.textBrowser_mode.setSizePolicy(sizePolicy)
        self.textBrowser_mode.setMinimumSize(QtCore.QSize(40, 28))
        self.textBrowser_mode.setMaximumSize(QtCore.QSize(40, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser_mode.setFont(font)
        self.textBrowser_mode.setStyleSheet("    background-color: rgb(234, 245, 255);")
        self.textBrowser_mode.setReadOnly(False)
        self.textBrowser_mode.setObjectName("textBrowser_mode")
        self.horizontalLayout_4.addWidget(self.textBrowser_mode)
        self.pushButton_check = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_check.setGeometry(QtCore.QRect(40, 45, 30, 30))
        self.pushButton_check.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    font: 12pt \"黑体\";\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    \n"
"    \n"
"    border-radius: 10px;\n"
"image: url(:/用户界面/对勾.png);\n"
"   \n"
"}\n"
"QPushButton:hover {\n"
"\n"
"border:2px outset rgba(36, 36, 36,0);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"border:4px outset rgba(36, 36, 36,0);\n"
"}\n"
"")
        self.pushButton_check.setText("")
        self.pushButton_check.setObjectName("pushButton_check")
        self.horizontalLayout_2.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.layoutWidget_3)
        self.frame_11.setStyleSheet("    background-color: rgb(234, 245, 255);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.pushButton_low = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_low.setGeometry(QtCore.QRect(10, 50, 21, 23))
        self.pushButton_low.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    font: 12pt \"黑体\";\n"
"    \n"
"    background-color: rgba(255, 255, 255,0);\n"
"image: url(:/用户界面/低风速.png);\n"
"    border-radius: 10px;\n"
"\n"
"   \n"
"}\n"
"QPushButton:hover {\n"
"\n"
"border:2px outset rgba(36, 36, 36,0);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"border:4px outset rgba(36, 36, 36,0);\n"
"}\n"
"")
        self.pushButton_low.setText("")
        self.pushButton_low.setObjectName("pushButton_low")
        self.pushButton_mid = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_mid.setGeometry(QtCore.QRect(50, 50, 21, 23))
        self.pushButton_mid.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    font: 12pt \"黑体\";\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    image: url(:/用户界面/中风速.png);\n"
"    border-radius: 10px;\n"
"\n"
"   \n"
"}\n"
"QPushButton:hover {\n"
"\n"
"border:2px outset rgba(36, 36, 36,0);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"border:4px outset rgba(36, 36, 36,0);\n"
"}\n"
"")
        self.pushButton_mid.setText("")
        self.pushButton_mid.setObjectName("pushButton_mid")
        self.pushButton_high = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_high.setGeometry(QtCore.QRect(90, 50, 21, 23))
        self.pushButton_high.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    font: 12pt \"黑体\";\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    image: url(:/用户界面/高风速.png);\n"
"    border-radius: 10px;\n"
"\n"
"   \n"
"}\n"
"QPushButton:hover {\n"
"\n"
"border:2px outset rgba(36, 36, 36,0);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"border:4px outset rgba(36, 36, 36,0);\n"
"}\n"
"")
        self.pushButton_high.setText("")
        self.pushButton_high.setObjectName("pushButton_high")
        self.layoutWidget_6 = QtWidgets.QWidget(self.frame_11)
        self.layoutWidget_6.setGeometry(QtCore.QRect(20, 5, 82, 31))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_5.sizePolicy().hasHeightForWidth())
        self.textBrowser_5.setSizePolicy(sizePolicy)
        self.textBrowser_5.setMinimumSize(QtCore.QSize(40, 28))
        self.textBrowser_5.setMaximumSize(QtCore.QSize(40, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setStyleSheet("background-color: rgb(234, 245, 255);")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.horizontalLayout_5.addWidget(self.textBrowser_5)
        self.textBrowser_speed = QtWidgets.QTextBrowser(self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_speed.sizePolicy().hasHeightForWidth())
        self.textBrowser_speed.setSizePolicy(sizePolicy)
        self.textBrowser_speed.setMinimumSize(QtCore.QSize(40, 28))
        self.textBrowser_speed.setMaximumSize(QtCore.QSize(40, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser_speed.setFont(font)
        self.textBrowser_speed.setStyleSheet("background-color: rgb(234, 245, 255);")
        self.textBrowser_speed.setReadOnly(False)
        self.textBrowser_speed.setObjectName("textBrowser_speed")
        self.horizontalLayout_5.addWidget(self.textBrowser_speed)
        self.horizontalLayout_2.addWidget(self.frame_11)
        self.verticalLayout.addWidget(self.frame_8)

        self.retranslateUi(Client)
        QtCore.QMetaObject.connectSlotsByName(Client)

    def retranslateUi(self, Client):
        _translate = QtCore.QCoreApplication.translate
        Client.setWindowTitle(_translate("Client", "user interface"))
        self.label_RoomName.setText(_translate("Client", "<html><head/><body><p><span style=\" font-weight:600;\">ROOM1</span></p></body></html>"))
        self.label.setText(_translate("Client", "<html><head/><body><p><span style=\" font-weight:600; color:#141414;\">实时数据</span></p></body></html>"))
        self.label_2.setText(_translate("Client", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:400; color:#4a4a4a;\">当前温度</span></p></body></html>"))
        self.label_current_tem.setText(_translate("Client", "<html><head/><body><p><span style=\" font-weight:600;\">30.00</span></p></body></html>"))
        self.label_12.setText(_translate("Client", "℃"))
        self.label_3.setText(_translate("Client", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:400; color:#4a4a4a;\">当前费用</span></p></body></html>"))
        self.label_current_fee.setText(_translate("Client", "<html><head/><body><p>0.00</p></body></html>"))
        self.label_13.setText(_translate("Client", "<html><head/><body><p>元</p></body></html>"))
        self.label_4.setText(_translate("Client", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:400; color:#4a4a4a;\">总费用</span></p></body></html>"))
        self.label_Total_fee.setText(_translate("Client", "<html><head/><body><p><span style=\" font-weight:600;\">0.00</span></p></body></html>"))
        self.label_14.setText(_translate("Client", "<html><head/><body><p>元</p></body></html>"))
        self.textBrowser.setHtml(_translate("Client", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">目标温度</p></body></html>"))
        self.textBrowser_target_tem.setHtml(_translate("Client", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:72;\">25</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Client", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">模式</p></body></html>"))
        self.textBrowser_mode.setHtml(_translate("Client", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:72;\">制冷</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("Client", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">风速</p></body></html>"))
        self.textBrowser_speed.setHtml(_translate("Client", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">mid</p></body></html>"))

import picture_rc
