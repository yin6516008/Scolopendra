#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Classes.dbManage import *
from pymongo import MongoClient

mongo_server = 'localhost'
mongo_port = 27017
client = MongoClient(mongo_server,mongo_port)
Scolopendra_db = client.Scolopendra_db
class group_gl(object):
    def __init__(self):
        self.__Scolopendra_db = Scolopendra_db
        self.__group_collection = Scolopendra_db.group

    def add_group(self,group):
        group_name = group['group_name']
        group_obj = self.__group_collection.find({'group_name':group_name}).count()
        print(group_obj)
        print(type(group_obj))
        if group_obj != 0:
            return 'Group Exist'
        else:
            self.__group_collection.insert_one(group)
            return 'OK'


    def show_all_group(self):
        all_group = []
        for item in self.__group_collection.find():
            all_group.append(item)
        return all_group

    def del_group(self,group_name):
        self.__group_collection.remove({"group_name":group_name})
        return 'OK'

    def show_hosts(self,group_name):
        hosts = self.__group_collection.find_one({"group_name":group_name})
        return hosts['group_hosts']