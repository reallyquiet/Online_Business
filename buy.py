# -*- coding: utf-8 -*-
"""
Created on Wed May 31 19:29:14 2017

@version：python3.6
@author: Yang
@安装Cryptor库：https://github.com/dlitz/pycrypto/archive/master.zip 
"""

import base64
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

#购买商品
#商户用私钥在购买证明上签名
def shop_authentication(message):
    with open('shop-private.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        signer = PKCS1_v1_5.new(rsakey)
        message = message.encode(encoding='UTF-8')
        digest = SHA.new(message)
        sign = signer.sign(digest)
        signature = base64.b64encode(sign)
        signature = signature.decode() #解码 字符串形式写进txt
        with open('buy_signature.txt','w+') as f:
            f.write(signature)
            f.close()


#用户用商家的公钥验证购买证明是否有效
#出现问题，用户向商家要求索赔，商家用公钥验证用户提交的购买证明
def ver_buy_signature(message):
    with open('buy_signature.txt')as f:
        signature = f.read()
    with open('shop-public.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        sign = base64.b64decode(signature)
        verifier = PKCS1_v1_5.new(rsakey)
        #message需要编码
        message = message.encode(encoding='UTF-8')
        digest = SHA.new(message)
        ver = verifier.verify(digest,sign)
    return ver



shop_authentication("NIKE Just Do It.")
print (ver_buy_signature("NIKE Just Do It."))
