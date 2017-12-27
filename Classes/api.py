#!/usr/bin/python
# -*- coding: UTF-8 -*-
import salt.client
import sys,os
reload(sys)
sys.setdefaultencoding('utf8')
import salt.config


master_opts = salt.config.client_config('/etc/salt/master')
salt_root_path = master_opts['file_roots']['base'][0]

# class salt_api(object):
#     def __init__(self,hosts,mudules,args):
#         self.__shell = 'powershell'
#         self.__api = salt.client.LocalClient()
salt_api = salt.client.LocalClient()
def cmd(hosts,mudules,args):
    print(6,hosts,mudules,args)
    data = salt_api.cmd(hosts,mudules,args)
    return data

