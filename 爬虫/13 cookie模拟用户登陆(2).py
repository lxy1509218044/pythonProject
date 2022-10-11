#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/17 22:22
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 13 cookie模拟用户登陆(2).py
# @Software: PyCharm
import  requests
import re
from lxml.html import etree

url = 'https://www.17k.com//chapter/3430275/46542695.html'
head = {
    'cookie': 'GUID=3f9c6165-1a6a-472f-bbfc-6dfb22ab9ddd; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F05%252F25%252F95%252F96969525.jpg-88x88%253Fv%253D1654651196000%26id%3D96969525%26nickname%3D%25E4%25BB%258A%25E4%25BE%259D%25E5%25AD%2590%25E6%25B4%259B%26e%3D1670208911%26s%3D1b68e3ea4b75cb7c; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2296969525%22%2C%22%24device_id%22%3A%2218140e4659e38-05988200245b4-26021b51-1327104-18140e4659f90%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%223f9c6165-1a6a-472f-bbfc-6dfb22ab9ddd%22%7D',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

resp = requests.get(url,headers=head)
resp.encoding = 'utf-8'
# print(resp.text)
tree = etree.HTML(resp.content)
# 匹配小说里的内容
result = tree.xpath("/html/body/div[4]/div[2]/div[2]/div[1]/div[2]/p/text()")
                   # /html/body/div[4]/div[2]/div[2]/div[1]/div[2]/p
# print(result)
for a in result:
    print(a)
