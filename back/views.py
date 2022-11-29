# coding=utf-8
from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse

from . import mysqlPack
import jwt
import hashlib


def hash_code(s, salt='log_reg_sys'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def loginUser(request):
    if request.method == 'POST':
        # vars
        userId = request.POST.get('user_id')
        password = request.POST.get('password')
        code = jwt.encode(payload={'user_id': 'a', 'time': str(datetime.now())}, algorithm='HS256', key='123456',
                          headers={"typ": "JWT", "alg": "HS256"})
        # logics
        result = mysqlPack.getUser(userId)
        if result:
            if result[0][1] != password:
                # code = 3
                # message = 'wrong password'
                # return render(request, 'api/login.html'， locals()), code.encode()
                return JsonResponse({'code': 3, 'message': 'wrong password'}), code.decode()
            else:
                return JsonResponse({'code': 0, 'message': 'login succeed'}), code.decode()
        else:
            return JsonResponse({'code': 2, 'message': 'user not found'}), code.decode()
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


def registerUser(request):
    if request.method == 'POST':
        # vars
        userId = request.POST.get('user_id')
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        verifyCode = request.POST.get('verify_code')
        # logics
        try:
            mysqlPack.createUser(userId, name, password, email)
            return JsonResponse({'code': 0, 'message': 'create user successfully!'})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 4, 'message': 'duplicated user name'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


def checkEmail(request):
    pass


def createClub(request):
    if request.method == 'POST':
        # vars
        name = request.POST.get('name')
        clubType = request.POST.get('type')
        masterId = request.POST.get('masterId')
        try:
            mysqlPack.createClub(name, clubType, masterId)
            return JsonResponse({'code': 0, 'message': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 7, 'message': 'error in createClub'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


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
                resultItem['name'] = data[1]
                resultItem['type'] = data[2]
                resultItem['star'] = data[3]
                resultItem['member_count'] = data[4]
                resultItem['score'] = data[5]
                resultItem['time'] = data[6]
                resultItem['intro'] = data[7]
                resultItem['cover'] = data[9]
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

# class TestRequest:
#     def __init__(self, str):
#         self.method = str
#
# testPost = TestRequest('POST')
# testGet = TestRequest('GET')
# loginUser(testPost)
