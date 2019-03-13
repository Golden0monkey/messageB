#coding:utf-8
#!usr/bin/env python3.6
'''
author:shadow
date:2019.3.13
初始化，
'''


from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask('message')
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config.from_pyfile('nconfig.py')#载入配置文件