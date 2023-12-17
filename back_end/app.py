"""
@ 文件名：  app.py
@ 文件功能描述： 服务器端的路由接口
@ 创建人：   田健豪
@ 创建日期： 2023年12月7日

@ 修改描述： 增加路由login，用于实现登录逻辑
@ 修改人：  田健豪
@ 修改日期： 2023年12月11日

@ 修改描述： 增加路由get_bill和get_details，用于打印账单和详单
@ 修改人：  田健豪
@ 修改日期： 2023年12月13日

@ 修改描述： 增加路由server_on，用于开启服务器
@ 修改人：  田健豪
@ 修改日期： 2023年12月14日

@ 修改描述： 增加路由power_on，power_off，set_wind_speed，用于开关机和调节风速
@ 修改人：  田健豪
@ 修改日期： 2023年12月14日

@ 修改描述： 增加路由update_control_panel，用于更新控制面板
@ 修改人：  田健豪
@ 修改日期： 2023年12月14日

@ 修改描述： 增加路由get_room_info，用于获取房间的信息
@ 修改人：  田健豪
@ 修改日期： 2023年12月14日

@ 修改描述： 增加初始化实例server，用于调用后端逻辑
@ 修改人：  田健豪
@ 修改日期： 2023年12月14日

@ 修改描述： 修改路由set_wind_speed，接收正确的目标温度值
@ 修改人：  田健豪
@ 修改日期： 2023年12月15日

@ 修改描述： 增添代码注释
@ 修改人：  田健豪
@ 修改日期： 2023年12月17日
"""

import flask
from flask import request, make_response

from database import database, UserTable
from runDispatch import Server

app = flask.Flask(__name__)
server = Server()

@app.post('/login')
def login():
    db = database()
    users = UserTable(db)
    username = request.form.get('username')
    password_input = request.form.get('password_input')
    # 检查用户名和密码是否正确
    if users.exist(username) and users.check_password(username, password_input):
        response_entity = make_response({
            "result": "OK"
        }, 200)
    else:
        response_entity = make_response({
            "result": "error"
        }, 403)
    return response_entity


@app.post('/update_control_panel')
def update_control_panel():
    room_id = request.form.get('room_id')
    dict = server.schedule(int(room_id))  # 传入房间号，返回该房间的信息
    response_entity = make_response(dict, 200)
    return response_entity


@app.post('/power_on')
def power_on():
    room_id = request.form.get('room_id')
    wind_speed = request.form.get('wind_speed')
    target_temperature = request.form.get('target_temperature')
    event_type = '开机请求'
    dict = server.schedule(int(room_id), event_type, target_temperature, wind_speed)  # 传入房间号，事件类型，目标温度，风速
    response_entity = make_response(dict, 200)

    return response_entity


@app.post('/power_off')
def power_off():
    room_id = request.form.get('room_id')
    event_type = '关机请求'
    dict = server.schedule(int(room_id), event_type)  # 传入房间号，事件类型
    response_entity = make_response(dict, 200)
    return response_entity


@app.post('/set_wind_speed')
def set_wind_speed():
    room_id = request.form.get('room_id')
    wind_speed = request.form.get('wind_speed')
    temperture = request.form.get('target_temperature')
    event_type = '送风请求'
    dict = server.schedule(int(room_id), event_type, temperture, wind_speed)  # 传入房间号，事件类型，目标温度，风速
    response_entity = make_response(dict, 200)
    return response_entity


@app.get('/get_room_info')
def get_room_info():
    dict_list = server.monitor()  # 返回所有房间的信息
    response_entity = make_response({
        'room_info': dict_list
    }, 200)
    return response_entity


@app.post('/server_on')
def server_on():
    price = request.form.get('price')
    mode = request.form.get('mode')
    server.setPrice(float(price))  # 设置费率
    server.setModel(mode)  # 设置模式
    server.try_test()  # 开启测试，会检查paramConfig文件设置，如果是测试模式则会开启测试，否则不会开启

    response_entity = make_response({
        'result': 'OK'
    }, 200)
    return response_entity


@app.get('/server_off')
def server_off():
    server.closeServer()  # 关闭服务器
    response_entity = make_response({
        'result': 'OK'
    }, 200)
    return response_entity

@app.post('/print_bill')
def print_bill():
    room_id = request.form.get('room_id')
    df = server.ask_bill(int(room_id))  # 传入房间号，返回DataFrame类型的账单
    result = df.to_dict(orient='list')  # 将DataFrame转换为字典的列表
    response_entity = make_response({
        'bill': result
    }, 200)
    return response_entity


@app.post('/print_details')
def print_details():
    room_id = request.form.get('room_id')
    df = server.ask_details(int(room_id))  # 传入房间号，返回DataFrame类型的详单
    result = df.to_dict(orient='list')   # 将DataFrame转换为字典的列表
    response_entity = make_response({
        'bill': result
    }, 200)
    return response_entity


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)