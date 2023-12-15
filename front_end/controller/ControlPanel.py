"""
@ 文件名：  ControlPanel.py
@ 文件功能描述： 绑定用户房间的控制面板的槽函数，实现前端交互逻辑
@ 创建人：   田健豪
@ 创建日期： 2023年12月10日

@ 修改描述： 增加槽函数pushButton_switch_clicked，用于实现开关机逻辑
@ 修改人：  田健豪
@ 修改日期： 2023年12月14日

@ 修改描述： 增加函数power_on，用于向服务器发送开机请求
@ 修改人：  田健豪
@ 修改日期： 2023年12月14日

@ 修改描述： 增加槽函数update，用于获取当前温度和费用，更新控制面板
@ 修改人：  田健豪
@ 修改日期： 2023年12月14日

@ 修改描述： 增加状态变量state，增加函数power_off，用于向服务器发送关机请求
@ 修改人：  田健豪
@ 修改日期： 2023年12月15日

"""



import sys

import requests
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PyQt5.QtCore import Qt, QTimer

import Clogin
import controller

class MyWindow(Clogin.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 如果需要，连接任何信号和槽
        self.pushButton_sign_in.clicked.connect(self.login)

    def login(self):
        # 在这里添加您的登录逻辑
        room_id = self.lineEdit_roomnumber.text()
        password_input = self.lineEdit_password.text()

        if room_id == "":
            QMessageBox.warning(self, '警告', '房间号不能为空，请输入！', QMessageBox.Yes)

        elif password_input == "":
            QMessageBox.warning(self, '警告', '密码不能为空，请输入！', QMessageBox.Yes)
        else:
            if password_input == "1":
                self.new_window = MyWidget(room_id)
                self.new_window.show()
                self.close()
            else:
                QMessageBox.critical(self, '错误', '用户名或密码错误！')


class MyWidget(controller.Ui_Client, QWidget):
    def __init__(self, room_id):
        super().__init__()
        self.setupUi(self)  # 使用loadUi不需要再次加载UI
        self.room_id = room_id
        self.label_RoomName.setText(f"ROOM{self.room_id}")
        self.state = 'off'

        self.slot_init()

    def slot_init(self):
        self.pushButton_switch.clicked.connect(self.pushButton_switch_clicked)
        self.pushButton_down.clicked.connect(self.pushButton_down_clicked)
        self.pushButton_up.clicked.connect(self.pushButton_up_clicked)
        self.pushButton_low.clicked.connect(self.pushButton_low_clicked)
        self.pushButton_mid.clicked.connect(self.pushButton_mid_clicked)
        self.pushButton_high.clicked.connect(self.pushButton_high_clicked)
        self.pushButton_check.clicked.connect(self.pushButton_check_clicked)

    def pushButton_down_clicked(self):
        self.textBrowser_target_tem.setText(str(int(self.textBrowser_target_tem.toPlainText()) - 1))

    def pushButton_up_clicked(self):
        self.textBrowser_target_tem.setText(str(int(self.textBrowser_target_tem.toPlainText()) + 1))

    def pushButton_low_clicked(self):
        self.textBrowser_speed.setText("low")

    def pushButton_mid_clicked(self):
        self.textBrowser_speed.setText("mid")

    def pushButton_high_clicked(self):
        self.textBrowser_speed.setText("high")

    def pushButton_check_clicked(self):
        if self.state == 'on':
            data = requests.post(f"http://127.0.0.1:5000/set_wind_speed", data={
                "room_id": self.room_id,
                "wind_speed": self.textBrowser_speed.toPlainText(),
                "target_temperature": self.textBrowser_target_tem.toPlainText()
            })


    def pushButton_switch_clicked(self):
        if self.state == 'off':
            self.power_on()
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update)
            self.timer.start(5000)  # 启动定时器
            self.state = 'on'
        elif self.state == 'on':
            self.power_off()
            self.timer.stop()
            del self.timer
            self.state = 'off'

    def power_on(self):
        data = requests.post(f"http://127.0.0.1:5000/power_on", data={
            "room_id": self.room_id,
            "wind_speed": self.textBrowser_speed.toPlainText(),
            "target_temperature": self.textBrowser_target_tem.toPlainText()
        })
        if data.status_code == 200:
            self.label_current_tem.setText(str(data.json()['当前温度']))
            self.label_current_fee.setText(str(data.json()['当前费用']))
            self.label_Total_fee.setText(str(data.json()['总费用']))

    def power_off(self):
        data = requests.post(f"http://127.0.0.1:5000/power_off", data={
            "room_id": self.room_id
        })
        if data.status_code == 200:
            self.label_current_tem.setText(str(data.json()['当前温度']))
            self.label_current_fee.setText(str(data.json()['当前费用']))
            self.label_Total_fee.setText(str(data.json()['总费用']))

    def update(self):
        data = requests.post(f"http://127.0.0.1:5000/update_control_panel", data={
            "room_id": self.room_id
        })
        if data.status_code == 200:
            self.label_current_tem.setText(str(data.json()['当前温度']))
            self.label_current_fee.setText(str(data.json()['当前费用']))
            self.label_Total_fee.setText(str(data.json()['总费用']))


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    window1 = MyWindow()
    window1.show()
    sys.exit(app.exec_())
