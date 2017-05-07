# <center>现代密码学实验</center>

## 1. 内容
调研代理签名的基础知识，模拟搭建电子商务平台。  

## 2. 功能
* 工厂给商户授权(对商户的权限、卖出产品承担的责任等签名).  
* 用户查询工厂的认证公钥.  
* 用户检查工厂给商户的授权是否正确，厂商的签名是否有效.  
* 用户提货，商户在购买证明上签名.  
* 用户检验签名是否有效.  
* 若出现问题，可以凭商户的电子签名和授权书等电子文档向商户和工厂索取赔偿.  

## 3. 技术栈
* 使用`Python`的`Django`框架，采用`B/S`结构.  
* 前端使用`Material Design Bootstrap`框架.  
* 商户的密钥使用`RSA`，签名使用`SHA 256`.  
* 数据库使用`Mongodb`.  


## 4. 开发环境搭建
### 4.1 Python
使用`Python 3.6`，`Anaconda`发行版(https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-4.3.1-Windows-x86_64.exe).  
> 安装过程中安装路径个人建议安装在分区根目录，比如我的安装路径为`D:\Anaconda3\`，其余的默认就好.  
> 安装完之后打开命令行，执行以下命令:  
> ```
> conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
> conda config --set show_channel_urls yes
> ```
> 之后如果要安装某个某个包，比如安装`Django`，只需要执行`conda install django`即可.  


### 4.2 Mongodb
下载地址: `https://www.mongodb.com/dr/fastdl.mongodb.org/win32/mongodb-win32-x86_64-2008plus-ssl-3.4.4-signed.msi/download`.  
安装过程没有什么要注意的，可根据自己的情况修改安装路径.  


## 5. 具体实现
* 商户点击`我是商户`按钮，提交个人信息以及自己的公钥到服务器，然后服务器使用工厂的私钥对商户的公钥进行签名认证，并将签名附在商户公钥后发布在网站上.  
* 用户点击查询按钮，在页面下方直接显示工厂的公钥；用户亦可以输入商户的名称查询商户的授权和签名是否正确.  
* 用户购买东西之后，商户需要对一些必要的信息用自己的私钥进行签名并发给用户，信息包括**商品名称**，**商户名称**，**购买时间**.  
* 用户使用商户的公钥对购买证明上的签名进行验证.  


## 6. 分工
`Dou`，`Yang`和`Yuan`负责**密码学部分**的实现，`Pang`负责前端页面的实现，`Cao`负责**服务器交互部分**.  


## 7. Referrences
* [数字签名是什么](http://www.ruanyifeng.com/blog/2011/08/what_is_a_digital_signature.html)  
* [`Python`快速入门教程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
* [`Django`快速入门教程](http://www.ruanyifeng.com/blog/2011/08/what_is_a_digital_signature.html)  
* [`Mongodb`快速入门教程](http://www.runoob.com/mongodb/mongodb-tutorial.html)  
* [`Git`入门教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)  

