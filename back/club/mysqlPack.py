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


def getFriendIds(userId: str):
    connect, cursor = connectDatabase()
    try:
        ins = 'select friend_id from follow where follower_id = %s;'
        cursor.execute(ins, [userId])
        result = cursor.fetchall()
    except Exception as e:
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


# club
def createClub(name: str, clubType: str, masterId: str, intro: str, cover: str, welcome: str, welcomeImage: str):
    typeNum = clubTypeToNum[clubType]
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('createClub', [name, typeNum, masterId, intro, cover, welcome, welcomeImage])
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return


def handleCreateClub(clubId: int, op: int):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('handleCreateClub', [clubId, op, '社长'])
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


def getUnhandledClubs():
    connect, cursor = connectDatabase()
    try:
        ins = 'select * from club where status = 0'
        cursor.execute(ins, [])
        result = cursor.fetchall()
    except Exception as e:
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def getAllClubs():
    connect, cursor = connectDatabase()
    try:
        ins = 'select * from club where status = 2'
        cursor.execute(ins, [])
        result = cursor.fetchall()
    except Exception as e:
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def getUserClub(userId: str):
    connect, cursor = connectDatabase()
    try:
        ins = 'select club_id from user_club where user_id = %s'
        cursor.execute(ins, [userId])  # 子串匹配
        result = cursor.fetchall()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def findClub(keyWord: str):
    connect, cursor = connectDatabase()
    try:
        ins = 'select * from club where name like %s and status = 2'
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
        ins = 'select * from club where status = 2 and club_id in (select club_id from user_club where user_id = %s)'
        cursor.execute(ins, [userId])
        result = cursor.fetchall()
    except Exception as e:
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def getOneClub(clubId: int):
    connect, cursor = connectDatabase()
    try:
        ins = 'select * from club where club_id = %s'
        cursor.execute(ins, [clubId])
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


def getClubMembers(clubId: int):
    connect, cursor = connectDatabase()
    try:
        ins = 'select user.*, label from user, user_club where user.user_id = user_club.user_id and club_id = %s'
        cursor.execute(ins, [clubId])
        result = cursor.fetchall()
    except Exception as e:
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def getClubEvents(clubId: int):
    connect, cursor = connectDatabase()
    try:
        ins = 'select event.*, club.cover, club.name, user.real_name from event, club, user where event.club_id = %s and event.status = 2 and club.club_id = event.club_id and user.user_id = event.user_id'
        cursor.execute(ins, [clubId])
        result = cursor.fetchall()
    except Exception as e:
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def getClubNotices(clubId: int):
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


def getClubRequests(clubId: int):
    connect, cursor = connectDatabase()
    try:
        # TODO 交申请时覆盖同一个社团前一次申请, 此处默认user_id, club_id也为joining_club候选码
        ins = 'select * from user, joining_club where user_id in (select applicant_id from joining_club where (club_id = %s and status = 0)) and user_id = applicant_id'
        cursor.execute(ins, [clubId])
        result = cursor.fetchall()
    except Exception as e:
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def updateUserClubLabel(userId: str, clubId: int, label: str):
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


def handleJoiningClub(op: int, formId: int):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('handleJoiningClub', (op, formId, '社员'))
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


def joinClub(userId: str, clubId: int):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('joinClub', (userId, clubId))
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


def joinClubDirect(userId: str, clubId: int):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('joinClubDirect', (userId, clubId, '社员'))
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


def quitClub(userId: str, clubId: int):
    connect, cursor = connectDatabase()
    try:
        cursor.execute('select master_id, name from club where club_id = %s', clubId)
        clubInfo = cursor.fetchall()
        masterId = clubInfo[0][0]
        clubName = clubInfo[0][1]
        cursor.callproc('quitClub', (userId, masterId, clubId, clubName))
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


def rateClubStar(clubId: int, star: int):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('rateClubStar', [clubId, star])
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


def modifyClubInfo(clubId: int, name: str, clubType: str, clubIntro: str, clubCover: str, welcome: str,
                   welcomeImage: str):
    connect, cursor = connectDatabase()
    try:
        typeNum = clubTypeToNum[clubType]
        cursor.callproc('modifyClubInfo', [clubId, name, typeNum, clubIntro, clubCover, welcome, welcomeImage])
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


