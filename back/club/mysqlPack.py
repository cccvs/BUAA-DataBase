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


# user
def createUser(userId: str, password: str, name: str, sex: str, institute: str, email: str):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('createUser', args=(userId, password, name, sex, institute, email))
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return


def getUser(userId: str):
    # 需要userId和用户Id完全匹配
    connect, cursor = connectDatabase()
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


def updateUserField(userId: str, realName: str, userSex: str, userInstitute: str,
                    userPhone: str, userEmail: str, ):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('updateUserField',
                        (userId, realName, userSex, userInstitute, userPhone, userEmail))
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


def updateUserPassword(userId: str, userPassword: str):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('updatePassword', (userId, userPassword))
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


def updateUserAvatar(userId: str, userAvatar: str):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('updateAvatar', (userId, userAvatar))
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


def handleFollowing(followerId: str, friendId: str):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('handleFollowing', (followerId, friendId))
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


def handleUnfollowing(followerId: str, friendId: str):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('handleUnfollowing', (followerId, friendId))
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


# club
def createClub(name: str, clubType: str, masterId: str, intro: str):
    typeNum = clubTypeToNum[clubType]
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('createClub', (name, typeNum, masterId, intro))
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
    try:
        ins = 'select * from club where name like %s;'
        cursor.execute(ins, ['%' + keyWord + '%'])  # 子串匹配
        result = cursor.fetchall()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def getClubList(userId: str):
    connect, cursor = connectDatabase()
    try:
        ins = 'select * from club where club_id in (select club_id from user_club where user_id = %s)'
        cursor.execute(ins, [userId])
        result = cursor.fetchall()
    except Exception as e:
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def getMasterClubList(userId: str):
    connect, cursor = connectDatabase()
    try:
        ins = 'select * from club where club_id in (select club_id from user_club where user_id = %s and identity = 2)'
        cursor.execute(ins, [userId])
        result = cursor.fetchall()
    except Exception as e:
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def getClubMembers(clubId: str):
    connect, cursor = connectDatabase()
    try:
        ins = 'select * from user where user_id in (select user_id from user_club where club_id = %s)'
        cursor.execute(ins, [clubId])
        result = cursor.fetchall()
    except Exception as e:
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def getClubEvents(clubId: str):
    connect, cursor = connectDatabase()
    try:
        ins = 'select * from event where club_id = %s'
        cursor.execute(ins, [clubId])
        result = cursor.fetchall()
    except Exception as e:
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def getClubNotices(clubId: str):
    connect, cursor = connectDatabase()
    try:
        ins = 'select * from notice where club_id = %s'
        cursor.execute(ins, [clubId])
        result = cursor.fetchall()
    except Exception as e:
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def getClubRequests(clubId: str):
    connect, cursor = connectDatabase()
    try:
        ins = 'select * from user where user_id in (select applicant_id from joining_club where (club_id = %s and status = 0))'
        cursor.execute(ins, [clubId])
        result = cursor.fetchall()
    except Exception as e:
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def updateUserClubLabel(userId: str, clubId: str, label: str):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('updateUserClubLabel', (label, userId, clubId))
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


def handleJoiningClub(op: int, formId: str):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('handleJoiningClub', (op, formId))
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


# others
def createEvent(clubId: int, userId: str, eventTitle: str, eventCover: str, eventContent: str, applyTime: str,
                expiredTime: str, beginTime: str, endTime: str, memberLimit: int):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('createEvent',
                        (clubId, userId, eventTitle, eventCover, eventContent, applyTime,
                         expiredTime, beginTime, endTime, memberLimit))
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


def test():
    conn, cursor = connectDatabase()
    ins = 'insert into event(event_id, club_id, user_id, content, time, apply_time, expired_time, begin_time, end_time, member_count, member_limit) values (2001, 1001, %s, %s, %s, %s, %s, %s, %s, 1, 200)'
    cursor.execute(ins, ['20373743', 1002, '2022-12-11 20:12:43', '2022-12-11 20:12:43', '2022-12-11 20:12:43',
                         '2022-12-11 20:12:43', '2022-12-11 20:12:43'])
    conn.commit()
    closeDatabase(conn, cursor)

# test()
