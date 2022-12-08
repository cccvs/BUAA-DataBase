# coding=utf-8
from datetime import datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from club import mysqlPack
import jwt
import hashlib

userField = ['user_id', 'password', 'avatar', 'time', 'real_name', 'sex', 'institute', 'phone', 'email', 'level',
             'following', 'followers']
clubField = ['club_id', 'name', 'type', 'star', 'member_count', 'score', 'time', 'intro', 'master_id', 'cover']
eventField = ['event_id', 'club_id', 'user_id', 'intro', 'time', 'apply_time', 'expired_time', 'begin_time', 'end_time',
              'member_count', 'limit']


def hash_code(s, salt='log_reg_sys'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        # vars
        userId = request.POST.get('user_id')
        password = request.POST.get('password')
        code = jwt.encode(payload={'user_id': userId, 'time': str(datetime.now())}, algorithm='HS256', key='123456',
                          headers={'typ': 'JWT', 'alg': 'HS256'})
        data = jwt.decode(jwt=code.decode(), key='123456', algorithms='HS256')
        print(data)
        # logics
        print(request.POST)
        result = mysqlPack.getUser(userId)
        print(result)
        if result:
            if result[0][1] != password:
                # code = 3
                # message = 'wrong password'
                # return render(request, 'api/login.html'， locals()), code.encode()
                return JsonResponse({'code': 3, 'message': 'wrong password'})
            else:
                return JsonResponse({'code': 0, 'message': 'login succeess', 'jwt': code.decode()})
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
            mysqlPack.createUser(userId, password, name, sex, institute, email)
            return JsonResponse({'code': 0, 'message': 'create user successfully!'})
        except Exception as e:
            return JsonResponse({'code': 4, 'message': 'duplicated user name'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


@csrf_exempt
def createClub(request):
    if request.method == 'POST':
        # vars
        name = request.POST.get('name')
        clubType = request.POST.get('type')
        intro = request.POST.get('intro')
        codeStr = request.POST.get('code')
        masterId = jwt.decode(jwt=codeStr, key='123456', algorithms='HS256')['user_id']
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
            resultList = list()
            for data in result:
                resultItem = dict()
                for num, field in enumerate(userField):
                    resultItem[field] = data[num]
                resultList.append(resultItem)
            retDict['club_dist'] = resultList
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
# class TestRequest:
#     def __init__(self, str):
#         self.method = str
#
# testPost = TestRequest('POST')
# testGet = TestRequest('GET')
# loginUser(testPost)
