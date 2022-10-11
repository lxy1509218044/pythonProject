#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/5 22:37
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 04 csv保存.py
# @Software: PyCharm
# 现在创建一个新的csv文件
import csv
import requests

# with open('文件路径', '打开模式') as f:
with open("b.mp4", "wb") as f:
    # 连续写入文字：文件名.writre('写入内容'，模式选择)
    f.write(requests.get(srculr).content)
    print('over')