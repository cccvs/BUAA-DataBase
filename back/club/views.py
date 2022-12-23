# coding=utf-8
from datetime import datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from club import mysqlPack
import jwt
import hashlib

jwtKey = '123456'
jwtFailedDict = {'code': 666, 'message': 'jwt verified error'}
userField = ['user_id', 'password', 'avatar', 'time', 'real_name', 'sex', 'institute', 'phone', 'email', 'level',
             'following', 'followers']
clubField = ['club_id', 'name', 'type', 'star', 'member_count', 'time', 'intro', 'master_id', 'cover',
             'status', 'welcome', 'welcome_image']
noticeField = ['notice_id', 'title', 'content', 'user_id', 'club_id', 'top']
eventField = ['event_id', 'club_id', 'user_id', 'title', 'cover', 'content', 'time', 'apply_time', 'expired_time',
              'begin_time', 'end_time', 'member_count', 'member_limit', 'status', 'like', 'dislike']
replyField = ['reply_id', 'post_id', 'user_id', 'time', 'content', 'like', 'dislike']
postField = ['post_id', 'club_id', 'user_id', 'time', 'title', 'content', 'like', 'dislike']
joiningClubField = ['form_id', 'applicant_id', 'club_id', 'status', 'time']
messageField = ['message_id', 'receiver_id', 'time', 'content']



