#coding:utf-8
#!usr/bin/env python3.6
'''
author:shadow
date:2019.3.10
'''


from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask('messageboard')
app.config.from_pyfile('mconfig.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

#from messageboard import views, errors, commands
