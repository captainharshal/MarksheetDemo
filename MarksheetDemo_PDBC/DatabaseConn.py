import pymysql

def getConnection(dbname=None):
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="root", database=dbname)
    return conn