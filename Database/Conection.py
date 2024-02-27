import pymysql

def connection():
    conn = pymysql.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "",
        database = "ferreteria_proyecto",
    )
    
    print("Base de datos conectada")
    return conn