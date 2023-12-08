import pymysql
from passlib.hash import argon2
import json


def database():
    with open("config/database_config.json") as fp:
        database_settings = json.load(fp)

    host = database_settings["host"]
    user = database_settings["user"]
    password = database_settings["password"]
    port = database_settings["port"]
    database = database_settings["database"]
    charset = database_settings["charset"]

    db = pymysql.connect(host=host, database=database, user=user, password=password, port=port, charset=charset)
    return db



class UserTable:
    def __init__(self, db):
        self.db = db

    # 插入新用户数据
    def insert(self, username, password):
        # 建立连接
        self.cursor = self.db.cursor()
        # 插入表的sql
        sql = 'insert into users (username,password) values (%s,%s);'

        try:
            self.cursor.execute(sql, [username, argon2.hash(password)])
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            self.cursor.close()

    # 验证用户密码
    def check_password(self, username, password):
        # 建立连接
        self.cursor = self.db.cursor()
        # 查询表的sql
        sql = 'select password from users where username = %s;'

        try:
            self.cursor.execute(sql, username)
            hashed_password = self.cursor.fetchone()[0]  # 取元组中的第一个值
            return argon2.verify(password, hashed_password)
        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            self.cursor.close()

    # 判断用户名是否存在
    def exist(self, username):
        # 建立连接
        self.cursor = self.db.cursor()
        # 计算表中指定用户名的总个数的sql
        sql = 'select count(1) from users where username = %s;'

        try:
            self.cursor.execute(sql, username)
            count = self.cursor.fetchone()[0]
            return count != 0
        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            self.cursor.close()

    # 删除用户信息
    def delete(self, username):
        # 建立连接
        self.cursor = self.db.cursor()
        # 删除表中指定用户名对应行的sql
        sql = 'delete from users where username = %s;'

        try:
            self.cursor.execute(sql, username)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            self.cursor.close()


class CheckTable:
    def __init__(self, db):
        self.db = db

    # 创建房间表
    def create_table(self):
        # 建立连接
        self.cursor = self.db.cursor()
        # 创建表的sql
        sql = 'create table if not exists checks (check_id int primary key auto_increment, room_id int, ' \
              'check_time timestamp default current_timestamp);'

        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            self.cursor.close()

    # 删除房间表
    def drop_table(self):
        # 建立连接
        self.cursor = self.db.cursor()
        # 删除表的sql
        sql = 'drop table if exists checks;'

        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            self.cursor.close()

    # 登记房间入住时间
    def check_in(self, room_id):
        # 建立连接
        self.cursor = self.db.cursor()
        # 插入表的sql
        sql = 'insert into checks (room_id) values (%s);'

        try:
            self.cursor.execute(sql, room_id)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            self.cursor.close()

    # 查询房间所有登记记录
    def fetch_all(self, room_id):
        # 建立连接
        self.cursor = self.db.cursor()
        # 查询表的sql
        sql = 'select check_time from checks where room_id = %s;'

        try:
            self.cursor.execute(sql, room_id)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            self.cursor.close()

    # 逐条查询房间登记记录
    def fetch_one(self, room_id):
        # 建立连接
        self.cursor = self.db.cursor()
        # 查询表的sql
        sql = 'select check_time from checks where room_id = %s;'
        try:
            self.cursor.execute(sql, room_id)
            return self.cursor.fetchone()
        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            self.cursor.close()


class DetailsTable:
    def __init__(self, db):
        self.db = db

    # 创建详单表
    def create_table(self):
        # 建立连接
        self.cursor = self.db.cursor()
        # 创建表的sql
        sql = 'create table if not exists details (detail_id int primary key auto_increment, room_id int,' \
              'event_time timestamp default current_timestamp, event_type varchar(50), wind_speed varchar(50),' \
              'room_state varchar(50), cost float);'

        try:
            self.cursor.execute(sql)
            self.db.commit()

        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            self.cursor.close()

    # 删除详单表
    def drop_table(self):
        # 建立连接
        self.cursor = self.db.cursor()
        # 删除表的sql
        sql = 'drop table if exists details;'

        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            self.cursor.close()

    # 插入详单数据
    def insert(self, room_id, event_type, room_wind_speed, room_state, cost):
        # 建立连接
        self.cursor = self.db.cursor()
        # 插入表的sql
        sql = 'insert into details (room_id, event_type, wind_speed, room_state, cost) values (%s,%s,%s,%s,%s);'

        try:
            self.cursor.execute(sql, [room_id, event_type, room_wind_speed, room_state, cost])
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            self.cursor.close()

    # 查询所有详单数据
    def fetch_all(self, room_id):
        # 建立连接
        self.cursor = self.db.cursor()
        # 查询表的sql
        sql = 'select event_time, event_type, wind_speed, room_state, cost from details where room_id = %s;'

        try:
            self.cursor.execute(sql, room_id)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            self.cursor.close()

    # 逐条查询详单数据
    def fetch_one(self, room_id):
        # 建立连接
        self.cursor = self.db.cursor()
        # 查询表的sql
        sql = 'select * from details where room_id = %s;'

        try:
            self.cursor.execute(sql, room_id)
            return self.cursor.fetchone()
        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            self.cursor.close()
