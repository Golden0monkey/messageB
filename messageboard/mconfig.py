#coding:utf-8
#!usr/bin/env python3.6
'''
author:shadow
date:2019.3.10
配置文件
'''


import os,sys
from messageboard import app

#配置数据库地址
dev_db = "sqlite:////"+os.path.join(os.path.dirname(app.root_path),'data.db')
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)

