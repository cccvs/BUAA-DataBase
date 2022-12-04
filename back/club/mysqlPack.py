# coding=utf-8
import pymysql
from back.settings import DATABASES

clubTypeToNum = {'科技': 0, '人文': 1, '实践': 2, '体育': 3, '艺术': 4, '其它': 5}
numToClubType = ['科技', '人文', '实践', '体育', '艺术', '其它']


def connectDatabase():
    database = DATABASES['default']
    connect = pymysql.connect(host=database['HOST'], db=database['NAME'], user=database['USER'],
                              passwd=database['PASSWORD'], charset="utf8")  # replace my password with 123456
    cursor = connect.cursor()
    return connect, cursor


def closeDatabase(connect, cursor):
    connect.close()
    cursor.close()


def createUser(userId: str, password: str, name: str, email: str):
    connect, cursor = connectDatabase()
    try:
        ins = 'insert into user(user_id, password, time, real_name, email, followers, following) values (%s, %s, CURRENT_TIMESTAMP, %s, %s, 0, 0);'
        cursor.execute(ins, [userId, password, name, email])
    except Exception as e:
        print(e)
        connect.rollback()
    connect.commit()
    return


# 需要userId和用户Id完全匹配
def getUser(userId: str):
    connect, cursor = connectDatabase()
    result = ''
    try:
        ins = 'select * from user where user_id = %s;'
        cursor.execute(ins, [userId])
        result = cursor.fetchall()
    except Exception as e:
        connect.rollback()
        raise e
    closeDatabase(connect, cursor)
    return result


def createClub(name: str, type: str, masterId: str):
    typeNum = clubTypeToNum[type]
    connect, cursor = connectDatabase()
    try:
        ins = 'insert into club(club_id, name, member_count, type, master_id, time) value (UUID_TO_BIN(UUID()), %s, 0, %s, %s, CURRENT_TIMESTAMP);'
        cursor.execute(ins, [name, typeNum, masterId])
    except Exception as e:
        print(e)
        connect.rollback()
    closeDatabase(connect, cursor)
    return


def findClub(keyWord: str):
    connect, cursor = connectDatabase()
    result = ''
    try:
        ins = 'select * from club where name like %s;'
        cursor.execute(ins, ['%' + keyWord + '%'])  # 子串匹配
        result = cursor.fetchall()
    except Exception as e:
        print(e)
        connect.rollback()
    closeDatabase(connect, cursor)
    return result

# createUser('a', 'b', 'c', 'd')
# createUser('aa', 'bb', 'cc', 'dd')

# conn, cursor = connectDatabase()
# cursor.execute('show databases')
# cursor.execute('select * from user')
# x = cursor.fetchall()
# print(x)
