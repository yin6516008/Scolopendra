#!/usr/bin/python
# -*- coding: UTF-8 -*-
from salt import key,config

class host_gl(object):
    def __init__(self):
        self.__opt = config.master_config('/etc/salt/master')
        self.__key = key.get_key(self.__opt)

    def show_host(self,):
        host_list = self.__key.list_keys()
        return host_list

    def accept_host(self,hosts):
        self.__key.accept(hosts)
        return 'OK'

    def detele_host(self,hosts):
        self.__key.delete_key(hosts)
        return 'OK'
