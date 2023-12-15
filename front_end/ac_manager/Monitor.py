"""
@ 文件名：  Monitor.py
@ 文件功能描述： 绑定空调管理员监控界面的槽函数，实现前端交互逻辑
@ 创建人：   田健豪
@ 创建日期： 2023年12月9日

@ 修改描述： 增加槽函数login，用于实现登录逻辑
@ 修改人：  田健豪
@ 修改日期： 2023年12月11日

@ 修改描述： 增加槽函数pushButton_low_down_clicked，实现低温度减少按钮触发逻辑
@ 修改人：  田健豪
@ 修改日期： 2023年12月11日

@ 修改描述： 增加槽函数pushButton_low_up_clicked，实现低温度增加按钮触发逻辑
@ 修改人：  田健豪
@ 修改日期： 2023年12月11日

@ 修改描述： 增加槽函数pushButton_high_down_clicked，实现高温度减少按钮触发逻辑
@ 修改人：  田健豪
@ 修改日期： 2023年12月11日

@ 修改描述： 增加槽函数pushButton_high_up_clicked，实现高温度增加按钮触发逻辑
@ 修改人：  田健豪
@ 修改日期： 2023年12月11日

@ 修改描述： 增加槽函数pushButton_Rates_check_clicked，实现费率设置按钮触发逻辑
@ 修改人：  田健豪
@ 修改日期： 2023年12月11日

@ 修改描述： 增加槽函数pushButton_cold_clicked，实现制冷模式按钮触发逻辑
@ 修改人：  田健豪
@ 修改日期： 2023年12月11日

@ 修改描述： 增加槽函数pushButton_warm_clicked，实现制热模式按钮触发逻辑
@ 修改人：  田健豪
@ 修改日期： 2023年12月11日

@ 修改描述： 增加槽函数pushButton_switch_clicked，实现开关机按钮触发逻辑
@ 修改人：  田健豪
@ 修改日期： 2023年12月14日


@ 修改描述： 增加槽函数get_room_info，用于获取房间信息
@ 修改人：  田健豪
@ 修改日期： 2023年12月14日

@ 修改描述： 增加槽函数update_room_info，用于更新房间信息
@ 修改人：  田健豪
@ 修改日期： 2023年12月14日
"""

import sys

import requests
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PyQt5.QtCore import Qt, QTimer

import Slogin
import Suiwidget

