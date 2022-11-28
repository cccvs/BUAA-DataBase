# coding=utf-8
import pymysql
from django.http import HttpResponse


def connectDatabase():
    connect = pymysql.connect(host="localhost", db="club_system", user="root",
                              passwd="123456", charset="utf8")  # replace my password with 123456
    cursor = connect.cursor()
    return connect, cursor


def closeDatabase(connect, cursor):
    connect.close()
    cursor.close()


def createUser(userID: str, password: str, name: str, email: str):
    # create logical part
    connect, cursor = connectDatabase()
    ins = 'insert into user(user_id, password, time, real_name, email)' \
          'values (%s, %s, CURRENT_TIMESTAMP, %s, %s)'
    cursor.execute(ins, [userID, password, name, email])
    connect.commit()

    return HttpResponse({'code': 0})


def getUser(userId: str):
    connect, cursor = connectDatabase()
    ins = "select * from user where user_id = %s"
    cursor.execute(ins, [userId])
    result = cursor.fetchall()
    closeDatabase(connect, cursor)
    return result


# createUser('a', 'b', 'c', 'd')
# createUser('aa', 'bb', 'cc', 'dd')

conn, cursor = connectDatabase()
# cursor.execute('show databases')
cursor.execute('select * from user')
x = cursor.fetchall()
print(x)
