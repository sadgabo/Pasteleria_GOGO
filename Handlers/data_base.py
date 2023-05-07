import pymysql


def Conection() -> pymysql.connections.Connection:
    return pymysql.connect(host='localhost', user='root',passwd='1234',db='pasteleria')
