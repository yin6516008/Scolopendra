#!/usr/bin/python
# -*- coding: UTF-8 -*-
import salt.client
import sys,os
reload(sys)
sys.setdefaultencoding('utf8')
import re
from salt import key,config,client
from Classes.Base_module import Base_Class
from pymongo.errors import InvalidDocument


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

    def grains(self,host):
        grains_info = self.__Client.cmd(host,'grains.items')
        if grains_info[host].has_key('osfullname'):
            host_info = {
                'host':grains_info[host]['host'],
                'id':grains_info[host]['id'],
                'cpu_model':grains_info[host]['cpu_model'],
                'num_cpus':grains_info[host]['num_cpus'],
                'cpuarch':grains_info[host]['cpuarch'],
                'osfullname':grains_info[host]['osfullname'],
                'mem_total':grains_info[host]['mem_total'],
                'ip4_interfaces':grains_info[host]['ip4_interfaces']
            }
        else:
            host_info = {
                'host':host,
                'error':'密钥验证失败或无法连接到minion'
            }
            return host_info
        try:
            self.Scolopendra_db.host_info.insert_one(host_info)
        except InvalidDocument:
            ip4_interfaces = host_info['ip4_interfaces']
            for k,v in ip4_interfaces.items():
                if re.match(".*\.",k) != None:
                    new_k = re.sub('\.','_',k)
                    print(new_k)
                    new_item = {new_k:ip4_interfaces.pop(k)}
                    ip4_interfaces.update(new_item)
                host_info['ip4_interfaces'] = ip4_interfaces
                print(host_info)
            self.Scolopendra_db.host_info.insert_one(host_info)
        return host_info

