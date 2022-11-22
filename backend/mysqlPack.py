# coding=utf-8
import pymysql
import jwt
from django.http import HttpResponse


def connectDatabase():
    connect = pymysql.connect(host="localhost", db="club_system", user="root",
                              passwd="123456", charset="utf8")  # replace my password with 123456
    cursor = connect.cursor()
    return connect, cursor


def createUser(userID, password, name, email):
    connect, cursor = connectDatabase()
    ins = 'insert into user(user_id, password, time, real_name, email)' \
          'values (%s, %s, CURRENT_TIMESTAMP, %s, %s)'
    cursor.execute(ins, [userID, password, name, email])
    connect.commit()
    return HttpResponse({'code': 0})


def findUser(userId: str):
    connect, cursor = connectDatabase()
    ins = "select * from user where user_id = %s"
    cursor.execute(ins, [userId])
    print(cursor.fetchall())
    connect.commit()


code = jwt.encode(payload={'user_id': 'a'}, algorithm='HS256', key='s', headers={"typ": "JWT", "alg": "HS256"})
print(code)
# createUser('a', 'b', 'c', 'd')
# createUser('aa', 'bb', 'cc', 'dd')

# conn, cursor = connectDatabase()
# cursor.execute('show databases')
# cursor.execute('select * from user')
# print(cursor.fetchall())
