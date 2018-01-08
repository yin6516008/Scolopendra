#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys,os
from Classes.api import salt_root_path
from Classes.Base_module import Base_Class

class file_gl(Base_Class):
    '''
    文件管理类
    '''
    def __init__(self,relpath=''):
        Base_Class.__init__(self)
        self.__root_abspath = os.path.join(salt_root_path,relpath)
        self.__root_relpath = relpath
        self.__show_file = {'dir':[],'file':[],'relpath':self.__root_relpath.split('/')}

    def show_file(self):
        '''
        文件展示，返回用户点击的文件夹下的数据
        '''
        print(self.__root_abspath)
        file_list = os.listdir(self.__root_abspath)
        for i in [os.path.join(self.__root_abspath,file) for file in file_list ]:
            if os.path.isdir(i):
                self.__show_file['dir'].append(os.path.basename(i))
            if os.path.isfile(i):
                self.__show_file['file'].append(os.path.basename(i))
        return self.__show_file

    def new_dir(self):
        '''
        新建目录
        :return:
        '''
        if os.path.exists(self.__root_abspath):
            return 'Folder Exists'
        else:
            os.mkdir(self.__root_abspath)
            self.log_write(log_content="新建目录%s" % self.__root_abspath,type='file')
            return 'OK'

    def del_file(self):
        '''
        删除文件
        :return:
        '''
        if os.path.exists(self.__root_abspath):
            os.remove(self.__root_abspath)
            self.log_write(log_content="删除文件%s" % self.__root_abspath,type='file')
            return 'OK'
        else:
            return 'is not exists'

    def upload_file(self,file):
        '''
        保存用户上传的文件到用户当前所在的目录
        '''
        try:
            file_path = os.path.join(self.__root_abspath,file.name)
            if not os.path.isfile(file_path):
                with open(file_path,'wb') as f:
                    for item in file.chunks():
                        f.write(item)
                    f.close()
                    self.log_write(log_content="上传文件%s" % file_path,type='file')
                return 'OK'
            else:
                return 'File Exists'
        except Exception:
            return 'Failed'