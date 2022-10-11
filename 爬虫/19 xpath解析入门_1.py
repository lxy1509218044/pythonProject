#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/15 18:40
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 19 xpath解析入门_1.py
# @Software: PyCharm
from lxml.html import etree

tree = etree.parse('D:/pythonProject/爬虫/b.html',etree.HTMLParser()) # 导入HTML文件
result = tree.xpath('/html/body/ol/li')
for a in result:
    result1 = a.xpath("./a/text()") # 在li中继续寻找,相对路径
    # print(result1)
    result2 = a.xpath("./a/@href") # 拿到属性值:@属性
    # print(result2)

print(tree.xpath('/html/body/div[1]/text()')) # 使用谷歌F12 copy模式自动调用xpath格式