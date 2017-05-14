# -*- coding:utf-8 -*-
"""
@author:Levy
@file:c_verify_f.py
@time:2017/5/919:55
"""
import base64
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

#只需提供message 工厂公钥和签名已经存在文件里可以后台调取
def c_ver_f(message):
    with open('f_s_signature.txt')as f:
        signature = f.read()
    with open('factory-public.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        sign = base64.b64decode(signature)
        verifier = PKCS1_v1_5.new(rsakey)
        #message需要编码
        message = message.encode(encoding='UTF-8')
        digest = SHA.new(message)
        ver = verifier.verify(digest,sign)
    return ver

print (c_ver_f("NIKE Just Do It."))



