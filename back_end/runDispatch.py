'''
@ 文件名：runDispatch.py
@ 文件功能描述：调度的封装接口
@ 创建日期：2023年12月7日
@ 创建人：任波
'''
import ServerDispatch
import TempControl

dp=ServerDispatch.Dispatch()
Room = set()
roomBook=[]
IDBook=[0]*40
def msg(roomID,env_type='开机请求',speed='',temp=''):
    # 检查 roomID 是否存在于集合 Room 中
    if roomID not in Room:
        # 如果 roomID 不存在于集合 Room 中，则将其添加到集合中
        Room.add(roomID)
        tem = TempControl(roomID,dp)
        IDBook[roomID-1]=len(roomBook)
        roomBook.append(tem)
    else:
        tem =roomBook[IDBook[roomID-1]]
    if env_type =='开机请求':
        if tem.runState=='close':
            TempControl.runTest(dp,tem,'open')
            return '请求成功'
        else:
            return '已经开机，请勿重复请求'
    elif env_type =='送风请求':
        TempControl.runTest(dp,tem,(str(temp)+','+str(speed)))

    elif env_type =='关机请求':
        TempControl.runTest(dp,tem,'close')