#coding:utf-8
#!usr/bin/env python3.6
'''
author:shadow
date:2019.3.14
数据库模型
'''

from datetime import datetime

from message import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)


def initdb():
    db.create_all()
