from database import database, CheckTable, DetailsTable
import time
import pandas as pd
import ServerDispatch
from datetime import datetime


def create_check_table(db):
    # 打开数据库
    check_table = CheckTable(db)
    check_table.drop_table()
    check_table.create_table()
    return check_table


# 打印账单
def print_bill(check_table, room_id):
    check_in_time = check_table.fetch_one(room_id)[0]

    check_in_time = check_in_time.strftime("%Y-%m-%d %H:%M:%S")
    print(check_in_time)
    check_out_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(check_out_time)

    df = pd.DataFrame({'房间号': [room_id], '入住时间': [check_in_time], '离开时间': [check_out_time]})
    df.to_excel('bill.xlsx', index=False)


# 创建详单表
def create_details_table(db):
    # 打开数据库
    details_table = DetailsTable(db)
    details_table.drop_table()
    details_table.create_table()
    return details_table


class DetailsList:
    def __init__(self):
        self.request_time = None
        self.service_start_time = None
        self.service_end_time = None
        self.wind_speed = None
        self.room_state = 'closed'

    def check_room_state(self, event_time, room_state):
        if self.room_state != 'running' and room_state == 'running':
            self.service_start_time = event_time
            return False
        elif self.room_state == 'running' and room_state != 'running':
            self.service_end_time = event_time
            return True
        else:
            return False


# 打印详单
def print_details(details_table, room_id):
    detail_tuples = details_table.fetch_all(room_id)
    detail_list = [list(detail_tuple) for detail_tuple in detail_tuples]
    event_time = [detail[0] for detail in detail_list]
    event_type = [detail[1] for detail in detail_list]
    wind_speed = [detail[2] for detail in detail_list]
    room_state = [detail[3] for detail in detail_list]
    cost = [detail[4] for detail in detail_list]
    details_list = DetailsList()
    df = pd.DataFrame(columns=['房间号', '请求时间', '服务开始时间', '服务结束时间', '服务时长', '风速', '当前费用', '费率'])

    for i in range(len(event_type)):

        if event_type[i] == '开机':
            if details_list.room_state != 'running' and room_state == 'running':
                details_list.service_start_time = event_time
            details_list.request_time = event_time[i]
            details_list.wind_speed = wind_speed[i]
            details_list.room_state = room_state[i]
        elif event_type[i] == '修改风速':
            if details_list.room_state == 'running':
                details_list.service_end_time = event_time[i]
                df = df.append({'房间号': room_id, '请求时间': details_list.request_time,
                                '服务开始时间': details_list.service_start_time,
                                '服务结束时间': details_list.service_end_time,
                                '服务时长': str(details_list.service_end_time - details_list.service_start_time),
                                '风速': details_list.wind_speed, '当前费用': cost[i], '费率': 1}, ignore_index=True)
            if room_state[i] == 'running':
                details_list.service_start_time = event_time[i]
            elif details_list.check_room_state(event_time[i], room_state[i]):
                df = df.append({'房间号': room_id, '请求时间': details_list.request_time,
                                '服务开始时间': details_list.service_start_time,
                                '服务结束时间': details_list.service_end_time,
                                '服务时长': str(details_list.service_end_time - details_list.service_start_time),
                                '风速': details_list.wind_speed, '当前费用': cost[i], '费率': 1}, ignore_index=True)
            details_list.wind_speed = wind_speed[i]
            details_list.room_state = room_state[i]
        elif event_type[i] == '关机':
            if details_list.room_state == 'running':
                details_list.service_end_time = event_time[i]
                df = df.append({'房间号': room_id, '请求时间': details_list.request_time,
                                '服务开始时间': details_list.service_start_time,
                                '服务结束时间': details_list.service_end_time,
                                '服务时长': str(details_list.service_end_time - details_list.service_start_time),
                                '风速': details_list.wind_speed, '当前费用': cost[i], '费率': 1}, ignore_index=True)

    df.to_excel('details.xlsx', index=False)


if __name__ == '__main__':
    database = database()

    # check_table = create_check_table(database)
    # # 登记房间入住时间
    # check_table.check_in(1)
    # # 打印账单
    # print_bill(check_table, 1)
    dp = ServerDispatch.Dispatch(database)

    details_table = create_details_table(database)

    dp.Insert(1, '开机', 'mid', 'waiting', 0)
    time.sleep(1)
    dp.Insert(1, '修改风速', 'high', 'running', 0)
    time.sleep(1)
    dp.Insert(1, '修改风速', 'mid', 'running', 1)

    dp.Insert(1, '关机', 'low', 'closed', 1)
    time.sleep(5)
    t1=time.time()
    print_details(dp.details_table, 1)
    print(time.time()-t1)

    database.close()