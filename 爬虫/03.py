# !/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/5 22:06
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 03.py
# @Software: PyCharm

import requests

url = 'https://movie.douban.com'

# 重新封装参数
param = {
    "type": "11",
    "interval_id": "100:3A90",
    "action": "",
    "start": 0,
    "limit": 20,
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}
read = requests.get(url=url, params=param, headers=headers)

print(read.request.url)  # 获取网页的url
print(read.request.headers)  # 获取网页读取网页的UA
print(read.text)  # 获取网页的源代码
read.close()  # 最后关闭resp
