#!/usr/bin/python
# -*- coding: UTF-8 -*-
from salt import key,config
from Classes.Base_module import Base_Class

class host_gl(Base_Class):
    '''
    主机管理类
    '''
    def __init__(self):
        Base_Class.__init__(self)
        self.__opt = config.master_config('/etc/salt/master')
        self.__key = key.get_key(self.__opt)

    def show_host(self):
        '''
        以字典形式返回所有主机信息和主机分类后的信息
        :return:
        '''
        host_list = self.__key.list_keys()
        sort_host = {}
        for host in host_list['minions']:
            sort = host.split('-')[0]
            if sort in sort_host:
                sort_host[sort].append(host)
            else:
                sort_host[sort] = []
                sort_host[sort].append(host)
        host_list['sort_host'] = sort_host
        return host_list

    def accept_host(self,hosts):
        '''
        添加一个主机
        :param hosts:
        :return:
        '''
        self.__key.accept(hosts)
        self.log_write(log_content="添加主机%s" % hosts,type='host')
        return 'OK'

    def detele_host(self,hosts):
        '''
        删除一个主机
        :param hosts:
        :return:
        '''
        self.__key.delete_key(hosts)
        self.log_write(log_content="删除主机%s" % hosts,type='host')
        return 'OK'
