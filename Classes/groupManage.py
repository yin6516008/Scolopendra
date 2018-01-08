#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Classes.Base_module import Base_Class

class group_gl(Base_Class):
    '''
    组管理类
    '''
    def __init__(self):
        Base_Class.__init__(self)

    def add_group(self,group):
        '''
        新建组,保存当mongoDB
        :param group:
        :return:
        '''
        group_name = group['group_name']
        group_obj = self.Scolopendra_db.group.find({'group_name':group_name}).count()
        if group_obj != 0:
            return 'Group Exist'
        else:
            self.Scolopendra_db.group.insert_one(group)
            self.log_write(log_content="新建组%s" % group_name,type='group')
            return 'OK'


    def show_all_group(self):
        '''
        返回所有组的信息
        :return:
        '''
        all_group = []
        for item in self.Scolopendra_db.group.find():
            all_group.append(item)
        return all_group

    def del_group(self,group_name):
        '''
        从mongoDB删除组
        :param group_name:
        :return:
        '''
        self.Scolopendra_db.group.remove({"group_name":group_name})
        self.log_write(log_content="删除组%s" % group_name,type='group')
        return 'OK'

    def show_hosts(self,group_name):
        '''
        返回一个组里的主机列表
        :param group_name:
        :return:
        '''
        hosts = self.Scolopendra_db.group.find_one({"group_name":group_name})
        return hosts['group_hosts']