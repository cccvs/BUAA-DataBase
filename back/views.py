# coding=utf-8
from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse
from .mysqlPack import *
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
        code = jwt.encode(payload={'user_id': 'a', 'time': str(datetime.now())}, algorithm='HS256', key='123456', headers={"typ": "JWT", "alg": "HS256"})
        # logics
        result = getUser(userId)
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
        if getUser(userId):
            return JsonResponse({'code': 4, 'message': 'duplicated user name'})
        else:
            createUser(userId, name, password, email)
            return JsonResponse({'code': 0, 'message': 'create user successfully!'})
    else:
        return JsonResponse({'code': 1, 'message': 'expect POST, get GET.'})


def checkEmail(request):
    pass

# class TestRequest:
#     def __init__(self, str):
#         self.method = str
#
# testPost = TestRequest('POST')
# testGet = TestRequest('GET')
# loginUser(testPost)
