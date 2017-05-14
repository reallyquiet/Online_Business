# -*- coding:utf-8 -*-
"""
@author:Levy
@file:authored.py
@time:2017/5/918:55
"""

import base64
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
#message = 'NIKE Just Do It.' #商户信息,这里先设为常量，后可从数据库中读入。

#授权就是商家发送一段message，工厂签名并且附上自己的公钥（此处分为两个文件存储）。
def f_authored(message):
    with open('factory-private.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        signer = PKCS1_v1_5.new(rsakey)
        message = message.encode(encoding='UTF-8')
        digest = SHA.new(message)
        sign = signer.sign(digest)
        signature = base64.b64encode(sign)
        signature = signature.decode() #解码 字符串形式写进txt
        with open('f_s_signature.txt','w+') as f:
            f.write(signature)
            f.close()


f_authored("NIKE Just Do It.")
