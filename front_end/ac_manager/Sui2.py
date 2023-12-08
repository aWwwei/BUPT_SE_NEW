# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sui2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 631, 541))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(253, 231, 223, 255), stop:1 rgba(223, 228, 226, 255));\n"
"border-radius:20px ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(2, 0, 661, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(-8, 0, 641, 181))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet("background-color: rgb(168, 168, 168,100);\n"
"border-radius:20px ;\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(90, 0, 221, 41))
        self.label_4.setStyleSheet("QLabel {\n"
"    border:none;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLabel::item{\n"
"background-color: transparent;\n"
"height:40px;\n"
"padding-left:4px;\n"
"\n"
"}\n"
"QLabel::item:hover {\n"
"    background-color:  transparent;\n"
"    color: rgba(43, 162, 238,150);\n"
"\n"
"\n"
"\n"
"}\n"
"QLabel::item:selected {\n"
"    /*background-color: transparent;*/\n"
"background-color:  transparent;\n"
"    color: rgb(43, 162, 238);\n"
"\n"
"\n"
"}\n"
"")
        self.label_4.setObjectName("label_4")
        self.widget = QtWidgets.QWidget(self.frame_5)
        self.widget.setGeometry(QtCore.QRect(10, 0, 71, 41))
        self.widget.setStyleSheet("image: url(:/管理员界面/空调.png);")
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_6)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 0, 629, 131))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_13 = QtWidgets.QFrame(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.layoutWidget_3 = QtWidgets.QWidget(self.frame_13)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 0, 311, 131))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_71 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_71.setObjectName("horizontalLayout_71")
        self.frame_80 = QtWidgets.QFrame(self.layoutWidget_3)
        self.frame_80.setStyleSheet("background-color: rgb(255, 242, 235);")
        self.frame_80.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_80.setObjectName("frame_80")
        self.layoutWidget2 = QtWidgets.QWidget(self.frame_80)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 0, 311, 131))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_21 = QtWidgets.QFrame(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setStyleSheet("#frame_21{\n"
"border-radius:10px;\n"
"background-color: rgb(255, 205, 198);\n"
"border:1px solid black\n"
"}")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.layoutWidget_27 = QtWidgets.QWidget(self.frame_21)
        self.layoutWidget_27.setGeometry(QtCore.QRect(10, 1, 291, 21))
        self.layoutWidget_27.setObjectName("layoutWidget_27")
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout(self.layoutWidget_27)
        self.horizontalLayout_57.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        self.frame_43 = QtWidgets.QFrame(self.layoutWidget_27)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_43.sizePolicy().hasHeightForWidth())
        self.frame_43.setSizePolicy(sizePolicy)
        self.frame_43.setStyleSheet("image: url(:/管理员界面/计费费率.png);\n"
"background-color: rgb(255, 205, 198);")
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.horizontalLayout_57.addWidget(self.frame_43)
        self.frame_44 = QtWidgets.QFrame(self.layoutWidget_27)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_44.sizePolicy().hasHeightForWidth())
        self.frame_44.setSizePolicy(sizePolicy)
        self.frame_44.setStyleSheet("background-color: rgb(255, 242, 235);")
        self.frame_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_44.setObjectName("frame_44")
        self.layoutWidget_28 = QtWidgets.QWidget(self.frame_44)
        self.layoutWidget_28.setGeometry(QtCore.QRect(0, 0, 251, 22))
        self.layoutWidget_28.setObjectName("layoutWidget_28")
        self.horizontalLayout_58 = QtWidgets.QHBoxLayout(self.layoutWidget_28)
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_58.setObjectName("horizontalLayout_58")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_28)
        self.label_18.setStyleSheet("background-color: rgb(255, 205, 198);\n"
"font: 75 9pt \"微软雅黑\";")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_58.addWidget(self.label_18)
        self.horizontalLayout_57.addWidget(self.frame_44)
        self.verticalLayout_3.addWidget(self.frame_21)
        self.frame_22 = QtWidgets.QFrame(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.frame_23 = QtWidgets.QFrame(self.frame_22)
        self.frame_23.setGeometry(QtCore.QRect(20, 10, 151, 61))
        self.frame_23.setStyleSheet("")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.layoutWidget_4 = QtWidgets.QWidget(self.frame_23)
        self.layoutWidget_4.setGeometry(QtCore.QRect(0, 0, 151, 61))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_59 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName("horizontalLayout_59")
        self.doubleSpinBox_rates = QtWidgets.QDoubleSpinBox(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_rates.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_rates.setSizePolicy(sizePolicy)
        self.doubleSpinBox_rates.setStyleSheet("")
        self.doubleSpinBox_rates.setProperty("value", 1.0)
        self.doubleSpinBox_rates.setObjectName("doubleSpinBox_rates")
        self.horizontalLayout_59.addWidget(self.doubleSpinBox_rates)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_59.addWidget(self.label_8)
        self.pushButton_Rates_check = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_Rates_check.setGeometry(QtCore.QRect(210, 30, 41, 31))
        self.pushButton_Rates_check.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    font: 12pt \"黑体\";\n"
"    \n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    \n"
"    \n"
"    image: url(:/管理员界面/对勾.png);\n"
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
        self.pushButton_Rates_check.setText("")
        self.pushButton_Rates_check.setObjectName("pushButton_Rates_check")
        self.verticalLayout_3.addWidget(self.frame_22)
        self.horizontalLayout_71.addWidget(self.frame_80)
        self.horizontalLayout.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.layoutWidget_2)
        self.frame_14.setStyleSheet("background-color: rgb(255, 242, 235);")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.layoutWidget3 = QtWidgets.QWidget(self.frame_14)
        self.layoutWidget3.setGeometry(QtCore.QRect(0, 0, 301, 131))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_15 = QtWidgets.QFrame(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setStyleSheet("#frame_15{\n"
"border-radius:10px;\n"
"background-color: rgb(255, 205, 198);\n"
"border:1px solid black\n"
"}")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.layoutWidget_16 = QtWidgets.QWidget(self.frame_15)
        self.layoutWidget_16.setGeometry(QtCore.QRect(10, 1, 281, 21))
        self.layoutWidget_16.setObjectName("layoutWidget_16")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.layoutWidget_16)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.frame_19 = QtWidgets.QFrame(self.layoutWidget_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setStyleSheet("image: url(:/管理员界面/温度.png);\n"
"background-color: rgb(255, 205, 198);")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_31.addWidget(self.frame_19)
        self.frame_20 = QtWidgets.QFrame(self.layoutWidget_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setStyleSheet("background-color: rgb(255, 242, 235);")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.layoutWidget_17 = QtWidgets.QWidget(self.frame_20)
        self.layoutWidget_17.setGeometry(QtCore.QRect(0, 0, 241, 22))
        self.layoutWidget_17.setObjectName("layoutWidget_17")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.layoutWidget_17)
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_17)
        self.label_5.setStyleSheet("background-color: rgb(255, 205, 198);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_32.addWidget(self.label_5)
        self.horizontalLayout_31.addWidget(self.frame_20)
        self.verticalLayout_4.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.layoutWidget_5 = QtWidgets.QWidget(self.frame_16)
        self.layoutWidget_5.setGeometry(QtCore.QRect(0, 0, 313, 91))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.frame_17 = QtWidgets.QFrame(self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.layoutWidget_7 = QtWidgets.QWidget(self.frame_17)
        self.layoutWidget_7.setGeometry(QtCore.QRect(0, 0, 101, 41))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_18 = QtWidgets.QFrame(self.layoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setStyleSheet("")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.lcdNumber_t_low = QtWidgets.QLCDNumber(self.frame_18)
        self.lcdNumber_t_low.setGeometry(QtCore.QRect(0, 10, 61, 23))
        self.lcdNumber_t_low.setStyleSheet("background-color: rgb(255, 242, 235);\n"
"border-radius:16px ;\n"
"border: 1px solid black ;\n"
"border-color: rgb(163, 163, 163);")
        self.lcdNumber_t_low.setSmallDecimalPoint(False)
        self.lcdNumber_t_low.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_t_low.setProperty("value", 16.0)
        self.lcdNumber_t_low.setObjectName("lcdNumber_t_low")
        self.horizontalLayout_8.addWidget(self.frame_18)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.horizontalLayout_6.addWidget(self.frame_17)
        self.frame_24 = QtWidgets.QFrame(self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setStyleSheet("background-color: rgb(255, 242, 235);")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.layoutWidget_8 = QtWidgets.QWidget(self.frame_24)
        self.layoutWidget_8.setGeometry(QtCore.QRect(0, 0, 121, 41))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_25 = QtWidgets.QFrame(self.layoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setStyleSheet("background-color: rgb(255, 242, 235)；")
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.lcdNumber_t_high = QtWidgets.QLCDNumber(self.frame_25)
        self.lcdNumber_t_high.setGeometry(QtCore.QRect(10, 10, 61, 23))
        self.lcdNumber_t_high.setStyleSheet("background-color: rgb(255, 242, 235);\n"
"border-radius:16px ;\n"
"border: 1px solid black ;\n"
"border-color: rgb(163, 163, 163);")
        self.lcdNumber_t_high.setSmallDecimalPoint(False)
        self.lcdNumber_t_high.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_t_high.setProperty("value", 24.0)
        self.lcdNumber_t_high.setObjectName("lcdNumber_t_high")
        self.horizontalLayout_9.addWidget(self.frame_25)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.horizontalLayout_6.addWidget(self.frame_24)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(45, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.pushButton_low_down = QtWidgets.QPushButton(self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_low_down.sizePolicy().hasHeightForWidth())
        self.pushButton_low_down.setSizePolicy(sizePolicy)
        self.pushButton_low_down.setStyleSheet("\n"
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
        self.pushButton_low_down.setText("")
        self.pushButton_low_down.setObjectName("pushButton_low_down")
        self.horizontalLayout_7.addWidget(self.pushButton_low_down)
        self.pushButton_low_up = QtWidgets.QPushButton(self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_low_up.sizePolicy().hasHeightForWidth())
        self.pushButton_low_up.setSizePolicy(sizePolicy)
        self.pushButton_low_up.setStyleSheet("\n"
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
        self.pushButton_low_up.setText("")
        self.pushButton_low_up.setObjectName("pushButton_low_up")
        self.horizontalLayout_7.addWidget(self.pushButton_low_up)
        spacerItem3 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.pushButton_high_down = QtWidgets.QPushButton(self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_high_down.sizePolicy().hasHeightForWidth())
        self.pushButton_high_down.setSizePolicy(sizePolicy)
        self.pushButton_high_down.setStyleSheet("\n"
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
        self.pushButton_high_down.setText("")
        self.pushButton_high_down.setObjectName("pushButton_high_down")
        self.horizontalLayout_7.addWidget(self.pushButton_high_down)
        self.pushButton_high_up = QtWidgets.QPushButton(self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_high_up.sizePolicy().hasHeightForWidth())
        self.pushButton_high_up.setSizePolicy(sizePolicy)
        self.pushButton_high_up.setStyleSheet("\n"
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
        self.pushButton_high_up.setText("")
        self.pushButton_high_up.setObjectName("pushButton_high_up")
        self.horizontalLayout_7.addWidget(self.pushButton_high_up)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addWidget(self.frame_16)
        self.horizontalLayout.addWidget(self.frame_14)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.layoutWidget4 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget4.setGeometry(QtCore.QRect(0, 0, 621, 181))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.layoutWidget4)
        self.frame_7.setStyleSheet("background-color: rgb(255, 242, 235);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.layoutWidget_14 = QtWidgets.QWidget(self.frame_7)
        self.layoutWidget_14.setGeometry(QtCore.QRect(0, 0, 201, 31))
        self.layoutWidget_14.setObjectName("layoutWidget_14")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.layoutWidget_14)
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.frame_41 = QtWidgets.QFrame(self.layoutWidget_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy)
        self.frame_41.setStyleSheet("image: url(:/管理员界面/摄像头.png);\n"
"background-color: rgb(255, 242, 235);")
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.horizontalLayout_38.addWidget(self.frame_41)
        self.frame_42 = QtWidgets.QFrame(self.layoutWidget_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_42.sizePolicy().hasHeightForWidth())
        self.frame_42.setSizePolicy(sizePolicy)
        self.frame_42.setStyleSheet("")
        self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.layoutWidget_26 = QtWidgets.QWidget(self.frame_42)
        self.layoutWidget_26.setGeometry(QtCore.QRect(0, 0, 161, 31))
        self.layoutWidget_26.setObjectName("layoutWidget_26")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.layoutWidget_26)
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_26)
        self.label_17.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_39.addWidget(self.label_17)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_39.addItem(spacerItem5)
        self.horizontalLayout_38.addWidget(self.frame_42)
        self.pushButton_switch = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_switch.setGeometry(QtCore.QRect(70, 40, 61, 51))
        self.pushButton_switch.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    font: 12pt \"黑体\";\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    \n"
"    \n"
"    border-radius: 10px;\n"
"image: url(:/管理员界面/开关.png);\n"
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
        self.pushButton_switch.setText("")
        self.pushButton_switch.setObjectName("pushButton_switch")
        self.pushButton_cold = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_cold.setGeometry(QtCore.QRect(20, 119, 61, 31))
        self.pushButton_cold.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    font: 12pt \"黑体\";\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"\n"
"    border-radius: 10px;\n"
"image: url(:/管理员界面/制冷.png);\n"
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
        self.pushButton_cold.setText("")
        self.pushButton_cold.setObjectName("pushButton_cold")
        self.pushButton_warm = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_warm.setGeometry(QtCore.QRect(120, 120, 61, 31))
        self.pushButton_warm.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    font: 12pt \"黑体\";\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"\n"
"    border-radius: 10px;\n"
"image: url(:/管理员界面/制热.png);\n"
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
        self.pushButton_warm.setText("")
        self.pushButton_warm.setObjectName("pushButton_warm")
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.layoutWidget4)
        self.frame_8.setStyleSheet("background-color: rgb(255, 242, 235);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.layoutWidget_47 = QtWidgets.QWidget(self.frame_8)
        self.layoutWidget_47.setGeometry(QtCore.QRect(0, 0, 201, 171))
        self.layoutWidget_47.setObjectName("layoutWidget_47")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.layoutWidget_47)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.frame_153 = QtWidgets.QFrame(self.layoutWidget_47)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_153.sizePolicy().hasHeightForWidth())
        self.frame_153.setSizePolicy(sizePolicy)
        self.frame_153.setStyleSheet("#frame_153{\n"
"    background-color: rgb(255, 205, 198);\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_153.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_153.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_153.setObjectName("frame_153")
        self.layoutWidget_87 = QtWidgets.QWidget(self.frame_153)
        self.layoutWidget_87.setGeometry(QtCore.QRect(10, 10, 181, 22))
        self.layoutWidget_87.setObjectName("layoutWidget_87")
        self.horizontalLayout_84 = QtWidgets.QHBoxLayout(self.layoutWidget_87)
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_84.setSpacing(0)
        self.horizontalLayout_84.setObjectName("horizontalLayout_84")
        self.ROOM1 = QtWidgets.QLabel(self.layoutWidget_87)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ROOM1.sizePolicy().hasHeightForWidth())
        self.ROOM1.setSizePolicy(sizePolicy)
        self.ROOM1.setStyleSheet("background-color: rgb(255, 205, 198);")
        self.ROOM1.setObjectName("ROOM1")
        self.horizontalLayout_84.addWidget(self.ROOM1)
        self.verticalLayout_27.addWidget(self.frame_153)
        self.frame_154 = QtWidgets.QFrame(self.layoutWidget_47)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.frame_154.sizePolicy().hasHeightForWidth())
        self.frame_154.setSizePolicy(sizePolicy)
        self.frame_154.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_154.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_154.setObjectName("frame_154")
        self.layoutWidget_88 = QtWidgets.QWidget(self.frame_154)
        self.layoutWidget_88.setGeometry(QtCore.QRect(0, 0, 201, 141))
        self.layoutWidget_88.setObjectName("layoutWidget_88")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.layoutWidget_88)
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_28.setSpacing(6)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.frame_155 = QtWidgets.QFrame(self.layoutWidget_88)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_155.sizePolicy().hasHeightForWidth())
        self.frame_155.setSizePolicy(sizePolicy)
        self.frame_155.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_155.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_155.setObjectName("frame_155")
        self.layoutWidget_10 = QtWidgets.QWidget(self.frame_155)
        self.layoutWidget_10.setGeometry(QtCore.QRect(0, 0, 201, 31))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_26 = QtWidgets.QFrame(self.layoutWidget_10)
        self.frame_26.setStyleSheet("#frame_26{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.layoutWidget_30 = QtWidgets.QWidget(self.frame_26)
        self.layoutWidget_30.setGeometry(QtCore.QRect(10, 5, 116, 59))
        self.layoutWidget_30.setObjectName("layoutWidget_30")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.layoutWidget_30)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.textBrowser_R1_state = QtWidgets.QTextBrowser(self.layoutWidget_30)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_R1_state.sizePolicy().hasHeightForWidth())
        self.textBrowser_R1_state.setSizePolicy(sizePolicy)
        self.textBrowser_R1_state.setStyleSheet("")
        self.textBrowser_R1_state.setObjectName("textBrowser_R1_state")
        self.horizontalLayout_20.addWidget(self.textBrowser_R1_state)
        self.textBrowser_Room1_state = QtWidgets.QTextBrowser(self.layoutWidget_30)
        self.textBrowser_Room1_state.setReadOnly(False)
        self.textBrowser_Room1_state.setObjectName("textBrowser_Room1_state")
        self.horizontalLayout_20.addWidget(self.textBrowser_Room1_state)
        self.horizontalLayout_5.addWidget(self.frame_26)
        self.frame_27 = QtWidgets.QFrame(self.layoutWidget_10)
        self.frame_27.setStyleSheet("#frame_27{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.layoutWidget_31 = QtWidgets.QWidget(self.frame_27)
        self.layoutWidget_31.setGeometry(QtCore.QRect(10, 5, 116, 59))
        self.layoutWidget_31.setObjectName("layoutWidget_31")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.layoutWidget_31)
        self.horizontalLayout_21.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.textBrowser_R1_mode = QtWidgets.QTextBrowser(self.layoutWidget_31)
        self.textBrowser_R1_mode.setObjectName("textBrowser_R1_mode")
        self.horizontalLayout_21.addWidget(self.textBrowser_R1_mode)
        self.textBrowser_Room1_mode = QtWidgets.QTextBrowser(self.layoutWidget_31)
        self.textBrowser_Room1_mode.setReadOnly(False)
        self.textBrowser_Room1_mode.setObjectName("textBrowser_Room1_mode")
        self.horizontalLayout_21.addWidget(self.textBrowser_Room1_mode)
        self.horizontalLayout_5.addWidget(self.frame_27)
        self.verticalLayout_28.addWidget(self.frame_155)
        self.frame_156 = QtWidgets.QFrame(self.layoutWidget_88)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_156.sizePolicy().hasHeightForWidth())
        self.frame_156.setSizePolicy(sizePolicy)
        self.frame_156.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_156.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_156.setObjectName("frame_156")
        self.layoutWidget_15 = QtWidgets.QWidget(self.frame_156)
        self.layoutWidget_15.setGeometry(QtCore.QRect(0, 0, 191, 41))
        self.layoutWidget_15.setObjectName("layoutWidget_15")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.layoutWidget_15)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(2)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_34 = QtWidgets.QFrame(self.layoutWidget_15)
        self.frame_34.setStyleSheet("#frame_34{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.layoutWidget_38 = QtWidgets.QWidget(self.frame_34)
        self.layoutWidget_38.setGeometry(QtCore.QRect(10, 5, 116, 59))
        self.layoutWidget_38.setObjectName("layoutWidget_38")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.layoutWidget_38)
        self.horizontalLayout_29.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.textBrowser_R1_tem = QtWidgets.QTextBrowser(self.layoutWidget_38)
        self.textBrowser_R1_tem.setObjectName("textBrowser_R1_tem")
        self.horizontalLayout_29.addWidget(self.textBrowser_R1_tem)
        self.textBrowser_Room1_tem = QtWidgets.QTextBrowser(self.layoutWidget_38)
        self.textBrowser_Room1_tem.setReadOnly(False)
        self.textBrowser_Room1_tem.setObjectName("textBrowser_Room1_tem")
        self.horizontalLayout_29.addWidget(self.textBrowser_Room1_tem)
        self.horizontalLayout_14.addWidget(self.frame_34)
        self.frame_35 = QtWidgets.QFrame(self.layoutWidget_15)
        self.frame_35.setStyleSheet("#frame_35{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.layoutWidget_39 = QtWidgets.QWidget(self.frame_35)
        self.layoutWidget_39.setGeometry(QtCore.QRect(10, 5, 116, 59))
        self.layoutWidget_39.setObjectName("layoutWidget_39")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.layoutWidget_39)
        self.horizontalLayout_30.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.textBrowser_R1_WindSpeed = QtWidgets.QTextBrowser(self.layoutWidget_39)
        self.textBrowser_R1_WindSpeed.setObjectName("textBrowser_R1_WindSpeed")
        self.horizontalLayout_30.addWidget(self.textBrowser_R1_WindSpeed)
        self.textBrowser_Room1_WindSpeed = QtWidgets.QTextBrowser(self.layoutWidget_39)
        self.textBrowser_Room1_WindSpeed.setReadOnly(False)
        self.textBrowser_Room1_WindSpeed.setObjectName("textBrowser_Room1_WindSpeed")
        self.horizontalLayout_30.addWidget(self.textBrowser_Room1_WindSpeed)
        self.horizontalLayout_14.addWidget(self.frame_35)
        self.verticalLayout_28.addWidget(self.frame_156)
        self.frame_159 = QtWidgets.QFrame(self.layoutWidget_88)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_159.sizePolicy().hasHeightForWidth())
        self.frame_159.setSizePolicy(sizePolicy)
        self.frame_159.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_159.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_159.setObjectName("frame_159")
        self.layoutWidget_91 = QtWidgets.QWidget(self.frame_159)
        self.layoutWidget_91.setGeometry(QtCore.QRect(0, 10, 191, 41))
        self.layoutWidget_91.setObjectName("layoutWidget_91")
        self.horizontalLayout_86 = QtWidgets.QHBoxLayout(self.layoutWidget_91)
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_86.setSpacing(6)
        self.horizontalLayout_86.setObjectName("horizontalLayout_86")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_36 = QtWidgets.QFrame(self.layoutWidget_91)
        self.frame_36.setStyleSheet("#frame_36{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.layoutWidget_40 = QtWidgets.QWidget(self.frame_36)
        self.layoutWidget_40.setGeometry(QtCore.QRect(10, 5, 118, 59))
        self.layoutWidget_40.setObjectName("layoutWidget_40")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.layoutWidget_40)
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34.setSpacing(2)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.textBrowser_R1_Currentfee = QtWidgets.QTextBrowser(self.layoutWidget_40)
        self.textBrowser_R1_Currentfee.setStyleSheet("")
        self.textBrowser_R1_Currentfee.setObjectName("textBrowser_R1_Currentfee")
        self.horizontalLayout_34.addWidget(self.textBrowser_R1_Currentfee)
        self.textBrowser_Room1_Currentfee = QtWidgets.QTextBrowser(self.layoutWidget_40)
        self.textBrowser_Room1_Currentfee.setReadOnly(False)
        self.textBrowser_Room1_Currentfee.setObjectName("textBrowser_Room1_Currentfee")
        self.horizontalLayout_34.addWidget(self.textBrowser_Room1_Currentfee)
        self.horizontalLayout_15.addWidget(self.frame_36)
        self.frame_37 = QtWidgets.QFrame(self.layoutWidget_91)
        self.frame_37.setStyleSheet("#frame_37{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.layoutWidget_41 = QtWidgets.QWidget(self.frame_37)
        self.layoutWidget_41.setGeometry(QtCore.QRect(10, 5, 117, 59))
        self.layoutWidget_41.setObjectName("layoutWidget_41")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.layoutWidget_41)
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_35.setSpacing(1)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.textBrowser_R1_Totalfee = QtWidgets.QTextBrowser(self.layoutWidget_41)
        self.textBrowser_R1_Totalfee.setObjectName("textBrowser_R1_Totalfee")
        self.horizontalLayout_35.addWidget(self.textBrowser_R1_Totalfee)
        self.textBrowser_Room1_Totalfee = QtWidgets.QTextBrowser(self.layoutWidget_41)
        self.textBrowser_Room1_Totalfee.setReadOnly(False)
        self.textBrowser_Room1_Totalfee.setObjectName("textBrowser_Room1_Totalfee")
        self.horizontalLayout_35.addWidget(self.textBrowser_Room1_Totalfee)
        self.horizontalLayout_15.addWidget(self.frame_37)
        self.horizontalLayout_86.addLayout(self.horizontalLayout_15)
        self.verticalLayout_28.addWidget(self.frame_159)
        self.verticalLayout_27.addWidget(self.frame_154)
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.layoutWidget4)
        self.frame_9.setStyleSheet("background-color: rgb(255, 242, 235);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.layoutWidget_48 = QtWidgets.QWidget(self.frame_9)
        self.layoutWidget_48.setGeometry(QtCore.QRect(0, 0, 201, 171))
        self.layoutWidget_48.setObjectName("layoutWidget_48")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.layoutWidget_48)
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.frame_157 = QtWidgets.QFrame(self.layoutWidget_48)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_157.sizePolicy().hasHeightForWidth())
        self.frame_157.setSizePolicy(sizePolicy)
        self.frame_157.setStyleSheet("#frame_157{\n"
"    background-color: rgb(255, 205, 198);\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_157.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_157.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_157.setObjectName("frame_157")
        self.layoutWidget_89 = QtWidgets.QWidget(self.frame_157)
        self.layoutWidget_89.setGeometry(QtCore.QRect(10, 10, 181, 22))
        self.layoutWidget_89.setObjectName("layoutWidget_89")
        self.horizontalLayout_85 = QtWidgets.QHBoxLayout(self.layoutWidget_89)
        self.horizontalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_85.setSpacing(0)
        self.horizontalLayout_85.setObjectName("horizontalLayout_85")
        self.ROOM2 = QtWidgets.QLabel(self.layoutWidget_89)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ROOM2.sizePolicy().hasHeightForWidth())
        self.ROOM2.setSizePolicy(sizePolicy)
        self.ROOM2.setStyleSheet("background-color: rgb(255, 205, 198);")
        self.ROOM2.setObjectName("ROOM2")
        self.horizontalLayout_85.addWidget(self.ROOM2)
        self.verticalLayout_29.addWidget(self.frame_157)
        self.frame_158 = QtWidgets.QFrame(self.layoutWidget_48)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.frame_158.sizePolicy().hasHeightForWidth())
        self.frame_158.setSizePolicy(sizePolicy)
        self.frame_158.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_158.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_158.setObjectName("frame_158")
        self.layoutWidget_90 = QtWidgets.QWidget(self.frame_158)
        self.layoutWidget_90.setGeometry(QtCore.QRect(0, 0, 201, 141))
        self.layoutWidget_90.setObjectName("layoutWidget_90")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.layoutWidget_90)
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.frame_160 = QtWidgets.QFrame(self.layoutWidget_90)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_160.sizePolicy().hasHeightForWidth())
        self.frame_160.setSizePolicy(sizePolicy)
        self.frame_160.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_160.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_160.setObjectName("frame_160")
        self.layoutWidget_13 = QtWidgets.QWidget(self.frame_160)
        self.layoutWidget_13.setGeometry(QtCore.QRect(0, 0, 201, 51))
        self.layoutWidget_13.setObjectName("layoutWidget_13")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.layoutWidget_13)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.layoutWidget_11 = QtWidgets.QWidget(self.frame_160)
        self.layoutWidget_11.setGeometry(QtCore.QRect(0, 0, 201, 41))
        self.layoutWidget_11.setObjectName("layoutWidget_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget_11)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_28 = QtWidgets.QFrame(self.layoutWidget_11)
        self.frame_28.setStyleSheet("#frame_28{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.layoutWidget_32 = QtWidgets.QWidget(self.frame_28)
        self.layoutWidget_32.setGeometry(QtCore.QRect(10, 5, 116, 59))
        self.layoutWidget_32.setObjectName("layoutWidget_32")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.layoutWidget_32)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.textBrowser_R2_state = QtWidgets.QTextBrowser(self.layoutWidget_32)
        self.textBrowser_R2_state.setStyleSheet("")
        self.textBrowser_R2_state.setObjectName("textBrowser_R2_state")
        self.horizontalLayout_22.addWidget(self.textBrowser_R2_state)
        self.textBrowser_Room2_state = QtWidgets.QTextBrowser(self.layoutWidget_32)
        self.textBrowser_Room2_state.setReadOnly(False)
        self.textBrowser_Room2_state.setObjectName("textBrowser_Room2_state")
        self.horizontalLayout_22.addWidget(self.textBrowser_Room2_state)
        self.horizontalLayout_10.addWidget(self.frame_28)
        self.frame_29 = QtWidgets.QFrame(self.layoutWidget_11)
        self.frame_29.setStyleSheet("#frame_29{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.layoutWidget_33 = QtWidgets.QWidget(self.frame_29)
        self.layoutWidget_33.setGeometry(QtCore.QRect(10, 5, 116, 59))
        self.layoutWidget_33.setObjectName("layoutWidget_33")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.layoutWidget_33)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.textBrowser_R2_mode = QtWidgets.QTextBrowser(self.layoutWidget_33)
        self.textBrowser_R2_mode.setObjectName("textBrowser_R2_mode")
        self.horizontalLayout_23.addWidget(self.textBrowser_R2_mode)
        self.textBrowser_Room2_mode = QtWidgets.QTextBrowser(self.layoutWidget_33)
        self.textBrowser_Room2_mode.setReadOnly(False)
        self.textBrowser_Room2_mode.setObjectName("textBrowser_Room2_mode")
        self.horizontalLayout_23.addWidget(self.textBrowser_Room2_mode)
        self.horizontalLayout_10.addWidget(self.frame_29)
        self.verticalLayout_30.addWidget(self.frame_160)
        self.frame_161 = QtWidgets.QFrame(self.layoutWidget_90)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_161.sizePolicy().hasHeightForWidth())
        self.frame_161.setSizePolicy(sizePolicy)
        self.frame_161.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_161.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_161.setObjectName("frame_161")
        self.layoutWidget_19 = QtWidgets.QWidget(self.frame_161)
        self.layoutWidget_19.setGeometry(QtCore.QRect(0, 0, 201, 41))
        self.layoutWidget_19.setObjectName("layoutWidget_19")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.layoutWidget_19)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.frame_38 = QtWidgets.QFrame(self.layoutWidget_19)
        self.frame_38.setStyleSheet("#frame_38{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.layoutWidget_42 = QtWidgets.QWidget(self.frame_38)
        self.layoutWidget_42.setGeometry(QtCore.QRect(10, 5, 116, 59))
        self.layoutWidget_42.setObjectName("layoutWidget_42")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.layoutWidget_42)
        self.horizontalLayout_36.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.textBrowser_R2_tem = QtWidgets.QTextBrowser(self.layoutWidget_42)
        self.textBrowser_R2_tem.setObjectName("textBrowser_R2_tem")
        self.horizontalLayout_36.addWidget(self.textBrowser_R2_tem)
        self.textBrowser_Room2_tem = QtWidgets.QTextBrowser(self.layoutWidget_42)
        self.textBrowser_Room2_tem.setReadOnly(False)
        self.textBrowser_Room2_tem.setObjectName("textBrowser_Room2_tem")
        self.horizontalLayout_36.addWidget(self.textBrowser_Room2_tem)
        self.horizontalLayout_16.addWidget(self.frame_38)
        self.frame_39 = QtWidgets.QFrame(self.layoutWidget_19)
        self.frame_39.setStyleSheet("#frame_39{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.layoutWidget_43 = QtWidgets.QWidget(self.frame_39)
        self.layoutWidget_43.setGeometry(QtCore.QRect(10, 5, 116, 59))
        self.layoutWidget_43.setObjectName("layoutWidget_43")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.layoutWidget_43)
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.textBrowser_R2_WindSpeed = QtWidgets.QTextBrowser(self.layoutWidget_43)
        self.textBrowser_R2_WindSpeed.setObjectName("textBrowser_R2_WindSpeed")
        self.horizontalLayout_37.addWidget(self.textBrowser_R2_WindSpeed)
        self.textBrowser_Room2_WindSpeed = QtWidgets.QTextBrowser(self.layoutWidget_43)
        self.textBrowser_Room2_WindSpeed.setReadOnly(False)
        self.textBrowser_Room2_WindSpeed.setObjectName("textBrowser_Room2_WindSpeed")
        self.horizontalLayout_37.addWidget(self.textBrowser_Room2_WindSpeed)
        self.horizontalLayout_16.addWidget(self.frame_39)
        self.verticalLayout_30.addWidget(self.frame_161)
        self.frame_162 = QtWidgets.QFrame(self.layoutWidget_90)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_162.sizePolicy().hasHeightForWidth())
        self.frame_162.setSizePolicy(sizePolicy)
        self.frame_162.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_162.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_162.setObjectName("frame_162")
        self.layoutWidget_92 = QtWidgets.QWidget(self.frame_162)
        self.layoutWidget_92.setGeometry(QtCore.QRect(0, 0, 201, 51))
        self.layoutWidget_92.setObjectName("layoutWidget_92")
        self.horizontalLayout_87 = QtWidgets.QHBoxLayout(self.layoutWidget_92)
        self.horizontalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_87.setObjectName("horizontalLayout_87")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.frame_40 = QtWidgets.QFrame(self.layoutWidget_92)
        self.frame_40.setStyleSheet("#frame_40{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.layoutWidget_44 = QtWidgets.QWidget(self.frame_40)
        self.layoutWidget_44.setGeometry(QtCore.QRect(10, 5, 118, 59))
        self.layoutWidget_44.setObjectName("layoutWidget_44")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.layoutWidget_44)
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_40.setSpacing(2)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.textBrowser_R2_Currentfee = QtWidgets.QTextBrowser(self.layoutWidget_44)
        self.textBrowser_R2_Currentfee.setStyleSheet("")
        self.textBrowser_R2_Currentfee.setObjectName("textBrowser_R2_Currentfee")
        self.horizontalLayout_40.addWidget(self.textBrowser_R2_Currentfee)
        self.textBrowser_Room2_Currentfee = QtWidgets.QTextBrowser(self.layoutWidget_44)
        self.textBrowser_Room2_Currentfee.setReadOnly(False)
        self.textBrowser_Room2_Currentfee.setObjectName("textBrowser_Room2_Currentfee")
        self.horizontalLayout_40.addWidget(self.textBrowser_Room2_Currentfee)
        self.horizontalLayout_17.addWidget(self.frame_40)
        self.frame_45 = QtWidgets.QFrame(self.layoutWidget_92)
        self.frame_45.setStyleSheet("#frame_45{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.layoutWidget_45 = QtWidgets.QWidget(self.frame_45)
        self.layoutWidget_45.setGeometry(QtCore.QRect(10, 5, 117, 59))
        self.layoutWidget_45.setObjectName("layoutWidget_45")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.layoutWidget_45)
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_41.setSpacing(1)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.textBrowser_R2_Totalfee = QtWidgets.QTextBrowser(self.layoutWidget_45)
        self.textBrowser_R2_Totalfee.setObjectName("textBrowser_R2_Totalfee")
        self.horizontalLayout_41.addWidget(self.textBrowser_R2_Totalfee)
        self.textBrowser_Room2_Totalfee = QtWidgets.QTextBrowser(self.layoutWidget_45)
        self.textBrowser_Room2_Totalfee.setReadOnly(False)
        self.textBrowser_Room2_Totalfee.setObjectName("textBrowser_Room2_Totalfee")
        self.horizontalLayout_41.addWidget(self.textBrowser_Room2_Totalfee)
        self.horizontalLayout_17.addWidget(self.frame_45)
        self.horizontalLayout_87.addLayout(self.horizontalLayout_17)
        self.verticalLayout_30.addWidget(self.frame_162)
        self.verticalLayout_29.addWidget(self.frame_158)
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.layoutWidget_6 = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget_6.setGeometry(QtCore.QRect(0, 0, 621, 181))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.layoutWidget_6)
        self.frame_10.setStyleSheet("background-color: rgb(255, 242, 235);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.layoutWidget_49 = QtWidgets.QWidget(self.frame_10)
        self.layoutWidget_49.setGeometry(QtCore.QRect(0, 0, 201, 171))
        self.layoutWidget_49.setObjectName("layoutWidget_49")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.layoutWidget_49)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.frame_163 = QtWidgets.QFrame(self.layoutWidget_49)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_163.sizePolicy().hasHeightForWidth())
        self.frame_163.setSizePolicy(sizePolicy)
        self.frame_163.setStyleSheet("#frame_163{\n"
"    background-color: rgb(255, 205, 198);\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_163.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_163.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_163.setObjectName("frame_163")
        self.layoutWidget_93 = QtWidgets.QWidget(self.frame_163)
        self.layoutWidget_93.setGeometry(QtCore.QRect(10, 10, 181, 22))
        self.layoutWidget_93.setObjectName("layoutWidget_93")
        self.horizontalLayout_88 = QtWidgets.QHBoxLayout(self.layoutWidget_93)
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_88.setSpacing(0)
        self.horizontalLayout_88.setObjectName("horizontalLayout_88")
        self.ROOM3 = QtWidgets.QLabel(self.layoutWidget_93)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ROOM3.sizePolicy().hasHeightForWidth())
        self.ROOM3.setSizePolicy(sizePolicy)
        self.ROOM3.setStyleSheet("background-color: rgb(255, 205, 198);")
        self.ROOM3.setObjectName("ROOM3")
        self.horizontalLayout_88.addWidget(self.ROOM3)
        self.verticalLayout_31.addWidget(self.frame_163)
        self.frame_164 = QtWidgets.QFrame(self.layoutWidget_49)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.frame_164.sizePolicy().hasHeightForWidth())
        self.frame_164.setSizePolicy(sizePolicy)
        self.frame_164.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_164.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_164.setObjectName("frame_164")
        self.layoutWidget_94 = QtWidgets.QWidget(self.frame_164)
        self.layoutWidget_94.setGeometry(QtCore.QRect(0, 0, 201, 141))
        self.layoutWidget_94.setObjectName("layoutWidget_94")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.layoutWidget_94)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.frame_165 = QtWidgets.QFrame(self.layoutWidget_94)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_165.sizePolicy().hasHeightForWidth())
        self.frame_165.setSizePolicy(sizePolicy)
        self.frame_165.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_165.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_165.setObjectName("frame_165")
        self.layoutWidget_21 = QtWidgets.QWidget(self.frame_165)
        self.layoutWidget_21.setGeometry(QtCore.QRect(0, 0, 201, 41))
        self.layoutWidget_21.setObjectName("layoutWidget_21")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget_21)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_30 = QtWidgets.QFrame(self.layoutWidget_21)
        self.frame_30.setStyleSheet("#frame_30{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.layoutWidget_34 = QtWidgets.QWidget(self.frame_30)
        self.layoutWidget_34.setGeometry(QtCore.QRect(10, 5, 116, 59))
        self.layoutWidget_34.setObjectName("layoutWidget_34")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.layoutWidget_34)
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.textBrowser_R3_state = QtWidgets.QTextBrowser(self.layoutWidget_34)
        self.textBrowser_R3_state.setStyleSheet("")
        self.textBrowser_R3_state.setObjectName("textBrowser_R3_state")
        self.horizontalLayout_24.addWidget(self.textBrowser_R3_state)
        self.textBrowser_Room3_state = QtWidgets.QTextBrowser(self.layoutWidget_34)
        self.textBrowser_Room3_state.setReadOnly(False)
        self.textBrowser_Room3_state.setObjectName("textBrowser_Room3_state")
        self.horizontalLayout_24.addWidget(self.textBrowser_Room3_state)
        self.horizontalLayout_11.addWidget(self.frame_30)
        self.frame_31 = QtWidgets.QFrame(self.layoutWidget_21)
        self.frame_31.setStyleSheet("#frame_31{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.layoutWidget_35 = QtWidgets.QWidget(self.frame_31)
        self.layoutWidget_35.setGeometry(QtCore.QRect(10, 5, 116, 59))
        self.layoutWidget_35.setObjectName("layoutWidget_35")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.layoutWidget_35)
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.textBrowser_R3_mode = QtWidgets.QTextBrowser(self.layoutWidget_35)
        self.textBrowser_R3_mode.setObjectName("textBrowser_R3_mode")
        self.horizontalLayout_28.addWidget(self.textBrowser_R3_mode)
        self.textBrowser_Room3_mode = QtWidgets.QTextBrowser(self.layoutWidget_35)
        self.textBrowser_Room3_mode.setReadOnly(False)
        self.textBrowser_Room3_mode.setObjectName("textBrowser_Room3_mode")
        self.horizontalLayout_28.addWidget(self.textBrowser_Room3_mode)
        self.horizontalLayout_11.addWidget(self.frame_31)
        self.verticalLayout_32.addWidget(self.frame_165)
        self.frame_166 = QtWidgets.QFrame(self.layoutWidget_94)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_166.sizePolicy().hasHeightForWidth())
        self.frame_166.setSizePolicy(sizePolicy)
        self.frame_166.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_166.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_166.setObjectName("frame_166")
        self.layoutWidget_22 = QtWidgets.QWidget(self.frame_166)
        self.layoutWidget_22.setGeometry(QtCore.QRect(0, 0, 201, 41))
        self.layoutWidget_22.setObjectName("layoutWidget_22")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.layoutWidget_22)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.frame_46 = QtWidgets.QFrame(self.layoutWidget_22)
        self.frame_46.setStyleSheet("#frame_46{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.layoutWidget_46 = QtWidgets.QWidget(self.frame_46)
        self.layoutWidget_46.setGeometry(QtCore.QRect(10, 5, 116, 59))
        self.layoutWidget_46.setObjectName("layoutWidget_46")
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout(self.layoutWidget_46)
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.textBrowser_R3_tem = QtWidgets.QTextBrowser(self.layoutWidget_46)
        self.textBrowser_R3_tem.setObjectName("textBrowser_R3_tem")
        self.horizontalLayout_42.addWidget(self.textBrowser_R3_tem)
        self.textBrowser_Room3_tem = QtWidgets.QTextBrowser(self.layoutWidget_46)
        self.textBrowser_Room3_tem.setReadOnly(False)
        self.textBrowser_Room3_tem.setObjectName("textBrowser_Room3_tem")
        self.horizontalLayout_42.addWidget(self.textBrowser_Room3_tem)
        self.horizontalLayout_18.addWidget(self.frame_46)
        self.frame_47 = QtWidgets.QFrame(self.layoutWidget_22)
        self.frame_47.setStyleSheet("#frame_47{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.layoutWidget_50 = QtWidgets.QWidget(self.frame_47)
        self.layoutWidget_50.setGeometry(QtCore.QRect(10, 5, 116, 59))
        self.layoutWidget_50.setObjectName("layoutWidget_50")
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout(self.layoutWidget_50)
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.textBrowser_R3_WindSpeed = QtWidgets.QTextBrowser(self.layoutWidget_50)
        self.textBrowser_R3_WindSpeed.setObjectName("textBrowser_R3_WindSpeed")
        self.horizontalLayout_43.addWidget(self.textBrowser_R3_WindSpeed)
        self.textBrowser_Room3_WindSpeed = QtWidgets.QTextBrowser(self.layoutWidget_50)
        self.textBrowser_Room3_WindSpeed.setReadOnly(False)
        self.textBrowser_Room3_WindSpeed.setObjectName("textBrowser_Room3_WindSpeed")
        self.horizontalLayout_43.addWidget(self.textBrowser_Room3_WindSpeed)
        self.horizontalLayout_18.addWidget(self.frame_47)
        self.verticalLayout_32.addWidget(self.frame_166)
        self.frame_167 = QtWidgets.QFrame(self.layoutWidget_94)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_167.sizePolicy().hasHeightForWidth())
        self.frame_167.setSizePolicy(sizePolicy)
        self.frame_167.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_167.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_167.setObjectName("frame_167")
        self.layoutWidget_95 = QtWidgets.QWidget(self.frame_167)
        self.layoutWidget_95.setGeometry(QtCore.QRect(0, 0, 201, 51))
        self.layoutWidget_95.setObjectName("layoutWidget_95")
        self.horizontalLayout_89 = QtWidgets.QHBoxLayout(self.layoutWidget_95)
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_89.setObjectName("horizontalLayout_89")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.frame_48 = QtWidgets.QFrame(self.layoutWidget_95)
        self.frame_48.setStyleSheet("#frame_48{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.layoutWidget_51 = QtWidgets.QWidget(self.frame_48)
        self.layoutWidget_51.setGeometry(QtCore.QRect(10, 5, 118, 59))
        self.layoutWidget_51.setObjectName("layoutWidget_51")
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout(self.layoutWidget_51)
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_44.setSpacing(2)
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        self.textBrowser_R3_Currentfee = QtWidgets.QTextBrowser(self.layoutWidget_51)
        self.textBrowser_R3_Currentfee.setStyleSheet("")
        self.textBrowser_R3_Currentfee.setObjectName("textBrowser_R3_Currentfee")
        self.horizontalLayout_44.addWidget(self.textBrowser_R3_Currentfee)
        self.textBrowser_Room3_Currentfee = QtWidgets.QTextBrowser(self.layoutWidget_51)
        self.textBrowser_Room3_Currentfee.setReadOnly(False)
        self.textBrowser_Room3_Currentfee.setObjectName("textBrowser_Room3_Currentfee")
        self.horizontalLayout_44.addWidget(self.textBrowser_Room3_Currentfee)
        self.horizontalLayout_19.addWidget(self.frame_48)
        self.frame_49 = QtWidgets.QFrame(self.layoutWidget_95)
        self.frame_49.setStyleSheet("#frame_49{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_49.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_49.setObjectName("frame_49")
        self.layoutWidget_52 = QtWidgets.QWidget(self.frame_49)
        self.layoutWidget_52.setGeometry(QtCore.QRect(10, 5, 117, 59))
        self.layoutWidget_52.setObjectName("layoutWidget_52")
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout(self.layoutWidget_52)
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_45.setSpacing(1)
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.textBrowser_R3_Totalfee = QtWidgets.QTextBrowser(self.layoutWidget_52)
        self.textBrowser_R3_Totalfee.setObjectName("textBrowser_R3_Totalfee")
        self.horizontalLayout_45.addWidget(self.textBrowser_R3_Totalfee)
        self.textBrowser_Room3_Totalfee = QtWidgets.QTextBrowser(self.layoutWidget_52)
        self.textBrowser_Room3_Totalfee.setReadOnly(False)
        self.textBrowser_Room3_Totalfee.setObjectName("textBrowser_Room3_Totalfee")
        self.horizontalLayout_45.addWidget(self.textBrowser_Room3_Totalfee)
        self.horizontalLayout_19.addWidget(self.frame_49)
        self.horizontalLayout_89.addLayout(self.horizontalLayout_19)
        self.verticalLayout_32.addWidget(self.frame_167)
        self.verticalLayout_31.addWidget(self.frame_164)
        self.horizontalLayout_3.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.layoutWidget_6)
        self.frame_11.setStyleSheet("background-color: rgb(255, 242, 235);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.layoutWidget_53 = QtWidgets.QWidget(self.frame_11)
        self.layoutWidget_53.setGeometry(QtCore.QRect(0, 0, 201, 171))
        self.layoutWidget_53.setObjectName("layoutWidget_53")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.layoutWidget_53)
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.frame_168 = QtWidgets.QFrame(self.layoutWidget_53)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_168.sizePolicy().hasHeightForWidth())
        self.frame_168.setSizePolicy(sizePolicy)
        self.frame_168.setStyleSheet("#frame_168{\n"
"    background-color: rgb(255, 205, 198);\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_168.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_168.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_168.setObjectName("frame_168")
        self.layoutWidget_96 = QtWidgets.QWidget(self.frame_168)
        self.layoutWidget_96.setGeometry(QtCore.QRect(10, 10, 181, 22))
        self.layoutWidget_96.setObjectName("layoutWidget_96")
        self.horizontalLayout_90 = QtWidgets.QHBoxLayout(self.layoutWidget_96)
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_90.setSpacing(0)
        self.horizontalLayout_90.setObjectName("horizontalLayout_90")
        self.ROOM4 = QtWidgets.QLabel(self.layoutWidget_96)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ROOM4.sizePolicy().hasHeightForWidth())
        self.ROOM4.setSizePolicy(sizePolicy)
        self.ROOM4.setStyleSheet("background-color: rgb(255, 205, 198);")
        self.ROOM4.setObjectName("ROOM4")
        self.horizontalLayout_90.addWidget(self.ROOM4)
        self.verticalLayout_33.addWidget(self.frame_168)
        self.frame_169 = QtWidgets.QFrame(self.layoutWidget_53)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.frame_169.sizePolicy().hasHeightForWidth())
        self.frame_169.setSizePolicy(sizePolicy)
        self.frame_169.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_169.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_169.setObjectName("frame_169")
        self.layoutWidget_97 = QtWidgets.QWidget(self.frame_169)
        self.layoutWidget_97.setGeometry(QtCore.QRect(0, 0, 201, 141))
        self.layoutWidget_97.setObjectName("layoutWidget_97")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.layoutWidget_97)
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.frame_170 = QtWidgets.QFrame(self.layoutWidget_97)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_170.sizePolicy().hasHeightForWidth())
        self.frame_170.setSizePolicy(sizePolicy)
        self.frame_170.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_170.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_170.setObjectName("frame_170")
        self.layoutWidget_24 = QtWidgets.QWidget(self.frame_170)
        self.layoutWidget_24.setGeometry(QtCore.QRect(0, 0, 201, 41))
        self.layoutWidget_24.setObjectName("layoutWidget_24")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.layoutWidget_24)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_32 = QtWidgets.QFrame(self.layoutWidget_24)
        self.frame_32.setStyleSheet("#frame_32{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.layoutWidget_36 = QtWidgets.QWidget(self.frame_32)
        self.layoutWidget_36.setGeometry(QtCore.QRect(10, 5, 116, 59))
        self.layoutWidget_36.setObjectName("layoutWidget_36")
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout(self.layoutWidget_36)
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.textBrowser_R4_state = QtWidgets.QTextBrowser(self.layoutWidget_36)
        self.textBrowser_R4_state.setStyleSheet("")
        self.textBrowser_R4_state.setObjectName("textBrowser_R4_state")
        self.horizontalLayout_47.addWidget(self.textBrowser_R4_state)
        self.textBrowser_Room4_state = QtWidgets.QTextBrowser(self.layoutWidget_36)
        self.textBrowser_Room4_state.setReadOnly(False)
        self.textBrowser_Room4_state.setObjectName("textBrowser_Room4_state")
        self.horizontalLayout_47.addWidget(self.textBrowser_Room4_state)
        self.horizontalLayout_12.addWidget(self.frame_32)
        self.frame_33 = QtWidgets.QFrame(self.layoutWidget_24)
        self.frame_33.setStyleSheet("#frame_33{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.layoutWidget_37 = QtWidgets.QWidget(self.frame_33)
        self.layoutWidget_37.setGeometry(QtCore.QRect(10, 5, 116, 59))
        self.layoutWidget_37.setObjectName("layoutWidget_37")
        self.horizontalLayout_48 = QtWidgets.QHBoxLayout(self.layoutWidget_37)
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        self.textBrowser_R4_mode = QtWidgets.QTextBrowser(self.layoutWidget_37)
        self.textBrowser_R4_mode.setObjectName("textBrowser_R4_mode")
        self.horizontalLayout_48.addWidget(self.textBrowser_R4_mode)
        self.textBrowser_Room4_mode = QtWidgets.QTextBrowser(self.layoutWidget_37)
        self.textBrowser_Room4_mode.setReadOnly(False)
        self.textBrowser_Room4_mode.setObjectName("textBrowser_Room4_mode")
        self.horizontalLayout_48.addWidget(self.textBrowser_Room4_mode)
        self.horizontalLayout_12.addWidget(self.frame_33)
        self.verticalLayout_34.addWidget(self.frame_170)
        self.frame_171 = QtWidgets.QFrame(self.layoutWidget_97)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_171.sizePolicy().hasHeightForWidth())
        self.frame_171.setSizePolicy(sizePolicy)
        self.frame_171.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_171.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_171.setObjectName("frame_171")
        self.layoutWidget_25 = QtWidgets.QWidget(self.frame_171)
        self.layoutWidget_25.setGeometry(QtCore.QRect(0, 0, 201, 41))
        self.layoutWidget_25.setObjectName("layoutWidget_25")
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout(self.layoutWidget_25)
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.frame_50 = QtWidgets.QFrame(self.layoutWidget_25)
        self.frame_50.setStyleSheet("#frame_50{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.layoutWidget_54 = QtWidgets.QWidget(self.frame_50)
        self.layoutWidget_54.setGeometry(QtCore.QRect(10, 5, 116, 59))
        self.layoutWidget_54.setObjectName("layoutWidget_54")
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout(self.layoutWidget_54)
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.textBrowser_R4_tem = QtWidgets.QTextBrowser(self.layoutWidget_54)
        self.textBrowser_R4_tem.setObjectName("textBrowser_R4_tem")
        self.horizontalLayout_50.addWidget(self.textBrowser_R4_tem)
        self.textBrowser_Room4_tem = QtWidgets.QTextBrowser(self.layoutWidget_54)
        self.textBrowser_Room4_tem.setReadOnly(False)
        self.textBrowser_Room4_tem.setObjectName("textBrowser_Room4_tem")
        self.horizontalLayout_50.addWidget(self.textBrowser_Room4_tem)
        self.horizontalLayout_49.addWidget(self.frame_50)
        self.frame_51 = QtWidgets.QFrame(self.layoutWidget_25)
        self.frame_51.setStyleSheet("#frame_51{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.layoutWidget_55 = QtWidgets.QWidget(self.frame_51)
        self.layoutWidget_55.setGeometry(QtCore.QRect(10, 5, 116, 59))
        self.layoutWidget_55.setObjectName("layoutWidget_55")
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout(self.layoutWidget_55)
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.textBrowser_R4_WindSpeed = QtWidgets.QTextBrowser(self.layoutWidget_55)
        self.textBrowser_R4_WindSpeed.setObjectName("textBrowser_R4_WindSpeed")
        self.horizontalLayout_51.addWidget(self.textBrowser_R4_WindSpeed)
        self.textBrowser_Room4_WindSpeed = QtWidgets.QTextBrowser(self.layoutWidget_55)
        self.textBrowser_Room4_WindSpeed.setReadOnly(False)
        self.textBrowser_Room4_WindSpeed.setObjectName("textBrowser_Room4_WindSpeed")
        self.horizontalLayout_51.addWidget(self.textBrowser_Room4_WindSpeed)
        self.horizontalLayout_49.addWidget(self.frame_51)
        self.verticalLayout_34.addWidget(self.frame_171)
        self.frame_172 = QtWidgets.QFrame(self.layoutWidget_97)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_172.sizePolicy().hasHeightForWidth())
        self.frame_172.setSizePolicy(sizePolicy)
        self.frame_172.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_172.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_172.setObjectName("frame_172")
        self.layoutWidget_98 = QtWidgets.QWidget(self.frame_172)
        self.layoutWidget_98.setGeometry(QtCore.QRect(0, 0, 201, 51))
        self.layoutWidget_98.setObjectName("layoutWidget_98")
        self.horizontalLayout_91 = QtWidgets.QHBoxLayout(self.layoutWidget_98)
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_91.setObjectName("horizontalLayout_91")
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.frame_52 = QtWidgets.QFrame(self.layoutWidget_98)
        self.frame_52.setStyleSheet("#frame_52{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.layoutWidget_56 = QtWidgets.QWidget(self.frame_52)
        self.layoutWidget_56.setGeometry(QtCore.QRect(10, 5, 118, 59))
        self.layoutWidget_56.setObjectName("layoutWidget_56")
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout(self.layoutWidget_56)
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_53.setSpacing(2)
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.textBrowser_R4_Currentfee = QtWidgets.QTextBrowser(self.layoutWidget_56)
        self.textBrowser_R4_Currentfee.setStyleSheet("")
        self.textBrowser_R4_Currentfee.setObjectName("textBrowser_R4_Currentfee")
        self.horizontalLayout_53.addWidget(self.textBrowser_R4_Currentfee)
        self.textBrowser_Room4_Currentfee = QtWidgets.QTextBrowser(self.layoutWidget_56)
        self.textBrowser_Room4_Currentfee.setReadOnly(False)
        self.textBrowser_Room4_Currentfee.setObjectName("textBrowser_Room4_Currentfee")
        self.horizontalLayout_53.addWidget(self.textBrowser_Room4_Currentfee)
        self.horizontalLayout_52.addWidget(self.frame_52)
        self.frame_53 = QtWidgets.QFrame(self.layoutWidget_98)
        self.frame_53.setStyleSheet("#frame_53{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.layoutWidget_57 = QtWidgets.QWidget(self.frame_53)
        self.layoutWidget_57.setGeometry(QtCore.QRect(10, 5, 117, 59))
        self.layoutWidget_57.setObjectName("layoutWidget_57")
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout(self.layoutWidget_57)
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_54.setSpacing(1)
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.textBrowser_R4_Totalfee = QtWidgets.QTextBrowser(self.layoutWidget_57)
        self.textBrowser_R4_Totalfee.setObjectName("textBrowser_R4_Totalfee")
        self.horizontalLayout_54.addWidget(self.textBrowser_R4_Totalfee)
        self.textBrowser_Room4_Totalfee = QtWidgets.QTextBrowser(self.layoutWidget_57)
        self.textBrowser_Room4_Totalfee.setReadOnly(False)
        self.textBrowser_Room4_Totalfee.setObjectName("textBrowser_Room4_Totalfee")
        self.horizontalLayout_54.addWidget(self.textBrowser_Room4_Totalfee)
        self.horizontalLayout_52.addWidget(self.frame_53)
        self.horizontalLayout_91.addLayout(self.horizontalLayout_52)
        self.verticalLayout_34.addWidget(self.frame_172)
        self.verticalLayout_33.addWidget(self.frame_169)
        self.horizontalLayout_3.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.layoutWidget_6)
        self.frame_12.setStyleSheet("background-color: rgb(255, 242, 235);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.layoutWidget_58 = QtWidgets.QWidget(self.frame_12)
        self.layoutWidget_58.setGeometry(QtCore.QRect(0, 0, 201, 171))
        self.layoutWidget_58.setObjectName("layoutWidget_58")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.layoutWidget_58)
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.frame_173 = QtWidgets.QFrame(self.layoutWidget_58)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_173.sizePolicy().hasHeightForWidth())
        self.frame_173.setSizePolicy(sizePolicy)
        self.frame_173.setStyleSheet("#frame_173{\n"
"    background-color: rgb(255, 205, 198);\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_173.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_173.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_173.setObjectName("frame_173")
        self.layoutWidget_99 = QtWidgets.QWidget(self.frame_173)
        self.layoutWidget_99.setGeometry(QtCore.QRect(10, 10, 181, 22))
        self.layoutWidget_99.setObjectName("layoutWidget_99")
        self.horizontalLayout_92 = QtWidgets.QHBoxLayout(self.layoutWidget_99)
        self.horizontalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_92.setSpacing(0)
        self.horizontalLayout_92.setObjectName("horizontalLayout_92")
        self.ROOM5 = QtWidgets.QLabel(self.layoutWidget_99)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ROOM5.sizePolicy().hasHeightForWidth())
        self.ROOM5.setSizePolicy(sizePolicy)
        self.ROOM5.setStyleSheet("background-color: rgb(255, 205, 198);")
        self.ROOM5.setObjectName("ROOM5")
        self.horizontalLayout_92.addWidget(self.ROOM5)
        self.verticalLayout_35.addWidget(self.frame_173)
        self.frame_174 = QtWidgets.QFrame(self.layoutWidget_58)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.frame_174.sizePolicy().hasHeightForWidth())
        self.frame_174.setSizePolicy(sizePolicy)
        self.frame_174.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_174.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_174.setObjectName("frame_174")
        self.layoutWidget_100 = QtWidgets.QWidget(self.frame_174)
        self.layoutWidget_100.setGeometry(QtCore.QRect(0, 0, 201, 141))
        self.layoutWidget_100.setObjectName("layoutWidget_100")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.layoutWidget_100)
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.frame_175 = QtWidgets.QFrame(self.layoutWidget_100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_175.sizePolicy().hasHeightForWidth())
        self.frame_175.setSizePolicy(sizePolicy)
        self.frame_175.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_175.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_175.setObjectName("frame_175")
        self.layoutWidget_59 = QtWidgets.QWidget(self.frame_175)
        self.layoutWidget_59.setGeometry(QtCore.QRect(0, 0, 201, 41))
        self.layoutWidget_59.setObjectName("layoutWidget_59")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.layoutWidget_59)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_54 = QtWidgets.QFrame(self.layoutWidget_59)
        self.frame_54.setStyleSheet("#frame_54{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_54.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_54.setObjectName("frame_54")
        self.layoutWidget_60 = QtWidgets.QWidget(self.frame_54)
        self.layoutWidget_60.setGeometry(QtCore.QRect(10, 5, 116, 59))
        self.layoutWidget_60.setObjectName("layoutWidget_60")
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout(self.layoutWidget_60)
        self.horizontalLayout_56.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.textBrowser_R5_state = QtWidgets.QTextBrowser(self.layoutWidget_60)
        self.textBrowser_R5_state.setStyleSheet("")
        self.textBrowser_R5_state.setObjectName("textBrowser_R5_state")
        self.horizontalLayout_56.addWidget(self.textBrowser_R5_state)
        self.textBrowser_Room5_state = QtWidgets.QTextBrowser(self.layoutWidget_60)
        self.textBrowser_Room5_state.setReadOnly(False)
        self.textBrowser_Room5_state.setObjectName("textBrowser_Room5_state")
        self.horizontalLayout_56.addWidget(self.textBrowser_Room5_state)
        self.horizontalLayout_13.addWidget(self.frame_54)
        self.frame_55 = QtWidgets.QFrame(self.layoutWidget_59)
        self.frame_55.setStyleSheet("#frame_55{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_55.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_55.setObjectName("frame_55")
        self.layoutWidget_61 = QtWidgets.QWidget(self.frame_55)
        self.layoutWidget_61.setGeometry(QtCore.QRect(10, 5, 116, 59))
        self.layoutWidget_61.setObjectName("layoutWidget_61")
        self.horizontalLayout_60 = QtWidgets.QHBoxLayout(self.layoutWidget_61)
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName("horizontalLayout_60")
        self.textBrowser_R5_mode = QtWidgets.QTextBrowser(self.layoutWidget_61)
        self.textBrowser_R5_mode.setObjectName("textBrowser_R5_mode")
        self.horizontalLayout_60.addWidget(self.textBrowser_R5_mode)
        self.textBrowser_Room5_mode = QtWidgets.QTextBrowser(self.layoutWidget_61)
        self.textBrowser_Room5_mode.setReadOnly(False)
        self.textBrowser_Room5_mode.setObjectName("textBrowser_Room5_mode")
        self.horizontalLayout_60.addWidget(self.textBrowser_Room5_mode)
        self.horizontalLayout_13.addWidget(self.frame_55)
        self.verticalLayout_36.addWidget(self.frame_175)
        self.frame_176 = QtWidgets.QFrame(self.layoutWidget_100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_176.sizePolicy().hasHeightForWidth())
        self.frame_176.setSizePolicy(sizePolicy)
        self.frame_176.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_176.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_176.setObjectName("frame_176")
        self.layoutWidget_62 = QtWidgets.QWidget(self.frame_176)
        self.layoutWidget_62.setGeometry(QtCore.QRect(0, 0, 201, 41))
        self.layoutWidget_62.setObjectName("layoutWidget_62")
        self.horizontalLayout_61 = QtWidgets.QHBoxLayout(self.layoutWidget_62)
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName("horizontalLayout_61")
        self.frame_56 = QtWidgets.QFrame(self.layoutWidget_62)
        self.frame_56.setStyleSheet("#frame_56{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_56.setObjectName("frame_56")
        self.layoutWidget_63 = QtWidgets.QWidget(self.frame_56)
        self.layoutWidget_63.setGeometry(QtCore.QRect(10, 5, 116, 59))
        self.layoutWidget_63.setObjectName("layoutWidget_63")
        self.horizontalLayout_62 = QtWidgets.QHBoxLayout(self.layoutWidget_63)
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName("horizontalLayout_62")
        self.textBrowser_R5_tem = QtWidgets.QTextBrowser(self.layoutWidget_63)
        self.textBrowser_R5_tem.setObjectName("textBrowser_R5_tem")
        self.horizontalLayout_62.addWidget(self.textBrowser_R5_tem)
        self.textBrowser_Room5_tem = QtWidgets.QTextBrowser(self.layoutWidget_63)
        self.textBrowser_Room5_tem.setReadOnly(False)
        self.textBrowser_Room5_tem.setObjectName("textBrowser_Room5_tem")
        self.horizontalLayout_62.addWidget(self.textBrowser_Room5_tem)
        self.horizontalLayout_61.addWidget(self.frame_56)
        self.frame_57 = QtWidgets.QFrame(self.layoutWidget_62)
        self.frame_57.setStyleSheet("#frame_57{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_57.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_57.setObjectName("frame_57")
        self.layoutWidget_64 = QtWidgets.QWidget(self.frame_57)
        self.layoutWidget_64.setGeometry(QtCore.QRect(10, 5, 116, 59))
        self.layoutWidget_64.setObjectName("layoutWidget_64")
        self.horizontalLayout_63 = QtWidgets.QHBoxLayout(self.layoutWidget_64)
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName("horizontalLayout_63")
        self.textBrowser_R5_WindSpeed = QtWidgets.QTextBrowser(self.layoutWidget_64)
        self.textBrowser_R5_WindSpeed.setObjectName("textBrowser_R5_WindSpeed")
        self.horizontalLayout_63.addWidget(self.textBrowser_R5_WindSpeed)
        self.textBrowser_Room5_WindSpeed = QtWidgets.QTextBrowser(self.layoutWidget_64)
        self.textBrowser_Room5_WindSpeed.setReadOnly(False)
        self.textBrowser_Room5_WindSpeed.setObjectName("textBrowser_Room5_WindSpeed")
        self.horizontalLayout_63.addWidget(self.textBrowser_Room5_WindSpeed)
        self.horizontalLayout_61.addWidget(self.frame_57)
        self.verticalLayout_36.addWidget(self.frame_176)
        self.frame_177 = QtWidgets.QFrame(self.layoutWidget_100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_177.sizePolicy().hasHeightForWidth())
        self.frame_177.setSizePolicy(sizePolicy)
        self.frame_177.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_177.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_177.setObjectName("frame_177")
        self.layoutWidget_101 = QtWidgets.QWidget(self.frame_177)
        self.layoutWidget_101.setGeometry(QtCore.QRect(0, 0, 201, 51))
        self.layoutWidget_101.setObjectName("layoutWidget_101")
        self.horizontalLayout_93 = QtWidgets.QHBoxLayout(self.layoutWidget_101)
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_93.setObjectName("horizontalLayout_93")
        self.horizontalLayout_64 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName("horizontalLayout_64")
        self.frame_58 = QtWidgets.QFrame(self.layoutWidget_101)
        self.frame_58.setStyleSheet("#frame_58{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_58.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_58.setObjectName("frame_58")
        self.layoutWidget_65 = QtWidgets.QWidget(self.frame_58)
        self.layoutWidget_65.setGeometry(QtCore.QRect(10, 5, 118, 59))
        self.layoutWidget_65.setObjectName("layoutWidget_65")
        self.horizontalLayout_65 = QtWidgets.QHBoxLayout(self.layoutWidget_65)
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_65.setSpacing(2)
        self.horizontalLayout_65.setObjectName("horizontalLayout_65")
        self.textBrowser_R5_Currentfee = QtWidgets.QTextBrowser(self.layoutWidget_65)
        self.textBrowser_R5_Currentfee.setStyleSheet("")
        self.textBrowser_R5_Currentfee.setObjectName("textBrowser_R5_Currentfee")
        self.horizontalLayout_65.addWidget(self.textBrowser_R5_Currentfee)
        self.textBrowser_Room5_Currentfee = QtWidgets.QTextBrowser(self.layoutWidget_65)
        self.textBrowser_Room5_Currentfee.setReadOnly(False)
        self.textBrowser_Room5_Currentfee.setObjectName("textBrowser_Room5_Currentfee")
        self.horizontalLayout_65.addWidget(self.textBrowser_Room5_Currentfee)
        self.horizontalLayout_64.addWidget(self.frame_58)
        self.frame_59 = QtWidgets.QFrame(self.layoutWidget_101)
        self.frame_59.setStyleSheet("#frame_59{\n"
"border-radius:10px;\n"
"border:1px solid black\n"
"}")
        self.frame_59.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_59.setObjectName("frame_59")
        self.layoutWidget_66 = QtWidgets.QWidget(self.frame_59)
        self.layoutWidget_66.setGeometry(QtCore.QRect(10, 5, 117, 59))
        self.layoutWidget_66.setObjectName("layoutWidget_66")
        self.horizontalLayout_66 = QtWidgets.QHBoxLayout(self.layoutWidget_66)
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_66.setSpacing(1)
        self.horizontalLayout_66.setObjectName("horizontalLayout_66")
        self.textBrowser_R5_Totalfee = QtWidgets.QTextBrowser(self.layoutWidget_66)
        self.textBrowser_R5_Totalfee.setObjectName("textBrowser_R5_Totalfee")
        self.horizontalLayout_66.addWidget(self.textBrowser_R5_Totalfee)
        self.textBrowser_Room5_Totalfee = QtWidgets.QTextBrowser(self.layoutWidget_66)
        self.textBrowser_Room5_Totalfee.setReadOnly(False)
        self.textBrowser_Room5_Totalfee.setObjectName("textBrowser_Room5_Totalfee")
        self.horizontalLayout_66.addWidget(self.textBrowser_Room5_Totalfee)
        self.horizontalLayout_64.addWidget(self.frame_59)
        self.horizontalLayout_93.addLayout(self.horizontalLayout_64)
        self.verticalLayout_36.addWidget(self.frame_177)
        self.verticalLayout_35.addWidget(self.frame_174)
        self.horizontalLayout_3.addWidget(self.frame_12)
        self.verticalLayout.addWidget(self.frame_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Arial Black\'; font-size:12pt; color:#070707;\">Administrator interface</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#070707;\">计费费率</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "\n"
"\n"
"<html><head/><body><p><span style=\" font-family:\'Arial Black\'; font-size:9pt; font-weight:400; color:#070707;\">元/℃</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'微软雅黑\'; font-size:11pt; font-weight:600; color:#070707;\">温度区间</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Arial Black\'; font-size:13pt; color:#070707;\">℃</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Arial Black\'; font-size:13pt; font-weight:400; color:#070707;\">℃</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">总开关</span></p></body></html>"))
        self.ROOM1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Arial Black\'; font-size:10pt; color:#070707;\">Room 1</span></p></body></html>"))
        self.textBrowser_R1_state.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">状态</span></p></body></html>"))
        self.textBrowser_Room1_state.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">开机</span></p></body></html>"))
        self.textBrowser_R1_mode.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">模式</span></p></body></html>"))
        self.textBrowser_Room1_mode.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">制冷</span></p></body></html>"))
        self.textBrowser_R1_tem.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">温度</span></p></body></html>"))
        self.textBrowser_Room1_tem.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">32</span></p></body></html>"))
        self.textBrowser_R1_WindSpeed.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">风速</span></p></body></html>"))
        self.textBrowser_Room1_WindSpeed.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_R1_Currentfee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">当前</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">费用</span></p></body></html>"))
        self.textBrowser_Room1_Currentfee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">0</span></p></body></html>"))
        self.textBrowser_R1_Totalfee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">总</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">费用</span></p></body></html>"))
        self.textBrowser_Room1_Totalfee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">0</span></p></body></html>"))
        self.ROOM2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Arial Black\'; font-size:10pt; color:#070707;\">Room 2</span></p></body></html>"))
        self.textBrowser_R2_state.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">状态</span></p></body></html>"))
        self.textBrowser_Room2_state.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">开机</span></p></body></html>"))
        self.textBrowser_R2_mode.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">模式</span></p></body></html>"))
        self.textBrowser_Room2_mode.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">制冷</span></p></body></html>"))
        self.textBrowser_R2_tem.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">温度</span></p></body></html>"))
        self.textBrowser_Room2_tem.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">32</span></p></body></html>"))
        self.textBrowser_R2_WindSpeed.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">风速</span></p></body></html>"))
        self.textBrowser_Room2_WindSpeed.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_R2_Currentfee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">当前</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">费用</span></p></body></html>"))
        self.textBrowser_Room2_Currentfee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">0</span></p></body></html>"))
        self.textBrowser_R2_Totalfee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">总</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">费用</span></p></body></html>"))
        self.textBrowser_Room2_Totalfee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">0</span></p></body></html>"))
        self.ROOM3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Arial Black\'; font-size:10pt; color:#070707;\">Room 3</span></p></body></html>"))
        self.textBrowser_R3_state.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">状态</span></p></body></html>"))
        self.textBrowser_Room3_state.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">开机</span></p></body></html>"))
        self.textBrowser_R3_mode.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">模式</span></p></body></html>"))
        self.textBrowser_Room3_mode.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">制冷</span></p></body></html>"))
        self.textBrowser_R3_tem.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">温度</span></p></body></html>"))
        self.textBrowser_Room3_tem.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">32</span></p></body></html>"))
        self.textBrowser_R3_WindSpeed.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">风速</span></p></body></html>"))
        self.textBrowser_Room3_WindSpeed.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_R3_Currentfee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">当前</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">费用</span></p></body></html>"))
        self.textBrowser_Room3_Currentfee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">0</span></p></body></html>"))
        self.textBrowser_R3_Totalfee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">总</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">费用</span></p></body></html>"))
        self.textBrowser_Room3_Totalfee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">0</span></p></body></html>"))
        self.ROOM4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Arial Black\'; font-size:10pt; color:#070707;\">Room 4</span></p></body></html>"))
        self.textBrowser_R4_state.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">状态</span></p></body></html>"))
        self.textBrowser_Room4_state.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">开机</span></p></body></html>"))
        self.textBrowser_R4_mode.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">模式</span></p></body></html>"))
        self.textBrowser_Room4_mode.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">制冷</span></p></body></html>"))
        self.textBrowser_R4_tem.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">温度</span></p></body></html>"))
        self.textBrowser_Room4_tem.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">32</span></p></body></html>"))
        self.textBrowser_R4_WindSpeed.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">风速</span></p></body></html>"))
        self.textBrowser_Room4_WindSpeed.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_R4_Currentfee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">当前</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">费用</span></p></body></html>"))
        self.textBrowser_Room4_Currentfee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">0</span></p></body></html>"))
        self.textBrowser_R4_Totalfee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">总</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">费用</span></p></body></html>"))
        self.textBrowser_Room4_Totalfee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">0</span></p></body></html>"))
        self.ROOM5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Arial Black\'; font-size:10pt; color:#070707;\">Room 5</span></p></body></html>"))
        self.textBrowser_R5_state.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">状态</span></p></body></html>"))
        self.textBrowser_Room5_state.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">开机</span></p></body></html>"))
        self.textBrowser_R5_mode.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">模式</span></p></body></html>"))
        self.textBrowser_Room5_mode.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">制冷</span></p></body></html>"))
        self.textBrowser_R5_tem.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">温度</span></p></body></html>"))
        self.textBrowser_Room5_tem.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">32</span></p></body></html>"))
        self.textBrowser_R5_WindSpeed.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">风速</span></p></body></html>"))
        self.textBrowser_Room5_WindSpeed.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_R5_Currentfee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">当前</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">费用</span></p></body></html>"))
        self.textBrowser_Room5_Currentfee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">0</span></p></body></html>"))
        self.textBrowser_R5_Totalfee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">总</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:600;\">费用</span></p></body></html>"))
        self.textBrowser_Room5_Totalfee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:8pt;\">0</span></p></body></html>"))

import picture_rc