class MyWindow(Slogin.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.slot__init()

    def slot__init(self):
        # 如果需要，连接任何信号和槽
        self.pushButton_sign_in.clicked.connect(self.login)

    def login(self):
        # 在这里添加您的登录逻辑
        username_input = self.lineEdit_username.text()
        password_input = self.lineEdit_password.text()

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

                self.new_window = MyWidget()
                self.new_window.show()
                self.close()
            else:
                QMessageBox.critical(self, '错误', '用户名或密码错误！')


class MyWidget(Suiwidget.Ui_Admin, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 使用loadUi不需要再次加载UI
        self.mode = "cool"
        self.price = 1
        self.state = "off"

        self.slot_init()

    def slot_init(self):
        self.pushButton_low_down.clicked.connect(self.pushButton_low_down_clicked)
        self.pushButton_low_up.clicked.connect(self.pushButton_low_up_clicked)
        self.pushButton_high_down.clicked.connect(self.pushButton_high_down_clicked)
        self.pushButton_high_up.clicked.connect(self.pushButton_high_up_clicked)
        self.pushButton_Rates_check.clicked.connect(self.pushButton_Rates_check_clicked)
        self.pushButton_cold.clicked.connect(self.pushButton_cold_clicked)
        self.pushButton_warm.clicked.connect(self.pushButton_warm_clicked)
        self.pushButton_switch.clicked.connect(self.pushButton_switch_clicked)

    def update_room_info(self, room_info):
        for i in range(5):
            if room_info[i] is not None:
                if i == 0:
                    self.textBrowser_Room1_state.setText(room_info[i]['状态'])
                    self.textBrowser_Room1_WindSpeed.setText(room_info[i]['风速'])
                    self.textBrowser_Room1_Currentfee.setText(str(room_info[i]['当前费用']))
                    self.textBrowser_Room1_Totalfee.setText(str(room_info[i]['总费用']))
                    self.textBrowser_Room1_tem.setText(str(room_info[i]['当前温度']))
                    self.textBrowser_Room1_target_tem.setText(str(room_info[i]['目标温度']))
                elif i == 1:
                    self.textBrowser_Room2_state.setText(room_info[i]['状态'])
                    self.textBrowser_Room2_WindSpeed.setText(room_info[i]['风速'])
                    self.textBrowser_Room2_Currentfee.setText(str(room_info[i]['当前费用']))
                    self.textBrowser_Room2_Totalfee.setText(str(room_info[i]['总费用']))
                    self.textBrowser_Room2_tem.setText(str(room_info[i]['当前温度']))
                    self.textBrowser_Room2_target_tem.setText(str(room_info[i]['目标温度']))
                elif i == 2:
                    self.textBrowser_Room3_state.setText(room_info[i]['状态'])
                    self.textBrowser_Room3_WindSpeed.setText(room_info[i]['风速'])
                    self.textBrowser_Room3_Currentfee.setText(str(room_info[i]['当前费用']))
                    self.textBrowser_Room3_Totalfee.setText(str(room_info[i]['总费用']))
                    self.textBrowser_Room3_tem.setText(str(room_info[i]['当前温度']))
                    self.textBrowser_Room3_target_tem.setText(str(room_info[i]['目标温度']))
                elif i == 3:
                    self.textBrowser_Room4_state.setText(room_info[i]['状态'])
                    self.textBrowser_Room4_WindSpeed.setText(room_info[i]['风速'])
                    self.textBrowser_Room4_Currentfee.setText(str(room_info[i]['当前费用']))
                    self.textBrowser_Room4_Totalfee.setText(str(room_info[i]['总费用']))
                    self.textBrowser_Room4_tem.setText(str(room_info[i]['当前温度']))
                    self.textBrowser_Room4_target_tem.setText(str(room_info[i]['目标温度']))
                elif i == 4:
                    self.textBrowser_Room5_state.setText(room_info[i]['状态'])
                    self.textBrowser_Room5_WindSpeed.setText(room_info[i]['风速'])
                    self.textBrowser_Room5_Currentfee.setText(str(room_info[i]['当前费用']))
                    self.textBrowser_Room5_Totalfee.setText(str(room_info[i]['总费用']))
                    self.textBrowser_Room5_tem.setText(str(room_info[i]['当前温度']))
                    self.textBrowser_Room5_target_tem.setText(str(room_info[i]['目标温度']))


    def pushButton_low_down_clicked(self):
        self.lcdNumber_t_low.display(self.lcdNumber_t_low.value() - 1)

    def pushButton_low_up_clicked(self):
        self.lcdNumber_t_low.display(self.lcdNumber_t_low.value() + 1)

    def pushButton_high_down_clicked(self):
        self.lcdNumber_t_high.display(self.lcdNumber_t_high.value() - 1)

    def pushButton_high_up_clicked(self):
        self.lcdNumber_t_high.display(self.lcdNumber_t_high.value() + 1)

    def pushButton_Rates_check_clicked(self):
        self.rate = self.doubleSpinBox_rates.value()

    def pushButton_cold_clicked(self):
        self.mode = "cool"
        self.label_mode_value.setText("制冷")
        self.label_mode_value.setFont(QFont("微软雅黑", 9))

    def pushButton_warm_clicked(self):
        self.mode = "warm"
        self.label_mode_value.setText("制热")
        self.label_mode_value.setFont(QFont("微软雅黑", 9))

    def pushButton_Rates_check_clicked(self):
        self.price = self.doubleSpinBox_rates.value()

    def pushButton_switch_clicked(self):
        if self.state == "off":
            self.server_on()
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.get_room_info)
            self.timer.start(2000)  # 启动定时器
            self.state = "on"
        elif self.state == "on":
            self.server_off()
            self.timer.stop()
            del self.timer
            self.state = "off"
            self.textBrowser_Room1_state.setText("closed")
            self.textBrowser_Room2_state.setText("closed")
            self.textBrowser_Room3_state.setText("closed")
            self.textBrowser_Room4_state.setText("closed")
            self.textBrowser_Room5_state.setText("closed")

    def server_on(self):
        data = requests.post(f"http://127.0.0.1:5000/server_on", data={
            "price": self.price,
            "mode": self.mode,
        })

    def server_off(self):
        data = requests.get(f"http://127.0.0.1:5000/server_off")

    def get_room_info(self):
        data = requests.get(f"http://127.0.0.1:5000/get_room_info")
        if data.status_code == 200:
            room_info = data.json()['room_info']
            self.update_room_info(room_info)


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
