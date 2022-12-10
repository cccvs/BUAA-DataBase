# coding=utf-8
from club import mysqlPack
import os
mysqlPack.initDatabase()
os.system('python ./back/manage.py migrate')
