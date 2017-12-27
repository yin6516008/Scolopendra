#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Create your views here.
import os
import json
import re
from django.shortcuts import render,HttpResponse,redirect,render_to_response
from Classes import api
from Classes.fileMnage import file_gl
from Classes.General import correct_Data,join_path

Ascii_Re = re.compile('\\.{3}')
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
    if request.method == 'GET':
        #验证用户是否已经登陆，检查用户session
        if request.session.get('user',False):
            return render(request,'action.html')
        else:
            return redirect('/login/')

    if request.method == 'POST':
        hosts = request.POST.get('hosts')
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

def upload(request):
    file_obj = request.FILES.get('upload_file')
    status = api.save_file_to_salt_root(file_obj)
    return HttpResponse(status)

def file(request):
    if request.method == 'GET':
        file_gl_obj = file_gl()
        file_list = file_gl_obj.show()
        return render(request,'file.html',{'file_list':file_list})
    elif request.method == 'POST':
        if request.POST.get('change_dir'):
            relpath_list = request.POST.get('change_dir')
            relpath = join_path(eval(relpath_list))
            file_gl_obj = file_gl(relpath=relpath)
            file_list = file_gl_obj.show()
            return HttpResponse(json.dumps(file_list))
        elif request.FILES.get('file_obj'):
            file = request.FILES.get('file_obj')
            relpath_list = request.POST.get('relpath')
            relpath = join_path(eval(relpath_list))
            file_gl_obj = file_gl(relpath=relpath)
            result = file_gl_obj.save_file_to_salt_root(file)
            return HttpResponse(result)
        elif request.POST.get('new_dir_data'):
            new_dir_str = request.POST.get('new_dir_data')
            relpath = join_path(eval(new_dir_str))
            file_gl_obj = file_gl(relpath=relpath)
            result = file_gl_obj.new_dir()
            return HttpResponse(result)