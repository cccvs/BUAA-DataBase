# coding=utf-8
import pymysql
import os
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


def initDatabase():
    database = DATABASES['default']
    base = 'back/database/'
    sqlFiles = ['create.sql', 'function.sql', 'procedure.sql',
                'trigger.sql', 'init.sql']
    # excute
    os.system('mysql -V')
    for name in sqlFiles:
        os.system('mysql -u root -p' + database['PASSWORD'] + ' < ' + base + name)


# func
def createUser(userId: str, password: str, name: str, sex: str, institute: str, email: str):
    connect, cursor = connectDatabase()
    try:
        ins = 'insert into user(user_id, password, time, real_name, sex, institute, email, followers, following) values (%s, %s, CURRENT_TIMESTAMP, %s, %s, %s, %s, 0, 0);'
        cursor.execute(ins, [userId, password, name, sex, institute, email])
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
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
    finally:
        closeDatabase(connect, cursor)
    return result


def createClub(name: str, type: str, masterId: str, intro: str):
    typeNum = clubTypeToNum[type]
    connect, cursor = connectDatabase()
    try:
        ins = 'insert into club(club_id, name, member_count, type, master_id, time, intro) value (UUID_TO_BIN(UUID()), %s, 0, %s, %s, CURRENT_TIMESTAMP, %s);'
        cursor.execute(ins, [name, typeNum, masterId, intro])
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
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
    finally:
        closeDatabase(connect, cursor)
    return result


def updateUserClubLabel(userId: str, clubId: str, label: str):
    connect, cursor = connectDatabase()
    result = ''
    try:
        ins = 'update user_club set label = %s where user_id = %s and club_id = %s;'
        cursor.execute(ins, [label, userId, clubId])
        result = cursor.fetchall()
    except Exception as e:
        print(e)
        connect.rollback()
    finally:
        closeDatabase(connect, cursor)
    return result


# createUser('a', 'b', 'c', 'd')
# createUser('aa', 'bb', 'cc', 'dd')

# conn, cursor = connectDatabase()
# x = 0
# res = cursor.callproc('getUser', args=('u_b', x))
# x = cursor.fetchall()
# print(x)


# initDatabase()
