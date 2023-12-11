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

Room = set()
temopen=0
database = front_desk.database()
dp = ServerDispatch.Dispatch(database)
temSet=[]
temID=[0]*40

def setPrice(p):
    dp.setPrice(p)

def msg(dp,roomID,env_type='开机请求',temp='',speed=''):

    # 检查 roomID 是否存在于集合 Room 中
    if roomID not in Room:
        # 如果 roomID 不存在于集合 Room 中，则将其添加到集合中
        Room.add(roomID)
        #dp.check_table.check_in(roomID)
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

    dic = {'temp':round(tem.tempNow, 4),
           'tempSet':tem.tempSet,
           'speed': tem.speedSet,
           'runState': tem.runState,
           'totalCost': round(tem.totalCost, 4)}
    if roomID==2:
        print(env_type)
        print(dic)
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
if __name__ == '__main__':

    times = 1
    t = time.time()
    for i in range(5):
        if msg0[i][0] != '':
            if len(msg0[i][0])==1:
                msg(dp, i + 1, msg0[i][0][0])
            else:
                msg(dp, i + 1, msg0[i][0][0],msg0[i][0][1],msg0[i][0][2])
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
            print('开始写入')
            t0=time.time()
            for i in range(5):
                front_desk.print_details(dp.details_table, i+1,'details'+str(i+1)+'.xlsx')
            print('写入完成,用时',time.time()-t0)
            print(time.time()-t0)
            database.close()
            break
        while (time.time() - t) >= 10:
            print('时间：',times)
            t1 = time.time()
            for i in range(5):
                if msg0[i][times] != '':
                    if len(msg0[i][times]) == 1:
                        msg(dp,i + 1, msg0[i][times][0])
                    else:
                        msg(dp,i + 1, msg0[i][times][0], msg0[i][times][1], msg0[i][times][2])
            t2 = time.time()
            print(t2 - t1)
            strS = ''
            strW = ''
            time.sleep(2)
            for item in dp.queueS:
                strS += str(item['roomID']) + ' '
            for item in dp.queueW:
                strW += str(item['roomID']) + ' '
            print(time.time() - t-10)
            print('服务队列：', strS)
            print('等待队列：', strW)
            t += 10
            times += 1


