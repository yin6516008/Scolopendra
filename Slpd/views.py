#!/usr/bin/python
# -*- coding:utf8 -*-

from django.shortcuts import render

# Create your views here.
import json
import re
from django.shortcuts import render,HttpResponse,redirect
# from Classes import salt_api


def login(request):
    #登陆函数
    #:param request:
    #:return:
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
            return redirect('/action/')
        else:
            return HttpResponse('111')



# def index(request):
#     '''
#     主页函数
#     :param request:
#     :return:
#     '''
#     params = {'client':'local','fun':'cmd.run','tgt':'*','arg':'dir'}
#     method = request.method
#     #检查用户是否已经登陆
#     if method == 'GET':
#         try:
#             if request.session['is_login']:
#                 return render(request,'index.html')
#             else:
#                 return redirect('/login/')
#         except KeyError as e:
#             print(e)
#             return redirect('/login/')
    #执行用户提交的命令并返回结果
    # elif method == 'POST':
    #     cmd = request.POST.get('cmd')
    #     arg = request.POST.get('arg')
    #     print(arg)
    #     params['arg'] = arg
    #     res = salt_api.main(params)
    #     print(res)
    #     content = res['return'][0]
    #     # for k,y in content.items():
    #     #     print(type(y))
    #     #     content[k] = re.sub('\r\n','<br/>',y)
    #     print(content)
    #     return render(request,'index.html',{'content':content})


def action(request):

    #接收参数，并调用salt-api，得到结果返回数据

    if request.method == 'GET':
        #验证用户是否已经登陆，检查用户session
            if request.session.get('user',False):
                return render(request,'action.html')
            else:
                return redirect('/login/')

    if request.method == 'POST':
        #接收参数列表
        args = request.POST.get('args')
        args = json.loads(args)
        #接收minion
        hosts = request.POST.get('hosts')
        #接收模块
        module = request.POST.get('module')
        #接收模块的方法
        func = request.POST.get('func')
        #拼接模块和方法
        action = module + '.' +func
        #调用api
        # res = api.exec(hosts,action,args)
        #返回结果
        return HttpResponse(json.dumps(res),content_type='application/json')