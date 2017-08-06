#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2

url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'

values = {
    'username' : '402255453@qq.com',
    'password' : '1994030'
}

data = urllib.urlencode(values) # 编码工作
req = urllib2.Request(url, data)  # 发送请求同时传data表单
response = urllib2.urlopen(req)  #接受反馈的信息
the_page = response.read()  #读取反馈的内容

print the_page