'''
@ 文件名：ReadConfig.py
@ 文件功能描述：读取预设参数
@ 创建人：任波
@ 创建日期：2023年11月27日
'''
import configparser


class Config:
    @staticmethod
    def getDispatch():
        cf = configparser.ConfigParser()
        cf.read("paramConfig.ini", encoding="utf-8")
        dispatch = cf.items("DISPATCH")
        dispatch = dict(dispatch)
        return dispatch

    @staticmethod
    def getTempcontrol():
        cf = configparser.ConfigParser()
        cf.read("paramConfig.ini", encoding="utf-8")
        tempcontrol = cf.items("TEMPCONTROL")
        tempcontrol = dict(tempcontrol)
        return tempcontrol

    @staticmethod
    def getBegintemp():
        cf = configparser.ConfigParser()
        cf.read("paramConfig.ini", encoding="utf-8")
        beginTemp = cf.items("BEGINTEMP")
        beginTemp = dict(beginTemp)
        return beginTemp
