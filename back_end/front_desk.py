"""
@ 文件名：  front_desk.py
@ 文件功能描述： 前台打印账单和详单的逻辑
@ 创建人：   田健豪
@ 创建日期： 2023年12月7日

@ 修改描述： 增加函数create_check_table，用于创建账单表
@ 修改人：  田健豪
@ 修改日期： 2023年12月7日

@ 修改描述： 增加函数create_details_table，用于创建详单表
@ 修改人：  田健豪
@ 修改日期： 2023年12月7日

@ 修改描述： 增加函数print_bill，用于打印账单
@ 修改人：  田健豪
@ 修改日期： 2023年12月7日

@ 修改描述： 增加类DetailsList，用于存储详单信息
@ 修改人：  田健豪
@ 修改日期： 2023年12月7日

@ 修改描述： 增加函数print_details，用于打印详单
@ 修改人：  田健豪
@ 修改日期： 2023年12月7日

@ 修改描述： 修改print_details存储时间的格式
@ 修改人：  田健豪
@ 修改日期： 2023年12月7日
"""


from database import database, CheckTable, DetailsTable
import time
import pandas as pd


def create_check_table(db):
    # 打开数据库
    check_table = CheckTable(db)
    check_table.drop_table()
    check_table.create_table()
    return check_table


# 打印账单
def print_bill(check_table, room_id, total_cost):
    check_in_time = check_table.fetch_one(room_id)[0]

    check_in_time = check_in_time.strftime("%Y-%m-%d %H:%M:%S")
    check_out_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    df = pd.DataFrame({'房间号': [room_id], '入住时间': [check_in_time], '离开时间': [check_out_time], '总费用': [total_cost]})
    return df
    #df.to_excel('bill.xlsx', index=False)


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
        # 从非运行状态到运行状态
        if self.room_state != 'running' and room_state == 'running':
            self.service_start_time = event_time
            return False
        # 从运行状态到非运行状态
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
            if details_list.room_state != 'running' and room_state[i] == 'running':
                details_list.service_start_time = event_time[i]
            details_list.request_time = event_time[i]
            details_list.wind_speed = wind_speed[i]
            details_list.room_state = room_state[i]
        elif event_type[i] == '修改风速':
            if details_list.room_state == 'running':
                details_list.service_end_time = event_time[i]
                df = df.append({'房间号': room_id, '请求时间': details_list.request_time.strftime("%Y-%m-%d %H:%M:%S"),
                                '服务开始时间': details_list.service_start_time.strftime("%Y-%m-%d %H:%M:%S"),
                                '服务结束时间': details_list.service_end_time.strftime("%Y-%m-%d %H:%M:%S"),
                                '服务时长': str(details_list.service_end_time - details_list.service_start_time),
                                '风速': details_list.wind_speed, '当前费用': cost[i], '费率': 1}, ignore_index=True)
                if room_state[i] == 'running':
                    details_list.service_start_time = event_time[i]
            elif details_list.check_room_state(event_time[i], room_state[i]):
                df = df.append({'房间号': room_id, '请求时间': details_list.request_time.strftime("%Y-%m-%d %H:%M:%S"),
                                '服务开始时间': details_list.service_start_time.strftime("%Y-%m-%d %H:%M:%S"),
                                '服务结束时间': details_list.service_end_time.strftime("%Y-%m-%d %H:%M:%S"),
                                '服务时长': str(details_list.service_end_time - details_list.service_start_time),
                                '风速': details_list.wind_speed, '当前费用': cost[i], '费率': 1}, ignore_index=True)
            details_list.wind_speed = wind_speed[i]
            details_list.room_state = room_state[i]
        elif event_type[i] == '关机':
            if details_list.room_state == 'running':
                details_list.service_end_time = event_time[i]
                df = df.append({'房间号': room_id, '请求时间': details_list.request_time.strftime("%Y-%m-%d %H:%M:%S"),
                                '服务开始时间': details_list.service_start_time.strftime("%Y-%m-%d %H:%M:%S"),
                                '服务结束时间': details_list.service_end_time.strftime("%Y-%m-%d %H:%M:%S"),
                                '服务时长': str(details_list.service_end_time - details_list.service_start_time),
                                '风速': details_list.wind_speed, '当前费用': cost[i], '费率': 1}, ignore_index=True)
            details_list.room_state = room_state[i]

    return df


if __name__ == '__main__':
    database = database()

    check_table = create_check_table(database)
    # 登记房间入住时间
    check_table.check_in(1)
    # 打印账单
    print_bill(check_table, 1, 1)
    database.close()
