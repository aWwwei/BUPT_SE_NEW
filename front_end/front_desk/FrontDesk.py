'''
@ 文件名：FrontDesk.py
@ 文件功能描述：前台界面显示
@ 创建人：孟祥超
@ 创建日期：2023年12月8日


@ 修改描述：调整表格在输出框中的显示：位置适中且能完全显示数据
@ 修改人：孟祥超
@ 修改日期：2023年12月10日

@ 修改描述：调整输出框大小
@ 修改人：孟祥超
@ 修改日期：2023年12月10日

@ 修改描述：添加通信功能：request获取信息
@ 修改人：孟祥超、田健豪
@ 修改日期：2023年12月11日

@ 修改描述：界面美化：调整字体、背景色和美化按钮样式等
@ 修改人：孟祥超、杨欣悦
@ 修改日期：2023年12月13日

@ 修改描述：固定显示界面窗口大小
@ 修改人：孟祥超
@ 修改日期：2023年12月14日

@ 修改描述：添加界面图标
@ 修改人：田健豪
@ 修改日期：2023年12月15日

@ 修改描述：修改表格和窗口大小
@ 修改人：田健豪
@ 修改日期：2023年12月15日
'''

import requests
from PyQt5.QtWidgets import QWidget, QMessageBox

import login
from PyQt5 import QtCore, QtGui, QtWidgets
#导入用于显示在界面中的图片
import photo_rc

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1060, 547) #设置窗口固定大小
        # 取消最大化按钮
        flags = QtCore.Qt.WindowFlags(
            QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        Form.setWindowFlags(flags)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setStyleSheet("background-color: rgb(230, 245, 255);")
        self.tableView = QtWidgets.QTableView(Form)
        #表格大小
        self.tableView.setGeometry(QtCore.QRect(150, 200, 890, 291))
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.verticalHeader().setVisible(False)
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
        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(30, 360, 101, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("\n"
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
        self.pushButton_1.setObjectName("pushButton")
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
"QPushButton_1:hover {\n"
"\n"
"border:2px outset rgba(36, 36, 36,0);\n"
"}\n"
"QPushButton_1:pressed {\n"
"\n"
"border:4px outset rgba(36, 36, 36,0);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(320, 30, 421, 171))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("AirCondition.jpg"))
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(60, 40, 181, 141))
        self.frame_2.setStyleSheet("image: url(:/前台/前台2.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2.raise_()
        self.pushButton_1.raise_()
        self.pushButton_2.raise_()
        self.label_3.raise_()
        self.tableView.raise_()
        self.room_id.raise_()
        self.frame_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 将窗口在屏幕正中央显示
        qr = Form.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        Form.move(qr.topLeft())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">房间号：</span></p></body></html>"))
        self.pushButton_1.setText(_translate("Form", "输出账单"))
        self.pushButton_2.setText(_translate("Form", "输出详单"))
        Form.setWindowIcon(QtGui.QIcon('front_desk_logo.png'))



class MyForm(Ui_Form,QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 绑定按钮的点击事件与槽函数
        self.pushButton_1.clicked.connect(self.display_bill)
        self.pushButton_2.clicked.connect(self.display_details)


    def display_bill(self):
        # 在输出表格框内显示第一个表格的逻辑
        # 可以使用QStandardItemModel和QTableView来显示表格
        table_model = QtGui.QStandardItemModel()
        table_model.setColumnCount(2)
        table_model.setRowCount(4)

        # 获取输入框中的房间号
        room_id = self.room_id.text()
        table_model.setItem(0, 0, QtGui.QStandardItem('房间号'))
        table_model.setItem(0, 1, QtGui.QStandardItem(room_id))
        table_model.setItem(1, 0, QtGui.QStandardItem('入住时间'))
        table_model.setItem(2, 0, QtGui.QStandardItem('离开时间'))
        table_model.setItem(3, 0, QtGui.QStandardItem('总费用'))

        # 添加可变参数到表格

        response = requests.post("http://127.0.0.1:5000/print_bill", data={"room_id":room_id})
        bill = response.json()['bill']
        args1 = bill["入住时间"]
        args2 = bill["离开时间"]
        args3 = bill["总费用"]

        table_model.setItem(1, 1, QtGui.QStandardItem(str(args1[0])))
        table_model.setItem(2, 1, QtGui.QStandardItem(str(args2[0])))
        table_model.setItem(3, 1, QtGui.QStandardItem(str(args3[0])))

        self.tableView.setModel(table_model)
        # 调整表格的大小
        self.tableView.resizeColumnsToContents()
        self.tableView.resizeRowsToContents()
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def display_details(self):
        # 在输出表格框内显示第二个表格的逻辑
        # 同样使用QStandardItemModel和QTableView来显示表格
        table_model = QtGui.QStandardItemModel()

        # 获取输入框中的房间号
        room_id = self.room_id.text()
        table_model.setItem(0, 0, QtGui.QStandardItem('房间号'))
        table_model.setItem(0, 1, QtGui.QStandardItem('请求时间'))
        table_model.setItem(0, 2, QtGui.QStandardItem('服务开始时间'))
        table_model.setItem(0, 3, QtGui.QStandardItem('结束服务时间'))
        table_model.setItem(0, 4, QtGui.QStandardItem('服务时长'))
        table_model.setItem(0, 5, QtGui.QStandardItem('风速'))
        table_model.setItem(0, 6, QtGui.QStandardItem('当前费用'))
        table_model.setItem(0, 7, QtGui.QStandardItem('费率'))

        # 添加可变参数到表格
        response = requests.post("http://127.0.0.1:5000/print_details", data={"room_id":room_id})
        details = response.json()['bill']
        args1 = details["请求时间"]
        args2 = details["服务开始时间"]
        args3 = details["服务结束时间"]
        args4 = details["服务时长"]
        args5 = details["风速"]
        args6 = details["当前费用"]
        args7 = details["费率"]
        #读取每行数据填入表格
        for i in range(len(args1)):
            table_model.setItem(i + 1, 0, QtGui.QStandardItem(room_id))
            table_model.setItem(i + 1, 1, QtGui.QStandardItem(str(args1[i])))
            table_model.setItem(i + 1, 2, QtGui.QStandardItem(str(args2[i])))
            table_model.setItem(i + 1, 3, QtGui.QStandardItem(str(args3[i])))
            table_model.setItem(i + 1, 4, QtGui.QStandardItem(str(args4[i])))
            table_model.setItem(i + 1, 5, QtGui.QStandardItem(str(args5[i])))
            table_model.setItem(i + 1, 6, QtGui.QStandardItem(str(args6[i])))
            table_model.setItem(i + 1, 7, QtGui.QStandardItem(str(args7[i])))

        self.tableView.setModel(table_model)
        #取消滑轮功能
        self.tableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #调整表格的列宽和行高，使其适应内容的大小
        self.tableView.resizeColumnsToContents()
        self.tableView.resizeRowsToContents()
        # 将水平表头的列自动调整为适应QTableView的宽度，使其充满整个可用空间。
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)


class LoginWindow(QWidget, login.Ui_login_window):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.slot_init()

    def slot_init(self):
        self.login_button.clicked.connect(self.login)

    def login(self):
        # 在这里添加您的登录逻辑
        username_input = self.username_edit.text()
        password_input = self.password_edit.text()

        if username_input == "":
            QMessageBox.warning(self, '警告', '用户名不能为空，请输入！', QMessageBox.Yes)

        elif password_input == "":
            QMessageBox.warning(self, '警告', '密码不能为空，请输入！', QMessageBox.Yes)
        else:
            data = requests.post(f"http://127.0.0.1:5000/login", data={
                "username": username_input,
                "password_input": password_input
            })
            if data.status_code == 200:

                self.new_window = MyForm()
                self.new_window.show()
                self.close()
            else:
                QMessageBox.critical(self, '错误', '用户名或密码错误！')


# 创建应用程序并运行
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())