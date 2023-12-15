"""
@ 文件名：runDispatch.py
@ 文件功能描述：调度的封装接口
@ 创建人：任波
@ 创建日期：2023年12月7日

@ 修改描述：添加插入调用
@ 修改人：任波
@ 修改日期：2023年12月7日

@ 修改描述：增加接口
@ 修改人：任波
@ 修改日期：2023年12月11日

@ 修改描述：整理为类
@ 修改人：任波
@ 修改日期：2023年12月13日

@ 修改描述：增设开关与模式控制
@ 修改人：任波
@ 修改日期：2023年12月14日


@ 修改描述：增设开关与模式控制
@ 修改人：任波
@ 修改日期：2023年12月14日

@ 修改描述：修改返回值的精确度，删除用于测试的print函数
@ 修改人：田健豪
@ 修改日期：2023年12月15日
"""

import front_desk
import ServerDispatch
import TempControl
import time
import threading

class Server:
    def __init__(self):
        super(Server, self).__init__()
        self.switch = 0                                      # 开关
        self.Room = set()                                    # 房间集合
        self.database = front_desk.database()                # 获取数据库类
        self.dp = ServerDispatch.Dispatch(self.database)     # 获取调度类
        self.temSet = [None]*40                              # 房间温控集合
        self.temID = [0] * 40                                # 温控ID集合
        self.queueP = []                                     # print队列
        self.thread = threading.Thread(target=self.dfprint)  # 创建线程
        self.thread.start()                                  # 启动线程

    def Switch(self,switch):
        self.switch = switch
        return switch
    
    def setModel(self,cool):
        if self.switch:
            return self.dp.setModel(cool)
        return 'set end'
    
    def setPrice(self,p):    # 设置费率
        self.dp.setPrice(p)
        return p

    def monitor(self):       # 空调管理员查询
        dic = []
        for i in range(5):
            tem = self.temSet[self.temID[i]]
            if tem is None:
                dic.append(None)
            else:
                dic.append({'当前温度': round(tem.tempNow, 4),
                        '目标温度': tem.tempSet,
                        '风速': tem.speedSet,
                        '状态': tem.runState,
                        '当前费用': round(tem.totalCost - tem.cost, 4),
                        '总费用': round(tem.totalCost, 4)})
        return dic

    def schedule(self, roomID, event_type='送风请求', temp='', speed=''): # 空调请求
        return self.msg(roomID, event_type, temp, speed)

    def ask_bill(self, roomID): # 查询账单
        return self.askdf(self, roomID, 0)

    def ask_details(self, roomID): # 查询详单
        return self.askdf(self, roomID, 1)

    def insert(self,df, path): # 队列相关，非接口
        self.queueP.append([df, path])

    def dfprint(self): # 队列相关，非接口
        i = 0
        t = time.time()
        while i < 10:
            time.sleep(1)
            if len(self.queueP) != 0:
                item = self.queueP.pop(0)
                print(i + 1, item)
                item[0].to_excel(item[1], index=False)
                i += 1
        self.database.close()

    def askdf(self,roomID,type): # 账单详单运行 非接口
        if type:
            tem = self.temSet[self.temID[roomID - 1]]
            tem.runState = 'closed'
            df = front_desk.print_details(self.dp.details_table, roomID)
            self.insert(df, 'details' + str(roomID) + '.xlsx')
        else:
            tem = self.temSet[self.temID[roomID - 1]]
            tem.runState = 'closed'
            df = front_desk.print_bill(self.dp.check_table, roomID, round(tem.totalCost, 4))
            self.insert(df, 'bill' + str(roomID) + '.xlsx')

        return df

    def msg(self, roomID, event_type='开机请求', temp='', speed=''):# 空调请求实际运行，非接口

        # 检查 roomID 是否存在于集合 self.Room 中
        if roomID not in self.Room:
            # 如果 roomID 不存在于集合 self.Room 中，则将其添加到集合中
            self.Room.add(roomID)
            self.dp.Insert(roomID, '账单', '0', '0', '0')
            tem = TempControl.TempControl(roomID, self.dp)
            self.temID[roomID - 1] = len(self.temSet)
            self.temSet.append(tem)

        else:
            tem = self.temSet[self.temID[roomID - 1]]
        if event_type == '开机请求':
            if tem.runState == 'closed':
                if len(self.dp.queueS) < 3:
                    tem.runState = 'running'
                else:
                    tem.runState = 'waiting'
                if temp =='':
                    tem.tempSet = 25
                else:
                    tem.tempSet = temp

                if speed =='':
                    tem.speedSet = 'mid'
                    self.dp.requestWind(tem.roomID, 2)
                elif speed == 'high':
                    tem.speedSet = 'high'
                    self.dp.requestWind(tem.roomID, 3)
                elif speed == 'mid':
                    tem.speedSet = 'mid'
                    self.dp.requestWind(tem.roomID, 2)
                elif speed == 'low':
                    tem.speedSet = 'low'
                    self.dp.requestWind(tem.roomID, 1)
                tem.cost = tem.totalCost
                self.dp.Insert(roomID, '开机', 'mid', tem.runState, round(tem.totalCost, 4))


        elif event_type == '送风请求':
            if temp != '':
                tem.tempSet = (int(temp))

            if speed == 'high':
                tem.speedSet = 'high'
                self.dp.requestWind(tem.roomID, 3)
                self.dp.Insert(roomID, '修改风速', 'high', tem.runState, round(tem.totalCost, 4))

            elif speed == 'mid':
                tem.speedSet = 'mid'
                self.dp.requestWind(tem.roomID, 2)
                self.dp.Insert(roomID, '修改风速', 'mid', tem.runState, round(tem.totalCost, 4))

            elif speed == 'low':
                tem.speedSet = 'low'
                self.dp.requestWind(tem.roomID, 1)
                self.dp.Insert(roomID, '修改风速', 'low', tem.runState, round(tem.totalCost, 4))

        elif event_type == '关机请求':

            tem.runState = 'closed'
            self.dp.stopWind(tem.roomID)
            time.sleep(0.2)
            self.dp.Insert(roomID, '关机', 'low', 'closed', round(tem.totalCost, 4))
            tem.runState = 'closed'

        dic = {'当前温度': round(tem.tempNow, 2),
               # '目标温度': tem.tempSet,
               # '风速': tem.speedSet,
               # '状态': tem.runState,
               '当前费用': round(tem.totalCost - tem.cost, 2),
               '总费用': round(tem.totalCost, 2)}

        return dic

    def try_test(self,roomID=1, type=1):
        if self.dp.flag:
            thread = threading.Thread(target=self.try_Test, args=(roomID, type))  # 创建线程
            thread.start()  # 启动线程

    def try_Test(self,roomID, type):  # 运行测试用例，返回房间号对应的账单详单两个dataframe的列表
        if self.dp.flag:
            msg0 = [
                [['开机请求'], ['送风请求', '18', ''], '', '', '', ['送风请求', '', 'high'], '', '', '',
                 ['送风请求', '22', ''],
                 '', '', '', '', ['关机请求'], '', '', '', ['开机请求'], '', '', '',
                 '', '', ['关机请求'], ''],
                ['', ['开机请求'], '', ['送风请求', '19', ''], '', '', ['关机请求'], ['开机请求'], '', '', '',
                 ['送风请求', '22', ''], '', '', '', '', ['关机请求'], '', '', ['开机请求'], '',
                 '', '', '', '', ['关机请求']],
                ['', '', ['开机请求'], '', '', '', '', '', '', '', '', '', '', '', ['送风请求', '24', 'low'], '', '',
                 ['送风请求', '', 'high'], '', '', '', '', ['关机请求'],
                 '', '', ''],
                ['', '', '', ['开机请求'], '', '', '', '', '', ['送风请求', '18', 'high'], '', '', '', '', '', '', '',
                 '',
                 ['送风请求', '20', 'mid'], '', '', '', '',
                 '', '', ['关机请求']],
                ['', ['开机请求'], '', '', ['送风请求', '22', ''], '', '', ['送风请求', '', 'high'], '', '', '', '',
                 ['送风请求', '', 'low'], '', '', ['送风请求', '20', 'high'], '', '', '', '', ['送风请求', '25', ''],
                 '', '', ['关机请求'], '', '']
            ]
            times = 1
            t = time.time()
            for i in range(5):
                if msg0[i][0] != '':
                    if len(msg0[i][0]) == 1:
                        self.msg(i + 1, msg0[i][0][0])
                    else:
                        self.msg(i + 1, msg0[i][0][0], msg0[i][0][1], msg0[i][0][2])
            strS = ''
            strW = ''
            time.sleep(2)
            for item in self.dp.queueS:
                strS += str(item['roomID']) + ' '
            for item in self.dp.queueW:
                strW += str(item['roomID']) + ' '
            while 1:
                if times >= 26:
                    dflist = []
                    time.sleep(5)
                    t0 = time.time()
                    for i in range(5):
                        tem = self.temSet[self.temID[i]]
                        tem.runState = 'closed'
                        df = front_desk.print_bill(self.dp.check_table, i + 1, round(tem.totalCost, 4))
                        self.insert(df, 'bill' + str(i + 1) + '.xlsx')
                        if i + 1 == roomID:
                            dflist.append(df)
                    for i in range(5):
                        df = front_desk.print_details(self.dp.details_table, i + 1)
                        self.insert(df, 'details' + str(i + 1) + '.xlsx')
                        if i + 1 == roomID:
                            dflist.append(df)
                    return dflist[type]

                while (time.time() - t) >= 10:
                    t1 = time.time()
                    for i in range(5):
                        if msg0[i][times] != '':
                            if len(msg0[i][times]) == 1:
                                self.msg(i + 1, msg0[i][times][0])
                            else:
                                self.msg(i + 1, msg0[i][times][0], msg0[i][times][1], msg0[i][times][2])
                    t2 = time.time()
                    strS = ''
                    strW = ''
                    time.sleep(2)
                    for item in self.dp.queueS:
                        strS += str(item['roomID']) + ' '
                    for item in self.dp.queueW:
                        strW += str(item['roomID']) + ' '
                    t += 10
                    times += 1

if __name__ == '__main__':
    server = Server()
    server.try_test(1, 1)
