#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
from Classes.Base_module import Base_Class
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

# from pymongo import MongoClient
#
# mongo_server = 'localhost'
# mongo_port = 27017
# client = MongoClient(mongo_server,mongo_port)
# Scolopendra_db = client.Scolopendra_db



class prpcrypt(object):
    '''
    加密，解密模块
    '''
    def __init__(self):
        self.salt = '!@#$%$#@!1234567'
        self.mode = AES.MODE_CBC

    #加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def encrypt(self, text):
        cryptor = AES.new(self.salt, self.mode, self.salt)
        #这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        #因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        #所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)

    #解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.salt, self.mode, self.salt)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')

class user_gl(Base_Class):
    def __init__(self):
        Base_Class.__init__(self)
        self.__prpcrypt = prpcrypt()

    def user_auth(self,username,passwd,request):
        user_obj = self.Scolopendra_db.user.find_one({'username':username})
        if type(user_obj) == dict:
            if user_obj['passwd'] == self.__prpcrypt.encrypt(passwd):
                self.log_write(log_content="%s登陆成功,登陆ip为 %s" % (username,request.META['REMOTE_ADDR']),type='login')
                return True
            else:
                return False
        else:
            return False












