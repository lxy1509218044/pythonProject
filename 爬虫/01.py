#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/5 20:10
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 爬虫.py
# @Software: PyCharm

# 服务器渲染：在服务器那边直接把数据和html整合在一起，统一返回给浏览器
# 客户端渲染：第一次请求只要一个html骨架，第二次请求拿到数据，进行数据演示
# 在页面源代码，看不到数据
# 熟练使用浏览器抓包工具
import requests

url = 'https://www.bilibili.com/video/BV19g411X7cb'
dic = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33"
}  # 加上一个请求头
resp = requests.get(url, headers=dic)  # 处理一个小小的反爬虫
print(resp) #输出网页读取结果
print(resp.text)  # 拿到页面源代码
