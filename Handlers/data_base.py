import pymysql


def Conection() -> pymysql.connections.Connection:
    return pymysql.connect(host='localhost', user='root',passwd='123',db='pasteleria')
