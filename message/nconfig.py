#coding:utf-8
#!usr/bin/env python3.6
'''
author:shadow
date:2019.3.13
配置
'''

import os,sys
from message import app


SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')

#sql配置，sqlite的数据库URL在linux或者mac系统的斜线数量是4，在window下是3个
# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')
print(dev_db)
#配置变量决定是否追踪对象的的修改，关闭警告
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)