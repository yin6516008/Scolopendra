#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
from datetime import datetime
from pymongo import MongoClient

mongo_server = "localhost"
mongo_port = 27017

class Base_Class(object):
    def __init__(self):
        self.mongo_server = 'localhost'
        self.mongo_port = 27017
        self.client = MongoClient(mongo_server,mongo_port)
        self.Scolopendra_db = self.client.Scolopendra_db
        self.date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    def log_write(self,log_content,type):
        log_info = {
            'type':type,
            'date':self.date,
            'log':log_content
        }
        self.Scolopendra_db.log.insert(log_info)

    def log_read(self,*args):
        if args == ():
            log = list(self.Scolopendra_db.log.find())
            return log