def hashCode(s, salt='club_system'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def checkJwt(jwtDict: dict) -> bool:
    codeStr: str = jwtDict['code']
    userId = jwtDict['user_id']
    time = jwtDict['time']
    newCodeStr: str = jwt.encode(payload={'user_id': userId, 'time': time}, algorithm='HS256', key=jwtKey,
                                 headers={'typ': 'JWT', 'alg': 'HS256'}).decode()
    return codeStr.__eq__(newCodeStr)


# user
@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        # vars
        userId = request.POST.get('user_id')
        password = request.POST.get('password')
        curTime = str(datetime.now())
        code = jwt.encode(payload={'user_id': userId, 'time': curTime}, algorithm='HS256', key=jwtKey,
                          headers={'typ': 'JWT', 'alg': 'HS256'})
        jwtDict = {'code': code.decode(), 'user_id': userId, 'time': curTime}
        # logics
        result = mysqlPack.getUser(userId)
        print(result)
        if result:
            if result[0][1] != hashCode(password):
                return JsonResponse({'code': 3, 'message': 'wrong password'})
            else:
                return JsonResponse(
                    {'code': 0, 'message': 'login succeess', 'jwt': jwtDict})
        else:
            return JsonResponse({'code': 2, 'message': 'user not found'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def registerUser(request):
    if request.method == 'POST':
        # vars
        userId = request.POST.get('user_id')
        name = request.POST.get('name')
        password = request.POST.get('password')
        sex = request.POST.get('sex')
        institute = request.POST.get('institute')
        email = request.POST.get('email')
        # verifyCode = request.POST.get('verify_code')
        # logics
        try:
            mysqlPack.createUser(userId, hashCode(password), name, sex, institute, email)
            return JsonResponse({'code': 0, 'message': 'create user successfully!'})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 4, 'message': 'duplicated user name'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def updateUserInformation(request):
    if request.method == 'POST':
        userDict = request.POST
        userId = userDict['user_id']
        realName = userDict['real_name']
        sex = userDict['sex']
        institute = userDict['institute']
        phone = userDict['phone']
        email = userDict['email']
        try:
            mysqlPack.updateUserField(userId, realName, sex, institute, phone, email)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 14, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def getUserInformation(request):
    if request.method == 'POST':
        jwtDict = {'code': request.POST.get('jwt[code]'), 'user_id': request.POST.get('jwt[user_id]'),
                   'time': request.POST.get('jwt[time]')}
        if not checkJwt(jwtDict):
            return JsonResponse(jwtFailedDict)
        userId = jwtDict['user_id']
        try:
            userResultDict = dict()
            result = mysqlPack.getUser(userId)
            for num, field in enumerate(userField):
                userResultDict[field] = result[0][num]
            return JsonResponse({'code': 0, 'message': '', 'user': userResultDict})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 15, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def modifyPassword(request):
    if request.method == 'POST':
        jwtDict = {'code': request.POST.get('jwt[code]'), 'user_id': request.POST.get('jwt[user_id]'),
                   'time': request.POST.get('jwt[time]')}
        if not checkJwt(jwtDict):
            return JsonResponse(jwtFailedDict)
        oldPassword = request.POST.get('old_password')
        newPassword = request.POST.get('new_password')
        userId = jwtDict['user_id']
        # check password
        userResult = mysqlPack.getUser(userId)
        if userResult:
            if userResult[0][1] != hashCode(oldPassword):
                return JsonResponse({'code': 3, 'message': 'wrong password'})
        else:
            return JsonResponse({'code': 2, 'message': 'user not found'})
        # change password
        try:
            mysqlPack.updateUserPassword(userId, hashCode(newPassword))
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 22, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def updateAvatar(request):
    if request.method == 'POST':
        userId = request.POST.get('user_id')
        avatar = request.POST.get('avatar')
        # end of file template
        try:
            mysqlPack.updateUserAvatar(userId, avatar)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 29, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


# club
@csrf_exempt
def createClub(request):
    if request.method == 'POST':
        # vars
        name = request.POST.get('name')
        clubType = request.POST.get('type')
        intro = request.POST.get('intro')
        cover = request.POST.get('image_url')
        welcome = request.POST.get('welcome')
        welcomeImage = request.POST.get('welcome_image')
        jwtDict = {'code': request.POST.get('jwt[code]'), 'user_id': request.POST.get('jwt[user_id]'),
                   'time': request.POST.get('jwt[time]')}
        masterId = jwtDict['user_id']
        if not checkJwt(jwtDict):
            return JsonResponse(jwtFailedDict)
        try:
            mysqlPack.createClub(name, clubType, masterId, intro, cover, welcome, welcomeImage)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 7, 'message': 'error in createClub'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def handleCreateClub(request):
    if request.method == 'POST':
        # vars
        clubId = request.POST.get('club_id')
        op = request.POST.get('op')
        try:
            mysqlPack.handleCreateClub(clubId, op)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 31, 'message': 'error in createClub'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def getUnhandledClubs(request):
    if request.method == 'POST':
        try:
            result = mysqlPack.getUnhandledClubs()
            resultList = []
            for data in result:
                resultItem = dict()
                for num, field in enumerate(clubField):
                    resultItem[field] = data[num]
                resultList.append(resultItem)
            return JsonResponse({'code': 0, 'message': '', 'club_list': resultList})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 41, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def getAllClubs(request):
    if request.method == 'POST':
        try:
            result = mysqlPack.getAllClubs()
            resultList = []
            for data in result:
                resultItem = dict()
                for num, field in enumerate(clubField):
                    resultItem[field] = data[num]
                resultList.append(resultItem)
            return JsonResponse({'code': 0, 'message': '', 'club_list': resultList})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 45, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def findClub(request):
    retDict = dict()
    if request.method == 'POST':
        keyWord = request.POST.get('key_word')
        # 获取已加入社团的id列表
        userId = request.POST.get('user_id')
        clubIdRes = mysqlPack.getUserClub(userId)
        clubIdSet = {x[0] for x in clubIdRes}
        try:
            result = mysqlPack.findClub(keyWord)
            resultList = []
            for data in result:
                resultItem = dict()
                for num, field in enumerate(clubField):
                    resultItem[field] = data[num]
                # 如果已加入社团，则不显示
                if resultItem['club_id'] not in clubIdSet:
                    resultList.append(resultItem)
            retDict['club_list'] = resultList
            retDict['code'] = 0
            retDict['message'] = ''
            return JsonResponse(retDict)
        except Exception as e:
            print(e)
            return JsonResponse({'code': 6, 'message': 'error in finding club'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def changePosition(request):
    if request.method == 'POST':
        userId = request.POST.get('user_id')
        clubId = request.POST.get('club_id')
        label = request.POST.get('label')
        try:
            mysqlPack.updateUserClubLabel(userId, clubId, label)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 9, 'message': 'error in changing position'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def getClubList(request):
    if request.method == 'POST':
        jwtDict = {'code': request.POST.get('jwt[code]'), 'user_id': request.POST.get('jwt[user_id]'),
                   'time': request.POST.get('jwt[time]')}
        if not checkJwt(jwtDict):
            return JsonResponse(jwtFailedDict)
        userId = jwtDict['user_id']
        try:
            result = mysqlPack.getClubList(userId)
            resultList = []
            for data in result:
                resultItem = dict()
                for num, field in enumerate(clubField):
                    resultItem[field] = data[num]
                resultList.append(resultItem)
            return JsonResponse({'code': 0, 'message': '', 'club_list': resultList})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 10, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def getMasterClubList(request):
    if request.method == 'POST':
        jwtDict = {'code': request.POST.get('jwt[code]'), 'user_id': request.POST.get('jwt[user_id]'),
                   'time': request.POST.get('jwt[time]')}
        if not checkJwt(jwtDict):
            return JsonResponse(jwtFailedDict)
        userId = jwtDict['user_id']
        try:
            result = mysqlPack.getMasterClubList(userId)
            resultList = []
            for data in result:
                resultItem = dict()
                for num, field in enumerate(clubField):
                    resultItem[field] = data[num]
                resultList.append(resultItem)
            return JsonResponse({'code': 0, 'message': '', 'club_list': resultList})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 23, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def getClubMembers(request):
    if request.method == 'POST':
        clubId = request.POST.get('club_id')
        userId = request.POST.get('user_id')
        try:
            # user's friend
            friendIdRes = mysqlPack.getFriendIds(userId)
            friendIdSet = {x[0] for x in friendIdRes}
            # club members
            result = mysqlPack.getClubMembers(clubId)
            resultList = []
            for data in result:
                resultItem = dict()
                for num, field in enumerate(userField + ['label']):
                    resultItem[field] = data[num]
                # 社长是否关注了该成员
                resultItem['is_follow'] = 1 if friendIdSet.__contains__(resultItem['user_id']) else 0
                resultList.append(resultItem)
            return JsonResponse({'code': 0, 'message': '', 'member_list': resultList})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 11, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def getClubEvents(request):
    if request.method == 'POST':
        clubId = request.POST.get('club_id')
        userId = request.POST.get('user_id')
        try:
            eventActionList = mysqlPack.getUserEventAction(userId)
            likeSet = {x[0] for x in eventActionList if x[1] == 0}
            dislikeSet = {x[0] for x in eventActionList if x[1] == 1}
            result = mysqlPack.getClubEvents(clubId)
            resultList = []
            for data in result:
                resultItem = dict()
                for num, field in enumerate(eventField + ['club_cover', 'club_name', 'user_real_name']):
                    resultItem[field] = data[num]
                # extra field, 0:点赞, 1:点踩, 2:无操作
                resultItem['show'] = False
                if resultItem['event_id'] in likeSet:
                    resultItem['op'] = 0
                elif resultItem['event_id'] in dislikeSet:
                    resultItem['op'] = 1
                else:
                    resultItem['op'] = 2
                resultList.append(resultItem)
            return JsonResponse({'code': 0, 'message': '', 'event_list': resultList})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 12, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def getClubNotices(request):
    if request.method == 'POST':
        clubId = request.POST.get('club_id')
        try:
            result = mysqlPack.getClubNotices(clubId)
            resultList = []
            for data in result:
                resultItem = dict()
                for num, field in enumerate(noticeField):
                    resultItem[field] = data[num]
                resultList.append(resultItem)
            return JsonResponse({'code': 0, 'message': '', 'notice_list': resultList})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 13, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def getClubRequests(request):
    if request.method == 'POST':
        clubId = request.POST.get('club_id')
        try:
            result = mysqlPack.getClubRequests(clubId)
            resultList = []
            for data in result:
                resultItem = dict()
                for num, field in enumerate(userField + joiningClubField):
                    resultItem[field] = data[num]
                resultList.append(resultItem)
            return JsonResponse({'code': 0, 'message': '', 'requests': resultList})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 16, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def handleJoiningClub(request):
    if request.method == 'POST':
        op = request.POST.get('op')
        formId = request.POST.get('request_id')
        try:
            mysqlPack.handleJoiningClub(op, formId)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 17, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def joinClub(request):
    if request.method == 'POST':
        print(request.POST)
        userId = request.POST.get('user_id')
        clubId = request.POST.get('club_id')
        try:
            mysqlPack.joinClub(userId, clubId)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 24, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def quitClub(request):
    if request.method == 'POST':
        userId = request.POST.get('user_id')
        clubId = request.POST.get('club_id')
        try:
            mysqlPack.quitClub(userId, clubId)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 25, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def rateClubStar(request):
    if request.method == 'POST':
        clubId = request.POST.get('club_id')
        star = request.POST.get('star')
        try:
            mysqlPack.rateClubStar(clubId, star)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 43, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def modifyClubInfo(request):
    if request.method == 'POST':
        clubId = request.POST.get('club_id')
        name = request.POST.get('name')
        clubType = request.POST.get('type')
        intro = request.POST.get('intro')
        cover = request.POST.get('cover')
        welcome = request.POST.get('welcome')
        welcomeImage = request.POST.get('welcome_image')
        try:
            mysqlPack.modifyClubInfo(clubId, name, clubType, intro, cover, welcome, welcomeImage)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 44, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


# message
@csrf_exempt
def deleteMessage(request):
    if request.method == 'POST':
        messageId = request.POST.get('message_id')
        try:
            mysqlPack.deleteMessage(messageId)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 27, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def deleteAllMessages(request):
    if request.method == 'POST':
        userId = request.POST.get('user_id')
        try:
            mysqlPack.deleteAllMessages(userId)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 28, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def getMessages(request):
    if request.method == 'POST':
        userId = request.POST.get('user_id')
        try:
            result = mysqlPack.getMessages(userId)
            resultList = []
            for data in result:
                resultItem = dict()
                for num, field in enumerate(messageField):
                    resultItem[field] = data[num]
                resultList.append(resultItem)
            return JsonResponse({'code': 0, 'message': '', 'messages': resultList})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 30, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


# event
@csrf_exempt
def createEvent(request):
    if request.method == 'POST':
        clubId = request.POST.get('club_id')
        userId = request.POST.get('user_id')
        title = request.POST.get('title')
        cover = request.POST.get('cover')
        content = request.POST.get('content')
        applyTime = request.POST.get('apply_time')
        expiredTime = request.POST.get('expired_time')
        beginTime = request.POST.get('begin_time')
        endTime = request.POST.get('end_time')
        limit = request.POST.get('limit')
        try:
            mysqlPack.createEvent(clubId, userId, title, cover, content, applyTime, expiredTime, beginTime, endTime,
                                  limit)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 18, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def handleCreateEvent(request):
    if request.method == 'POST':
        eventId = request.POST.get('event_id')
        op = request.POST.get('op')
        try:
            mysqlPack.handleCreateEvent(eventId, op)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 32, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def getUnhandledEvents(request):
    if request.method == 'POST':
        try:
            result = mysqlPack.getUnhandledEvents()
            resultList = []
            for data in result:
                resultItem = dict()
                for num, field in enumerate(eventField):
                    resultItem[field] = data[num]
                resultList.append(resultItem)
            return JsonResponse({'code': 0, 'message': '', 'event_list': resultList})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 42, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def participateEvent(request):
    if request.method == 'POST':
        eventId = request.POST.get('event_id')
        userId = request.POST.get('user_id')
        try:
            mysqlPack.participateEvent(userId, eventId)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 33, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def likeEvent(request):
    if request.method == 'POST':
        userId = request.POST.get('user_id')
        eventId = request.POST.get('event_id')
        op = request.POST.get('op')
        try:
            mysqlPack.likeEvent(userId, eventId, op)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 34, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
# post/reply
def getClubPosts(request):
    if request.method == 'POST':
        clubId = request.POST.get('club_id')
        userId = request.POST.get('user_id')
        postActionList = mysqlPack.getUserPostAction(userId)
        likeSet = {x[0] for x in postActionList if x[1] == 0}
        dislikeSet = {x[0] for x in postActionList if x[1] == 1}
        try:
            result = mysqlPack.getClubPosts(clubId)
            resultList = []
            for data in result:
                resultItem = dict()
                for num, field in enumerate(postField + ['user_avatar', 'user_name']):
                    resultItem[field] = data[num]
                if resultItem['post_id'] in likeSet:
                    resultItem['op'] = 0
                elif resultItem['post_id'] in dislikeSet:
                    resultItem['op'] = 1
                else:
                    resultItem['op'] = 2
                resultList.append(resultItem)
            return JsonResponse({'code': 0, 'message': '', 'post_list': resultList})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 35, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def publishPost(request):
    if request.method == 'POST':
        userId = request.POST.get('user_id')
        clubId = request.POST.get('club_id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        try:
            mysqlPack.publishPost(userId, clubId, title, content)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 36, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def likePost(request):
    if request.method == 'POST':
        userId = request.POST.get('user_id')
        postId = request.POST.get('post_id')
        op = request.POST.get('op')
        try:
            mysqlPack.likePost(userId, postId, op)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 37, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def likeReply(request):
    if request.method == 'POST':
        userId = request.POST.get('user_id')
        replyId = request.POST.get('reply_id')
        op = request.POST.get('op')
        try:
            mysqlPack.likeReply(userId, replyId, op)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 49, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def deletePost(request):
    if request.method == 'POST':
        postId = request.POST.get('post_id')
        try:
            mysqlPack.deletePost(postId)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 38, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def deleteReply(request):
    if request.method == 'POST':
        replyId = request.POST.get('reply_id')
        try:
            mysqlPack.deleteReply(replyId)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 40, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def replyPost(request):
    if request.method == 'POST':
        userId = request.POST.get('user_id')
        postId = request.POST.get('post_id')
        content = request.POST.get('content')
        try:
            mysqlPack.replyPost(userId, postId, content)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 46, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def getPostReplies(request):
    if request.method == 'POST':
        postId = request.POST.get('post_id')
        userId = request.POST.get('user_id')
        replyActionList = mysqlPack.getUserReplyAction(userId)
        likeSet = {x[0] for x in replyActionList if x[1] == 0}
        dislikeSet = {x[0] for x in replyActionList if x[1] == 1}
        try:
            result = mysqlPack.getPostReplies(postId)
            resultList = []
            for data in result:
                resultItem = dict()
                for num, field in enumerate(replyField + ['user_avatar', 'user_name']):
                    resultItem[field] = data[num]
                resultList.append(resultItem)
                if resultItem['reply_id'] in likeSet:
                    resultItem['op'] = 0
                elif resultItem['reply_id'] in dislikeSet:
                    resultItem['op'] = 1
                else:
                    resultItem['op'] = 2
            return JsonResponse({'code': 0, 'message': '', 'reply_list': resultList})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 47, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def getOnePost(request):
    if request.method == 'POST':
        postId = request.POST.get('post_id')
        userId = request.POST.get('user_id')
        postActionList = mysqlPack.getUserPostAction(userId)
        likeSet = {x[0] for x in postActionList if x[1] == 0}
        dislikeSet = {x[0] for x in postActionList if x[1] == 1}
        try:
            result = mysqlPack.getOnePost(postId)[0]
            resultItem = dict()
            for num, field in enumerate(postField + ['user_avatar', 'user_name']):
                resultItem[field] = result[num]
            if resultItem['post_id'] in likeSet:
                resultItem['op'] = 0
            elif resultItem['post_id'] in dislikeSet:
                resultItem['op'] = 1
            else:
                resultItem['op'] = 2
            return JsonResponse({'code': 0, 'message': '', 'post': resultItem})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 48, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


# others
@csrf_exempt
def handleFollowing(request):
    if request.method == 'POST':
        followerId = request.POST.get('follower_id')
        friendId = request.POST.get('friend_id')
        try:
            mysqlPack.handleFollowing(followerId, friendId)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 19, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def handleUnfollowing(request):
    if request.method == 'POST':
        followerId = request.POST.get('follower_id')
        friendId = request.POST.get('friend_id')
        try:
            mysqlPack.handleUnfollowing(followerId, friendId)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 20, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def publishNotice(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        userId = request.POST.get('user_id')
        clubId = request.POST.get('club_id')
        top = request.POST.get('top')
        try:
            mysqlPack.publishNotice(title, content, userId, clubId, top)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 25, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def deleteNotice(request):
    if request.method == 'POST':
        noticeId = request.POST.get('notice_id')
        try:
            mysqlPack.deleteNotice(noticeId)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 39, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def addComment(request):
    if request.method == 'POST':
        userId = request.POST.get('user_id')
        eventId = request.POST.get('event_id')
        content = request.POST.get('content')
        try:
            mysqlPack.addComment(userId, eventId, content)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 26, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def joinClubBulk(request):
    length = request.POST.get('length')
    clubId = request.POST.get('club_id')
    userIdList = [request.POST.get("data[%d][item][user_id]" % i) for i in range(length)]
    if request.method == 'POST':
        try:
            for userId in userIdList:
                mysqlPack.joinClubDirect(userId, clubId)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 50, 'message': 'error'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})