#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/15 17:33
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 19 lxml使用.py
# @Software: PyCharm
# xpath是在XML文档中搜索文档的一种语言
# html是xml的一个子集import requests
import requests
from lxml.html import etree
url = 'https://movie.douban.com/top250'
ua = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
resp = requests.get(url,headers=ua)
# print(resp.text)
# print(soup.prettify())
tree = etree.HTML(resp.text)
result = tree.xpath(".//ol[@class='grid_view']/li/text()")[0].strip()
print(result)
resp.close()