# coding=utf-8
import pymysql


def connect_database():
    conn = pymysql.connect(host="localhost", db="club_system", user="root",
                           passwd="123456", charset="utf8") # replace my password with 123456
    cursor = conn.cursor()
    return conn, cursor


def create_user():
    pass

conn, cursor = connect_database()
cursor.execute('show databases')
print(cursor.fetchall())
# cursor.execute('insert into user(`user_id`, `user_name`, `password`, `time`, `email`) '
#                'values(UUID_TO_BIN(UUID()), \'a\', \'a\', CURRENT_TIMESTAMP, \'sb\')')
cursor.execute('select * from user')
print(cursor.fetchall())
# cursor.execute('select * from ')
