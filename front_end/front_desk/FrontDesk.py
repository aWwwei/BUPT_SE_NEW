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



@ 修改描述：添加界面图标
@ 修改人：田健豪
@ 修改日期：2023年12月15日

@ 修改描述：修改表格和窗口大小
@ 修改人：田健豪
@ 修改日期：2023年12月15日

@ 修改描述：增加登录界面和登录逻辑
@ 修改人：田健豪
@ 修改日期：2023年12月16日

@ 修改描述：增加打印账单和详单时房间号为空的警告
@ 修改人：田健豪
@ 修改日期：2023年12月17日
'''

import requests
from PyQt5.QtWidgets import QWidget, QMessageBox

import login  # 导入登录界面
import reception
from PyQt5 import QtCore, QtGui, QtWidgets


class MyForm(reception.Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 绑定按钮的点击事件与槽函数
        self.pushButton.clicked.connect(self.display_bill)
        self.pushButton_2.clicked.connect(self.display_details)


    def display_bill(self):
        if self.room_id.text() == "":
            QMessageBox.warning(self, '警告', '房间号不能为空，请输入！', QMessageBox.Yes)
            return
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
        if self.room_id.text() == "":
            QMessageBox.warning(self, '警告', '房间号不能为空，请输入！', QMessageBox.Yes)
            return
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