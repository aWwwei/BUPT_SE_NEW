'''
@ 文件名：TempControl.py
@ 文件功能描述：负责控制服务端温度变化的温度控制器类
@ 创建日期：2023年11月29日
@ 创建人：任波
@ 修改描述：添加插入调用
@ 修改人：任波
@ 修改日期：2020年12月7日
@ 修改描述：修改状态判断
@ 修改人：任波
@ 修改日期：2020年12月10日
@ 修改描述：优化计费
@ 修改人：任波
@ 修改日期：2020年12月11日
'''

#from PyQt5.QtCore import pyqtSignal
#from PyQt5.QtCore import QObject
import time
import ReadConfig
import threading
import ServerDispatch

class TempControl:#(QObject):
    #changeSignal = pyqtSignal()  # 用于发射信号

    def __init__(self, roomID,dp):
        super(TempControl, self).__init__()
        self.roomID = roomID
        self.tempConfig = ReadConfig.Config.getTempcontrol()    # 读入控制模块参数
        self.beginConfig = ReadConfig.Config.getBegintemp()     # 读入初始温度
        self.timeSpeed = int(self.tempConfig['speed'])          # 设置仿真速度
        self.refreshSeq = int(self.tempConfig['refreshseq'])    # 温度更新频率
        self.highPrice = float(self.tempConfig['highprice'])    # 高风费率
        self.midPrice = float(self.tempConfig['midprice'])      # 中风费率
        self.lowPrice = float(self.tempConfig['lowprice'])      # 低风费率
        self.highDelta = float(self.tempConfig['highdelta'])    # 高风温度变化率
        self.midDelta = float(self.tempConfig['middelta'])      # 中风温度变化率
        self.lowDelta = float(self.tempConfig['lowdelta'])      # 低风温度变化率
        self.tempDefault = int(self.beginConfig['room' + str(self.roomID)])     # 初始温度
        self.tempNow = int(self.beginConfig['room' + str(self.roomID)])         # 室内温度
        self.tempSet = 25           # 默认温度 25°
        self.speedSet = 'mid'       # 默认风速 high mid low
        self.runModel = 'cool'      # 默认运行状态 cool warm
        self.runState = 'close'     # 用于指示是否运行 run close sleep waiting sleeping
        self.cost= 0
        self.totalCost = 0          # 计费
        self.dp = dp
        #self.changeTemp()
        self.thread = threading.Thread(target=self.changeTemp)  # 创建线程
        self.thread.start()  # 启动线程

    def setDefault_Now(self):
        self.tempDefault = int(self.config['room' + str(self.roomID)])
        self.tempNow = int(self.config['room' + str(self.roomID)])

    # 模式设置函数
    def setModel(self, model):
        self.runModel = model

    # 风速设置函数
    def setSpeed(self, speed):
        self.speedSet = speed

    # 温度设置函数
    def setTemp(self, temp):
        self.tempSet = temp
        return 1
    def changeState(self):
        while True:
            run = 0
            wait = 0
            for item in self.dp.queueS:
                if item['roomID'] == self.roomID:
                    run = 1
            for item in self.dp.queueW:
                if item['roomID'] == self.roomID:
                    wait = 1
            if run:
                if self.runState != 'running':
                    self.dp.Insert(self.roomID, '开机', self.speedSet, 'running', round(self.totalCost, 4))
                self.runState = 'running'
            elif wait:
                if self.runState == 'running':
                    self.dp.Insert(self.roomID, '修改风速', self.speedSet, 'waiting', round(self.totalCost, 4))
                self.runState = 'waiting'
        
    # 用信号定时触发该函数，一定频率进行改变
    def changeTemp(self):
        t=time.time()
        while True:
            while time.time() - t >= (6 / self.refreshSeq / self.timeSpeed):
                run = 0
                wait = 0
                for item in self.dp.queueS:
                    if item['roomID'] == self.roomID:
                        run = 1
                for item in self.dp.queueW:
                    if item['roomID'] == self.roomID:
                        wait = 1
                if run:
                    if self.runState != 'running':
                        self.dp.Insert(self.roomID, '开机', self.speedSet, 'running', round(self.totalCost, 4))
                    self.runState = 'running'
                elif wait:
                    if self.runState == 'running':
                        self.dp.Insert(self.roomID, '修改风速', self.speedSet, 'waiting', round(self.totalCost, 4))
                    self.runState = 'waiting'

                if time.time() - t >= (60 / self.refreshSeq / self.timeSpeed):
                    t += (60 / self.refreshSeq / self.timeSpeed)
                    if self.runState == 'running':
                        if self.runModel == "cool" and self.tempNow <= self.tempSet:  # 温度相等停止变化
                            self.runState = 'sleeping'
                            self.dp.stopWind(self.roomID)
                            time.sleep(0.5)
                            self.dp.Insert(self.roomID, '关机', self.speedSet, 'waiting', round(self.totalCost, 4))
                        elif self.runModel == "warm" and self.tempNow >= self.tempSet:  # 温度相等停止变化
                            self.runState = 'sleeping'
                            self.dp.stopWind(self.roomID)
                            time.sleep(0.5)
                            self.dp.Insert(self.roomID, '关机', self.speedSet, 'waiting', round(self.totalCost, 4))

                        elif self.runModel == "cool" and self.tempNow > self.tempSet:  # 制冷模式下
                            if self.speedSet == 'high':
                                self.tempNow -= self.highDelta / self.refreshSeq
                                self.totalCost += self.dp.Price*self.highPrice / self.refreshSeq
                                if self.tempNow < self.tempSet:
                                    self.totalCost += (self.tempNow - self.tempSet) * self.dp.Price * self.highPrice / self.highDelta
                                    self.tempNow = self.tempSet
                            elif self.speedSet == 'mid':
                                self.tempNow -= self.midDelta / self.refreshSeq
                                self.totalCost += self.dp.Price*self.midPrice / self.refreshSeq
                                if self.tempNow < self.tempSet:
                                    self.totalCost += (self.tempNow - self.tempSet) * self.dp.Price * self.midPrice / self.midDelta
                                    self.tempNow = self.tempSet
                            elif self.speedSet == 'low':
                                self.tempNow -= self.lowDelta / self.refreshSeq
                                self.totalCost += self.dp.Price*self.lowPrice / self.refreshSeq
                                if self.tempNow < self.tempSet:
                                    self.totalCost += (self.tempNow - self.tempSet) * self.dp.Price * self.lowPrice / self.lowDelta
                                    self.tempNow = self.tempSet

                        elif self.runModel == "warm" and self.tempNow < self.tempSet:  # 制热模式下
                            if self.speedSet == 'high':
                                self.tempNow += self.highDelta / self.refreshSeq
                                self.totalCost += self.dp.Price*self.highPrice / self.refreshSeq
                                if self.tempNow > self.tempSet:
                                    self.totalCost -= (self.tempNow - self.tempSet) * self.dp.Price * self.highPrice / self.highDelta
                                    self.tempNow = self.tempSet
                            elif self.speedSet == 'mid':
                                self.tempNow += self.midDelta / self.refreshSeq
                                self.totalCost += self.dp.Price*self.midPrice / self.refreshSeq
                                if self.tempNow > self.tempSet:
                                    self.totalCost -= (self.tempNow - self.tempSet) * self.dp.Price * self.midPrice / self.midDelta
                                    self.tempNow = self.tempSet
                            elif self.speedSet == 'low':
                                self.tempNow += self.lowDelta / self.refreshSeq
                                self.totalCost += self.dp.Price*self.lowPrice / self.refreshSeq
                                if self.tempNow > self.tempSet:
                                    self.totalCost -= (self.tempNow - self.tempSet) * self.dp.Price * self.lowPrice / self.lowDelta
                                    self.tempNow = self.tempSet

                    elif self.runState == 'sleeping':
                        if self.speedSet == 'high':
                            speedValue = 3
                        elif self.speedSet == 'mid':
                            speedValue = 2
                        elif self.speedSet == 'low':
                            speedValue = 1
                        if self.runModel == "cool" and (self.tempNow - self.tempSet) >= 1:  # 温度相等停止变化
                            # self.runState = 'running'
                            self.runState = 'waiting'
                            self.dp.requestWind(self.roomID, speedValue)
                        elif self.runModel == "warm" and (self.tempSet - self.tempNow) >= 1:  # 温度相等停止变化
                            # self.runState = 'running'
                            self.runState = 'waiting'
                            self.dp.requestWind(self.roomID, speedValue)
                        elif self.tempNow < self.tempDefault:
                            self.tempNow += 0.5 / self.refreshSeq
                        elif self.tempNow > self.tempDefault:
                            self.tempNow -= 0.5 / self.refreshSeq

                    # elif self.runState == 'waiting':
                    #    if self.tempNow < self.tempDefault:
                    #        self.tempNow += 0.5 / self.refreshSeq
                    #    elif self.tempNow > self.tempDefault:
                    #        self.tempNow -= 0.5 / self.refreshSeq

                    elif self.runState == 'close':
                        if self.tempNow < self.tempDefault:
                            self.tempNow += 0.5 / self.refreshSeq
                        elif self.tempNow > self.tempDefault:
                            self.tempNow -= 0.5 / self.refreshSeq

                # 精度处理

                # 对于温度和金额的精度进行处理

                # 发送更新信号
                # self.changeSignal.emit()



