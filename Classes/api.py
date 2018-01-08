#!/usr/bin/python
# -*- coding: UTF-8 -*-
import salt.client
import sys,os
reload(sys)
sys.setdefaultencoding('utf8')
from salt import key,config,client
from Classes.Base_module import Base_Class



master_opts = config.client_config('/etc/salt/master')
salt_root_path = master_opts['file_roots']['base'][0]




class salt_api(Base_Class):
    '''
    salt-api类
    '''
    def __init__(self):
        Base_Class.__init__(self)
        self.__opt = config.master_config('/etc/salt/master')
        self.__key = key.get_key(self.__opt)
        self.__Client = salt.client.LocalClient()
        self.timeout = 60

    def cmd(self,group_name,mudules,args):
        '''
        命令执行方法
        :param hosts:
        :param mudules:
        :param args:
        :return:
        '''
        if group_name == '*':
            hosts = group_name
        else:
            hosts = group_gl_obj.show_hosts(group_name)
        print(6,hosts,mudules,args)
        if type(hosts) ==  list :
            if len(hosts) > 100:
                host_number = len(hosts)
                self.timeout += int(host_number / 50)
            data = self.__Client.cmd(hosts, mudules, args,expr_form='list',timeout=self.timeout)
            self.log_write(log_content="对%s执行了%s命令,参数为%s" % (group_name,mudules,args),type='action')
        else:
            all_host = self.__key.list_keys()['minions']
            self.timeout += int(len(all_host) / 50)
            data = self.__Client.cmd(hosts,mudules,args,timeout=self.timeout)
            self.log_write(log_content="对%s执行了%s命令,参数为%s" % (group_name,mudules,args),type='action')
        return data

