#coding:utf-8
#!usr/bin/env python3.6
'''
author:shadow
date:2019.3.10
配置文件
'''


import os
from messageboard import app

#配置数据库地址
dev_db = "sqlite:///"+os.path.join(os.path.dirname(app.root_path),'data.db')

#配置密匙
SECRET_KEY = os.getenv('SECRET_KEY','secert string')

SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL',dev_db)