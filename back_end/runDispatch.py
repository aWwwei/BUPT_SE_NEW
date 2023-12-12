'''
@ 文件名：runDispatch.py
@ 文件功能描述：调度的封装接口
@ 创建日期：2023年12月7日
@ 创建人：任波
'''
import front_desk
import ServerDispatch
import TempControl
import time
import threading

Room = set()
temopen=0
database = front_desk.database()
dp = ServerDispatch.Dispatch(database)
temSet=[]
temID=[0]*40
queueP=[]

def setPrice(p):
    dp.setPrice(p)

def msg(dp,roomID,env_type='开机请求',temp='',speed=''):

    # 检查 roomID 是否存在于集合 Room 中
    if roomID not in Room:
        # 如果 roomID 不存在于集合 Room 中，则将其添加到集合中
        Room.add(roomID)
        dp.Insert(roomID,'账单','0','0','0')
        tem = TempControl.TempControl(roomID,dp)
        temID[roomID - 1]=len(temSet)
        temSet.append(tem)

    else:
        tem =temSet[temID[roomID-1]]
    if env_type =='开机请求':
        if tem.runState=='close':
            if len(dp.queueS)<3:
                tem.runState = 'running'
            else:
                tem.runState = 'waiting'
            tem.tempSet = 25
            tem.speedSet = 'mid'
            tem.cost = tem.totalCost
            dp.Insert(roomID, '开机', 'mid', tem.runState, round(tem.totalCost, 4))
            dp.requestWind(tem.roomID, 2)

    elif env_type =='送风请求':
        if temp!='':
            tem.tempSet = (int(temp))

        if speed == 'high':
            tem.speedSet = 'high'
            dp.requestWind(tem.roomID, 3)
            dp.Insert(roomID, '修改风速', 'high', tem.runState, round(tem.totalCost, 4))

        elif speed == 'mid':
            tem.speedSet = 'mid'
            dp.requestWind(tem.roomID, 2)
            dp.Insert(roomID, '修改风速', 'mid', tem.runState, round(tem.totalCost, 4))

        elif speed == 'low':
            tem.speedSet = 'low'
            dp.requestWind(tem.roomID, 1)
            dp.Insert(roomID, '修改风速', 'low', tem.runState, round(tem.totalCost, 4))

    elif env_type =='关机请求':
        
        tem.runState = 'close'
        dp.stopWind(tem.roomID)
        time.sleep(0.2)
        dp.Insert(roomID, '关机', 'low', 'close', round(tem.totalCost, 4))

    dic = {'当前温度': round(tem.tempNow, 4),
               '目标温度': tem.tempSet,
               '风速': tem.speedSet,
               '状态': tem.runState,
               '当前费用': round(tem.totalCost - tem.cost, 4),
               '总费用': round(tem.totalCost, 4)}
    if roomID==2:
        print(env_type)
        print(dic)
    return dic

def monitor():
    dic=[]
    for i in range(5):
        tem = temSet[temID[i]]
        dic.append({'当前温度': round(tem.tempNow, 4),
               '目标温度': tem.tempSet,
               '风速': tem.speedSet,
               '状态': tem.runState,
               '当前费用': round(tem.totalCost - tem.cost, 4),
               '总费用': round(tem.totalCost, 4)})
    return dic

def schedule(roomID,env_type='开机请求',temp='',speed=''):
    msg(dp, roomID, env_type, temp, speed)

msg0 = [
        [['开机请求'], ['送风请求','18',''],'', '','', ['送风请求','','high'], '', '', '', ['送风请求','22',''], '', '', '', '', ['关机请求'], '', '', '', ['开机请求'], '', '', '',
         '', '', ['关机请求'], ''],
        ['', ['开机请求'], '', ['送风请求','19',''], '', '', ['关机请求'], ['开机请求'], '', '', '', ['送风请求','22',''], '', '', '', '', ['关机请求'], '', '', ['开机请求'], '',
         '', '', '', '', ['关机请求']],
        ['', '', ['开机请求'], '', '', '', '', '', '', '', '', '', '', '', ['送风请求','24','low'], '', '', ['送风请求','','high'], '', '', '', '', ['关机请求'],
         '', '', ''],
        ['', '', '', ['开机请求'], '', '', '', '', '', ['送风请求','18','high'], '', '', '', '', '', '', '', '', ['送风请求','20','mid'], '', '', '', '',
         '', '', ['关机请求']],
        ['', ['开机请求'], '', '', ['送风请求','22',''], '', '', ['送风请求','','high'], '', '', '', '', ['送风请求','','low'], '', '', ['送风请求','20','high'], '', '', '', '', ['送风请求','25',''],
         '', '', ['关机请求'], '', '']
        ]

def insert(df,path):
    queueP.append([df,path])

def dfprint():
    i=0
    t=time.time()
    while i <10:
        time.sleep(1)
        if len(queueP) != 0:
            item = queueP.pop(0)
            print(i+1,item)
            item[0].to_excel(item[1], index=False)
            i += 1
    print('写入完成,用时', time.time() - t)
    database.close()

def try_test():
    if dp.flag:
        times = 1
        t = time.time()
        for i in range(5):
            if msg0[i][0] != '':
                if len(msg0[i][0]) == 1:
                    msg(dp, i + 1, msg0[i][0][0])
                else:
                    msg(dp, i + 1, msg0[i][0][0], msg0[i][0][1], msg0[i][0][2])
        strS = ''
        strW = ''
        time.sleep(2)
        for item in dp.queueS:
            strS += str(item['roomID']) + ' '
        for item in dp.queueW:
            strW += str(item['roomID']) + ' '
        print('服务队列：', strS)
        print('等待队列：', strW)
        while 1:
            if times >= 26:
                time.sleep(5)
                dp.stop_Insert()
                thread = threading.Thread(target=dfprint)  # 创建线程
                thread.start()  # 启动线程
                print('开始写入')
                t0 = time.time()
                for i in range(5):
                    tem = temSet[temID[i]]
                    df=front_desk.print_bill(dp.check_table, i + 1,round(tem.totalCost, 4))
                    insert(df, 'bill' + str(i + 1) + '.xlsx')
                for i in range(5):
                    df=front_desk.print_details(dp.details_table, i + 1)
                    insert(df, 'details' + str(i + 1) + '.xlsx')
                print('主程序运行完成,用时', time.time() - t0)
                break
            while (time.time() - t) >= 10:
                print('时间：', times)
                t1 = time.time()
                for i in range(5):
                    if msg0[i][times] != '':
                        if len(msg0[i][times]) == 1:
                            msg(dp, i + 1, msg0[i][times][0])
                        else:
                            msg(dp, i + 1, msg0[i][times][0], msg0[i][times][1], msg0[i][times][2])
                t2 = time.time()
                print(t2 - t1)
                strS = ''
                strW = ''
                time.sleep(2)
                for item in dp.queueS:
                    strS += str(item['roomID']) + ' '
                for item in dp.queueW:
                    strW += str(item['roomID']) + ' '
                print(time.time() - t - 10)
                print('服务队列：', strS)
                print('等待队列：', strW)
                t += 10
                times += 1
        
if __name__ == '__main__':
    try_test()
     
