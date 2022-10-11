# !/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/5 22:00
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 02.py
# @Software: PyCharm
import requests

url = "https://fanyi.baidu.com/sug"
s = input("请输入你要翻译的单词")
dat = {
    "kw": s
}
# 发送post请求，发送的数据必须放在s字典里通过data进行传递
resp = requests.post(url, data=dat)
# 将服务器返回的内容直接处理成json() =》data
print(resp.json())
