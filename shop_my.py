# -*- coding:utf-8 -*-
"""
@author:Levy
@file:shop_my.py
@time:2017/5/90:46
"""

from Crypto import Random
from Crypto.PublicKey import RSA
def shop_key():
    # 伪随机数生成器
    random_generator = Random.new().read
    # rsa算法生成实例
    rsa = RSA.generate(1024, random_generator)
    # 商户的秘钥对的生成
    private_pem = rsa.exportKey()
    with open('shop-private.pem', 'wb') as f:
        f.write(private_pem)
    public_pem = rsa.publickey().exportKey()
    with open('shop-public.pem', 'wb') as f:
        f.write(public_pem)

