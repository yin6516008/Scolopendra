#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re


def correct_Data(data):
    '''
    转换中文、unicode等字符串
    :param data:
    :return:
    '''
    ascii_re = re.compile(r'\\w{3}\w.{3}')
    newline_re = re.compile(r'\r\n')
    for host,content in data.items():
        print(type(content))
        if type(content) is str:
            if re.search(ascii_re,repr(str(content))):
                data[host] = unicode(eval(repr(str(content))),'gbk')
            elif re.search(newline_re,str(content)):
                data[host] = re.sub(newline_re,'<br/>',str(content))
        if type(content) is dict:
            content_str = ''
            for k,v in content.items():
                if re.search(ascii_re,repr(str(v))):
                    content[k] = unicode(eval(repr(str(v))),'gbk')
                elif re.search(newline_re,str(v)):
                    content[k] = re.sub(newline_re,'<br/>',str(v))
            for k,v in content.items():
                element_str = k + ':' + str(v)
                content_str += element_str + '<br/>'
            data[host] = content_str
    return data

def join_path(path_list):
    '''
    将传过来的列表拼接成相对路径
    :param path_list: 需要拼接的路径
    :return:
    '''
    relpath = '/'.join(path_list)
    if relpath == '':
        return relpath
    else:
        relpath = re.sub('^/','',relpath)
    return relpath