def runTest(dp, tem, msg):
    msg = msg.split(',')
    if len(msg) == 1:
        if msg[0] == 'open' :
            tem.runState = 'waiting'
            tem.tempSet = 25
            tem.speedSet = 'mid'
            dp.requestWind(tem.roomID, 2)

        elif msg[0] == 'close' :
            tem.runState = 'close'
            dp.stopWind(tem.roomID)

    elif len(msg) == 2:
        if msg[0] == '':
            if msg[1] == 'high':
                tem.speedSet = 'high'
                dp.requestWind(tem.roomID, 3)

            elif msg[1] == 'mid':
                tem.speedSet = 'mid'
                dp.requestWind(tem.roomID, 2)

            elif msg[1] == 'low':
                tem.speedSet = 'low'
                dp.requestWind(tem.roomID, 1)

               
        elif msg[1] == '':
            tem.tempSet = (int(msg[0]))
        else:
            if msg[1] == 'high':
                tem.speedSet = 'high'
                dp.requestWind(tem.roomID, 3)

            elif msg[1] == 'mid':
                tem.speedSet = 'mid'
                dp.requestWind(tem.roomID, 2)

            elif msg[1] == 'low':
                tem.speedSet = 'low'
                dp.requestWind(tem.roomID, 1)

            tem.tempSet = (int(msg[0]))
