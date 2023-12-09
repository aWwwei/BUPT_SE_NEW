'''
@ 文件名：ServerDispatch.py
@ 文件功能描述：服务器调度管理类，用于接受客户端送风请求并进行调度
@ 创建日期：2023年11月27日
@ 创建人：任波
@ 修改描述：修正逻辑
@ 修改日期：2023年12月6日
'''
from database import DetailsTable
from datetime import datetime
import time
#from PyQt5.QtCore import pyqtSignal
#from PyQt5.QtCore import QObject
import ReadConfig
import front_desk
import threading


class Dispatch:
    #changeSignal = pyqtSignal()  # 用于发射信号

    def __init__(self,database):
        super(Dispatch, self).__init__()

        self.queueS = []    # 服务队列
        self.queueW = []    # 等待队列
        self.queueI = []    # 插入队列
        self.roomIDA = 0    # 全局变量roomIDA代表经调度要从服务队列移到等待队列，停止送风的房间号，可直接读取
        self.roomIDB = 0    # 全局变量roomIDB代表经调度要从等待队列移到服务队列，开始送风的房间号，可直接读取
        self.speedA = 0     # roomIDA对应的风速（事实上始终为0）
        self.speedB = 0     # roomIDB对应的风速
        self.stop_flag = threading.Event()

        config = ReadConfig.Config.getDispatch()
        self.timeSpeed = int(config['speed'])                     # 读入仿真速度
        self.queueSLen = int(config['quelen'])                    # 读入队列长度
        self.waitTime = int(config['waittime'])/self.timeSpeed    # 读入最长等待时间
        self.check_table = front_desk.create_check_table(database)
        self.details_table = front_desk.create_details_table(database)    # 创建详单表
        self.thread = threading.Thread(target=self.updateQueue)   # 创建线程
        self.thread.start()  # 启动线程
        self.thread0 = threading.Thread(target=self.updateInsert)  # 创建线程
        self.thread0.start()  # 启动线程

   
    # 加入服务队列
    def addToServer(self, roomID, speedValue):
        t=time.time()
        dic = {'roomID': roomID, 'speed': speedValue, 'waitedT':0, 'waitT': self.waitTime, 'startT':0
               
               }

        self.queueS.append(dic)
        return self.queueS

    # 加入等待队列
    def addToWait(self, roomID, speedValue):
        t=time.time()
        dic = {'roomID': roomID, 'speed': speedValue, 'waitedT':0, 'waitT': self.waitTime, 'startT':t
               }
        self.queueW.append(dic)
        return self.queueW

    # 从服务队列移除
    def removeFromServer(self, roomID):
        for item in self.queueS:
            if item['roomID'] == roomID:
                self.queueS.remove(item)
                break

    # 从等待队列移除
    def removeFromWait(self, roomID):
        for item in self.queueW:
            if item['roomID'] == roomID:
                self.queueW.remove(item)
                break

    # 从等待队列移入服务队列
    def moveToServer(self, roomID):
        for item in self.queueW:
            if item['roomID'] == roomID:
                dic = item
                dic['startT'] = 0
                self.queueS.append(dic)
                self.queueW.remove(item)
                break

    # 从服务队列移入等待队列
    def moveToWait(self, roomID):
        for item in self.queueS:
            if item['roomID'] == roomID:
                dic = item
                dic['startT'] = time.time()
                self.queueW.append(dic)
                self.queueS.remove(item)
                break

    def addWaitTime(self, startT):
        waittime = time.time()-startT
        return waittime

    def addServerTime(self, startT):
        servertime = time.time()-startT
        return servertime

    def serverDispatch(self,roomID,speedValue):
        num = 0     # 记录服务队列中比请求风速小的房间的个数
        lowNum = 0  # 服务队列中低风请求的个数
        midNum = 0  # 服务队列中中风请求的个数
        for item in self.queueS:
            if item['speed'] < speedValue:
                num += 1
        for item in self.queueS:
            if item['speed'] == 1:
                lowNum += 1
            elif item['speed'] == 2:
                midNum += 1
                # 服务队列中至少有一个房间风速小于新请求
        if num >= 1:
            if lowNum >= 1:
                for item in self.queueS:
                    if item['speed'] == 1:
                        roomIDO = item['roomID']
                        self.moveToWait(roomIDO)
                        self.addToServer(roomID, speedValue)
                        #print(roomID,'加入服务 ',roomIDO,'退出等待')
                        return roomIDO, 0, roomID, speedValue
            elif lowNum == 0 and midNum >= 1:
                for item in self.queueS:
                    if item['speed'] == 2:  # 队列中第一个中风速即为中风速里（最低优先级）服务时间最久的，将该房间加入等待队列
                        roomIDO = item['roomID']
                        self.moveToWait(roomIDO)
                        self.addToServer(roomID, speedValue)
                        #print(roomID,'加入服务 ',roomIDO,'退出等待')
                        return roomIDO, 0, roomID, speedValue
                # 服务队列中房间风速都大于等于新请求
        else:
            self.addToWait(roomID, speedValue)
            return roomID, 0, 0, 0  # 表示拒绝请求，放入等待队列

    def waitDispatch(self,loc,roomID,speedValue):
        num = 0     # 记录等待队列中比请求风速大的房间的个数
        highNum = 0  # 等待队列中高风请求的个数
        midNum = 0  # 等待队列中中风请求的个数
        for item in self.queueW:
            if item['speed'] > speedValue:
                num += 1
        for item in self.queueW:
            if item['speed'] == 3:
                highNum += 1
            elif item['speed'] == 2:
                midNum += 1
        # 等待队列中至少有一个房间风速大于新请求
        if num >= 1:
            # 等待队列至少有一个高风速
            if highNum >= 1:
                for item in self.queueW:
                    if item['speed'] == 3:  # 队列中第一个高风速即为高风速里（最高优先级）等待时间最久的，将该房间加入服务队列
                        roomIDO = item['roomID']
                        speedO = item['speed']
                        self.removeFromServer(roomID)
                        self.addToWait(roomID, speedValue)
                        self.moveToServer(roomIDO)
                        self.removeFromWait(roomIDO)
                        #print(roomIDO,'加入服务 ',roomID,'退出等待')
                        return roomID, 0, roomIDO, speedO
                        # 等待队列无高风速，至少有一个中风速
            elif highNum == 0 and midNum >= 1:
                for item in self.queueW:
                    if item['speed'] == 2:  # 队列中第一个中风速即为中风速里（最高优先级）等待时间最久的，将该房间加入服务队列
                        roomIDO = item['roomID']
                        speedO = item['speed']
                        self.removeFromServer(roomID)
                        self.addToWait(roomID, speedValue)
                        self.moveToServer(roomIDO)
                        self.removeFromWait(roomIDO)
                        #print(roomIDO,'加入服务 ',roomID,'退出等待')
                        return roomID, 0, roomIDO, speedO

                    # 等待队列中的风速都小于等于新请求
        else:
            self.queueS[loc]['speed'] = speedValue      # 允许发出请求的房间送风，在服务队列更改风速值
            return 0, 0, roomID, speedValue
            # 若等待队列为空

    def requestWind(self, roomID, speedValue):      # 返回值为4个参数，停止送风的房间号（若为0则代表没有），其风速（0），开始送风的房间号（若为0则代表没有），其风速
        flagS = 0   # 判断是否在服务队列重复房间
        flagW = 0   # 判断是否在等待队列重复房间
        loc = 0        # 记录重复房间在队列中的位置
        for i in range(len(self.queueS)):
            if self.queueS[i]['roomID'] == roomID:
                flagS = 1
                loc = i
                break
        for i in range(len(self.queueW)):
            if self.queueW[i]['roomID'] == roomID:
                flagW = 1
                loc = i
                break
            
        if flagS == 0 and flagW == 0:
            # 若服务队列未满
            if len(self.queueS) < self.queueSLen:
                self.addToServer(roomID, speedValue)
                return 0, 0, roomID, speedValue    # 表示接收请求，开始送风
            # 若服务队列满
            else:
                self.serverDispatch(roomID,speedValue) # 查看是否

        elif flagS == 1: # 已经在服务队列
            
            # 若等待队列不为空
            if len(self.queueW) != 0:
                # 风速比原来升高或不变
                if speedValue > self.queueS[loc]['speed'] or speedValue == self.queueS[loc]['speed']:
                    self.queueS[loc]['speed'] = speedValue
                    return 0, 0, roomID, speedValue
                # 风速比原来降低
                elif speedValue < self.queueS[loc]['speed']:
                    self.waitDispatch(loc,roomID,speedValue)
            # 若等待队列为空
            else:
                self.queueS[loc]['speed'] = speedValue      # 允许发出请求的房间送风，在服务队列更改风速值
                return 0, 0, roomID, speedValue

        elif flagW == 1:
            
            # 此时等待队列必不为空，不用考虑为空的情况
            # 风速比原来降低或不变
            if speedValue < self.queueW[loc]['speed'] or speedValue == self.queueW[loc]['speed']:
                self.queueW[loc]['speed'] = speedValue
                return roomID, 0, 0, 0
            # 风速比原来升高
            elif speedValue > self.queueW[loc]['speed']:
                self.serverDispatch(roomID,speedValue)

    def stopWind(self, roomID):     # 返回值为4个参数，停止送风的房间号，其风速（0），开始送风的房间号（若为0则代表没有），其风速
        flag = 0
        flag0 = 0
        for item in self.queueS:
            if roomID == item['roomID']:
                flag = 1
                break
        for item in self.queueW:
            if roomID == item['roomID']:
                flag0 = 1
                break
        # 若该房间号已经在服务队列中
        if flag == 1:
            self.removeFromServer(roomID)
            highNum = 0     # 等待队列中高风请求的个数
            midNum = 0      # 等待队列中中风请求的个数
            # 若等待队列不为空
            if len(self.queueW) != 0:
                for item in self.queueW:
                    if item['speed'] == 3:
                        highNum += 1
                    elif item['speed'] == 2:
                        midNum += 1
                if highNum >= 1:   # 等待队列至少有一个高风速，将等待时间最长的加入服务队列
                    for item in self.queueW:
                        if item['speed'] == 3:  # 队列中第一个高风速即为高风速里（最高优先级）等待时间最久的，将该房间加入服务队列
                            roomIDO = item['roomID']
                            speedO = item['speed']
                            self.moveToServer(roomIDO)
                            return roomID, 0, roomIDO, speedO
                elif highNum == 0 and midNum >= 1:   # 等待队列无高风速，至少有一个中风速，将等待时间最长的加入服务队列
                    for item in self.queueW:
                        if item['speed'] == 2:  # 队列中第一个中风速即为中风速里（最高优先级）等待时间最久的，将该房间加入服务队列
                            roomIDO = item['roomID']
                            speedO = item['speed']
                            self.moveToServer(roomIDO)
                            return roomID, 0, roomIDO, speedO
                else:   # 等待队列全为低风速
                    for item in self.queueW:
                        if item['speed'] == 1:  # 队列中第一个低风速即为低风速里（最高优先级）等待时间最久的，将该房间加入服务队列
                            roomIDO = item['roomID']
                            speedO = item['speed']
                            self.moveToServer(roomIDO)
                            return roomID, 0, roomIDO, speedO
            # 若等待队列为空
            else:
                return roomID, 0, 0, 0
        # 若该房间号在等待队列中
        elif flag0 == 1:
            self.removeFromWait(roomID)
            return roomID, 0, 0, 0
        else:
            return roomID, 0, 0, 0

    def updateQueue(self):
        while True:
            while (len(self.queueS) == self.queueSLen and len(self.queueW) > 0):
                time.sleep(0.1/self.timeSpeed)
                S=[]
                W=[]
                for item in self.queueS:
                    S.append(item['roomID']) 
                for item in self.queueW:
                    W.append(item['roomID']) 
                S_set = set(S)
                W_set = set(W)
                for ID in S_set:
                    if ID in W_set:
                        self.removeFromWait(ID)
                for item in self.queueW:
                    if time.time() >= item['waitT']+ item['startT']:
                        j=1
                        for i in range(len(self.queueS)):
                            if item['speed'] == self.queueS[i]['speed']:
                                self.roomIDA = self.queueS[i]['roomID']    # roomIDA代表经调度要从服务队列移到等待队列，停止送风的房间号
                                self.roomIDB = item['roomID']              # roomIDB代表经调度要从等待队列移到服务队列，开始送风的房间号
                                self.speedA = 0
                                self.speedB = item['speed']
                                self.moveToWait(self.queueS[i]['roomID'])
                                self.moveToServer(item['roomID'])
                                #print(item['roomID'],'加入服务 ',self.queueS[i]['roomID'],'退出等待')
                                break                           
                        if j:
                            self.roomIDA = 0
                            self.roomIDB = 0
                            self.speedA = 0
                            self.speedB = 0
                    else:
                        self.roomIDA = 0
                        self.roomIDB = 0
                        self.speedA = 0
                        self.speedB = 0

    def Insert(self,roomID,env_type,speed,runState,cost):
        t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #print(t)
        item = [ roomID, t,env_type,speed,runState,cost]
        self.queueI.append(item)

    def updateInsert(self):
        while not self.stop_flag.is_set():
            time.sleep(1)
            if len(self.queueI)!=0:
                item = self.queueI.pop(0)
                print(item)
                self.details_table.insert(item[0], item[1],item[2], item[3], item[4], item[5])
    
    def stop_Insert(self):
        self.stop_flag.set()  # 设置标志变量，使函数B的循环退出

    

                

