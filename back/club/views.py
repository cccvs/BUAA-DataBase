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
clubField = ['club_id', 'name', 'type', 'star', 'member_count', 'score', 'time', 'intro', 'master_id', 'cover']
eventField = ['event_id', 'club_id', 'user_id', 'title', 'cover', 'content', 'time', 'apply_time', 'expired_time',
              'begin_time', 'end_time', 'member_count', 'member_limit']
noticeField = ['notice_id', 'title', 'content', 'user_id', 'club_id', 'top']


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
        userDict = request.POST.get('user')
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
        jwtDict = request.POST.get('jwt')
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
        jwtDict = request.POST.get('jwt')
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


# club
@csrf_exempt
def createClub(request):
    if request.method == 'POST':
        # vars
        name = request.POST.get('name')
        clubType = request.POST.get('type')
        intro = request.POST.get('intro')
        jwtDict = request.POST.get('jwt')
        masterId = jwtDict['user_id']
        if not checkJwt(jwtDict):
            return JsonResponse(jwtFailedDict)
        try:
            mysqlPack.createClub(name, clubType, masterId, intro)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 7, 'message': 'error in createClub'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def findClub(request):
    retDict = dict()
    if request.method == 'POST':
        # vars
        keyWord = request.POST.get('key_word')
        try:
            result = mysqlPack.findClub(keyWord)
            resultList = []
            for data in result:
                resultItem = dict()
                for num, field in enumerate(clubField):
                    resultItem[field] = data[num]
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
        jwtDict = request.POST.get('jwt')
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
def getClubMembers(request):
    if request.method == 'POST':
        clubId = request.POST.get('club_id')
        try:
            result = mysqlPack.getClubMembers(clubId)
            resultList = []
            for data in result:
                resultItem = dict()
                for num, field in enumerate(userField):
                    resultItem[field] = data[num]
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
        try:
            result = mysqlPack.getClubEvents(clubId)
            resultList = []
            for data in result:
                resultItem = dict()
                for num, field in enumerate(eventField):
                    resultItem[field] = data[num]
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
            mysqlPack.getClubRequests(clubId)
            return JsonResponse({'code': 0, 'message': ''})
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


# others
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
