#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Create your views here.
import os
import json
import re
from django.shortcuts import render,HttpResponse,redirect,render_to_response
from Classes import api
from Classes.fileManage import file_gl
from Classes.General import correct_Data,join_path
from Classes.hostManage import host_gl
from Classes.groupManage import group_gl

def login(request):
    '''
    登陆函数
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        #获取用户提交的用户名和密码
        user = request.POST.get('user')
        password = request.POST.get('password')
        #用户名密码验证，并session赋值
        if user == 'root' and password == 'kemingjunde':
            print(user,password)
            request.session['user'] = user
            return render(request,'action.html')
        else:
            return HttpResponse('111')


def action(request):
    '''
    接收参数，并调用salt-api，得到结果返回数据
    :param request:
    :return:
    '''
    group_gl_obj = group_gl()
    if request.method == 'GET':
        #验证用户是否已经登陆，检查用户session
        if request.session.get('user',False):
            all_group = group_gl_obj.show_all_group()
            return render(request,'action.html',{'all_group':all_group})
        else:
            return redirect('/login/')

    if request.method == 'POST':
        group_name = request.POST.get('hosts')
        print(group_name)
        if group_name == '*':
            hosts = group_name
        else:
            hosts = group_gl_obj.show_hosts(group_name)
        print(1,hosts)
        #接收模块
        mudule_func = request.POST.get('module')
        print(2,mudule_func)
        #接收参数列表
        args = request.POST.get('args')
        args = json.loads(args)
        print(4,args)
        #调用api
        res = api.cmd(hosts,mudule_func,args)
        print(7,res)
        data = correct_Data(res)
        try:
            return HttpResponse(json.dumps(data),content_type='application/json')
        except UnicodeDecodeError:
            data = correct_Data(res)
            return HttpResponse(json.dumps(data),content_type='application/json')


def host(request):
    '''
    主机管理页的方法
    :param request:
    :return:
    '''
    host_gl_obj = host_gl()
    if request.method == 'GET':
        host_list = host_gl_obj.show_host()
        return render(request,'host.html',{'host_list':host_list})
    elif request.method == 'POST':
        action_host = request.POST.get('action')
        print(action_host)
        hostname = request.POST.get('hostname')
        if action_host == 'del':
            result = host_gl_obj.detele_host(hostname)
            print(result)
            return HttpResponse(result)
        if action_host == 'accept':
            result = host_gl_obj.accept_host(hostname)
            return HttpResponse(result)


def group(request):
    '''
    组管理页的方法
    :param request:
    :return:
    '''
    group_gl_obj = group_gl()
    if request.method == 'GET':
        all_group = group_gl_obj.show_all_group()
        return render(request,'group.html',{'all_group':all_group})
    elif request.method == 'POST':
        group_name = request.POST.get('del_group')
        result = group_gl_obj.del_group(group_name)
        return HttpResponse(result)

def add_group(request):
    '''
    新建组的方法
    :param request:
    :return:
    '''
    host_gl_obj = host_gl()
    if request.method == 'GET':
        host_list = host_gl_obj.show_host()
        return render(request,'add_group.html',{'host_list':host_list})
    elif request.method == 'POST':
        action = request.POST.get('action')
        group_name = request.POST.get('group_name')
        group_hosts_str = request.POST.get('group_table')
        group_hosts = eval(group_hosts_str)
        group_description = request.POST.get('group_description')
        group_hosts_number = len(group_hosts)
        print(action,group_name,group_hosts,group_description)
        group = {
            'group_name':group_name,
            'group_hosts':group_hosts,
            'group_description':group_description,
            'group_hosts_number':group_hosts_number
        }
        group_gl_obj = group_gl()
        status = group_gl_obj.add_group(group)

        return HttpResponse(status)


def file(request):
    '''
    文件管理的主方法
    :param request:
    :return:
    '''
    if request.method == 'GET':
        file_gl_obj = file_gl()
        file_list = file_gl_obj.show_file()
        return render(request,'file.html',{'file_list':file_list})
    elif request.method == 'POST':
        if request.POST.get('action'):
            action = request.POST.get('action')
            print(action)
            path_str = request.POST.get('path')
            relpath = join_path(eval(path_str))
            print(relpath)
            file_gl_obj = file_gl(relpath=relpath)
            if hasattr(file_gl_obj,action):
                func = getattr(file_gl_obj,action)
                result = func()
                print(result)
                if type(result) == str :
                    return HttpResponse(json.dumps({'status':result}))
                elif type(result) == dict:
                    return HttpResponse(json.dumps({'data':result}))
        elif request.FILES.get('file_obj'):
            file = request.FILES.get('file_obj')
            relpath_list = request.POST.get('relpath')
            relpath = join_path(eval(relpath_list))
            file_gl_obj = file_gl(relpath=relpath)
            result = file_gl_obj.upload_file(file)
            print(result)
            return HttpResponse(json.dumps({'status':result}))
        else:
            return HttpResponse('fff')


def log(request):
    return render(request,'log.html')