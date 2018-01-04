#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys,os
from Classes.api import salt_root_path


class file_gl(object):
    '''
    文件管理类
    '''
    def __init__(self,relpath=''):
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
        if os.path.exists(self.__root_abspath):
            return 'Folder Exists'
        else:
            os.mkdir(self.__root_abspath)
            return 'OK'

    def del_file(self):
        if os.path.exists(self.__root_abspath):
            os.remove(self.__root_abspath)
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
                return 'OK'
            else:
                return 'File Exists'
        except Exception:
            return 'Failed'