# event
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


def handleCreateEvent(eventId: int, op: int):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('handleCreateEvent', [eventId, op])
        result = cursor.fetchall()
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def getUnhandledEvents():
    connect, cursor = connectDatabase()
    try:
        ins = 'select event.*, club.cover, club.name, user.real_name from event, club, user where event.status = 0 and event.club_id = club.club_id and event.user_id = user.user_id'
        cursor.execute(ins, [])
        result = cursor.fetchall()
    except Exception as e:
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def participateEvent(userId: str, eventId: int):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('participateEvent', [userId, eventId])
        result = cursor.fetchall()
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def likeEvent(userId: str, eventId: int, op: int):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('likeEvent', [userId, eventId, op])
        result = cursor.fetchall()
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def getUserEventAction(userId: str):
    connect, cursor = connectDatabase()
    try:
        ins = 'select event_id, action from user_event_like where user_id = %s'
        cursor.execute(ins, [userId])
        result = cursor.fetchall()
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def getUserEventParticipate(userId: str):
    connect, cursor = connectDatabase()
    try:
        ins = 'select event_id from user_event_participate where user_id = %s'
        cursor.execute(ins, [userId])
        result = cursor.fetchall()
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


# message
def deleteMessage(messageId: str):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('deleteMessage', (messageId,))
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


def deleteAllMessages(userId: str):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('deleteAllMessages', (userId,))
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


def getMessages(userId: str):
    connect, cursor = connectDatabase()
    try:
        cursor.execute('select * from message where receiver_id = %s', [userId])
        result = cursor.fetchall()
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


# post reply
def getClubPosts(clubId: int):
    connect, cursor = connectDatabase()
    try:
        ins = 'select post.*, user.avatar, user.real_name from post, user where club_id = %s and post.user_id = user.user_id'
        cursor.execute(ins, [clubId])
        result = cursor.fetchall()
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def publishPost(userId: str, clubId: int, title: str, content: str):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('publishPost', [userId, clubId, title, content])
        result = cursor.fetchall()
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def likePost(userId: str, postId: int, op: int):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('likePost', [userId, postId, op])
        result = cursor.fetchall()
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def likeReply(userId: str, replyId: int, op: int):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('likeReply', [userId, replyId, op])
        result = cursor.fetchall()
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def deletePost(postId: str):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('deletePost', [postId])
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


def deleteReply(replyId: str):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('deleteReply', [replyId])
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


def replyPost(userId: str, postId: int, content: str):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('replyPost', [userId, postId, content])
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


def getPostReplies(postId: str):
    connect, cursor = connectDatabase()
    try:
        ins = 'select reply.*, avatar, real_name from reply, user where post_id = %s and reply.user_id = user.user_id'
        cursor.execute(ins, [postId])
        result = cursor.fetchall()
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def getOnePost(postId: str):
    connect, cursor = connectDatabase()
    try:
        ins = 'select post.*, user.avatar, user.real_name from post, user where post.user_id = user.user_id and post_id = %s'
        cursor.execute(ins, [postId])
        result = cursor.fetchall()
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def getUserPostAction(userId: str):
    connect, cursor = connectDatabase()
    try:
        ins = 'select post_id, action from user_post where user_id = %s'
        cursor.execute(ins, [userId])
        result = cursor.fetchall()
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


def getUserReplyAction(userId: str):
    connect, cursor = connectDatabase()
    try:
        ins = 'select reply_id, action from user_reply where user_id = %s'
        cursor.execute(ins, [userId])
        result = cursor.fetchall()
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)
    return result


# others
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


def publishNotice(noticeTitle: str, noticeContent: str, userId: str, clubId: int, noticeTop: int):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('publishNotice', (noticeTitle, noticeContent, userId, clubId, noticeTop))
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
        raise e
    finally:
        closeDatabase(connect, cursor)


def deleteNotice(noticeId: str):
    connect, cursor = connectDatabase()
    try:
        cursor.callproc('deleteNotice', [noticeId])
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
