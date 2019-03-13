#coding:utf-8
#!usr/bin/env python3.6
'''
author:shadow
date:2019.3.13
设置
'''

import os,sys
from message import app


SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')