#!/usr/bin/python
# -*- coding: UTF-8 -*-
import salt.client
import sys,os
reload(sys)
sys.setdefaultencoding('utf8')
from salt import key,config,client


master_opts = config.client_config('/etc/salt/master')
salt_root_path = master_opts['file_roots']['base'][0]




class salt_api(object):
    def __init__(self):
        self.__opt = config.master_config('/etc/salt/master')
        self.__key = key.get_key(self.__opt)
        self.__Client = salt.client.LocalClient()


    def cmd(self,hosts,mudules,args):
        timeout = 60
        print(6,hosts,mudules,args)
        if type(hosts) ==  list :
            if len(hosts) > 100:
                host_number = len(hosts)
                timeout += int(host_number / 50)
            data = self.__Client.cmd(hosts, mudules, args,expr_form='list',timeout=timeout)
        else:
            all_host = self.__key.list_keys()['minions']
            timeout += int(len(all_host) / 50)
            data = self.__Client.cmd(hosts,mudules,args,timeout=timeout)
        return data

