#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pymongo import MongoClient

mongo_server = 'localhost'
mongo_port = 27017
client = MongoClient(mongo_server,mongo_port)
Scolopendra = client.Scolopendra
host_collection = Scolopendra.host_collection



