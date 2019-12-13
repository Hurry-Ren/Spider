import pymysql

host = "127.0.0.1"
user = "root"
passwd = "root"
db = "dangdang"

def connect():
    conn = pymysql.connect(host = host , user = user , passwd = passwd , db = db)
    return conn