#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/5 22:44
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 05 re解析.py
# @Software: PyCharm

# 数据解析概述
# 在上一章中，我们基本上掌握了抓取整个网页的基本技能，
# 但是呢，大多数情况下，我们并不需要整个网页的内容，只是需要那么一小部分，怎么办呢？
# 这就涉及到了数据提取的问题。
# 本课程中，提供三种解析方式：
# 1.re解析(正则表达式)
# 2.bs4解析
# 3.xpath解析
# 这三种方式可以混合进行使用，完全以结果做导向，只要能拿到你想要的数据。
# 用什么方案并不重要。当你掌握了这些之后。再考虑性能的问题。

# （re解析）正则表达式
# 正则表达式Regular Expression、正则表达式，一种使用表达式的方式对字符串进行匹配的语法规则。
# 我们抓取到的网页源代码本质上就是一个超长的字符串，想从里面提取内容。用正则再合适不过了。
# 正则的优点：速度快，效率高，准确性高正则的缺点：新手上手难度有点儿高。
# 不过只要掌握了正则编写的逻辑关系，写出一个提取页面内容的正则其实并不复杂正则的语法：
# 使用元字符进行排列组合用来匹配字符串 在线测试正则表达式https://tool.oschina.net/regex/
# 元字符：具有固定含义的特殊符号常用元字符：

# re模块

import re

# # findall:匹配字符串中所有符合正则的内容
# list = re.findall(r"\d+", "我的电话号是:10086,我女朋友的电话是:10011")
# print(list)
# print('////////////////////////////////')
#
# # finditer:匹配字符创的所有内容[返回的是迭代器]
# it = re.finditer(r"\d+", "我的电话号是:10086,我女朋友的电话是:10011")
# print(it)  # 输出内存地址
# for a in it:
#     print(a.group())
# print('////////////////////////////////')
#
# # search:找到一个结果就返回,返回结果是match对象,拿数据需要.group对象,每次检索一次
# s = re.search(r"\d+", "我的电话号是:10086,我女朋友的电话是:10011")
# print(s.group())
# print(s.group())
# print('////////////////////////////////')
#
# # match是从头开始匹配
# q = re.match(r"\d+", "我的电话号是:10086,我女朋友的电话是:10011")
# print(q.group())
# print('////////////////////////////////')

# # 预加载正则表达式,就是调用正则表达式
# obj = re.compile(r"\d+")
#
# ret = obj.finditer('我的电话号是:109000')
# for it in ret:
#     print(it.group())
#
# ret = obj.findall('呵呵,我就不信你不换换台55555555544')
# print(ret)

s = """"
<div class='Jay'><span id='1'>非我司</span></div>
<div class='说的啥'><span id='2'>中反算</span></div>
<div class='阿迪王'><span id='3'>中国人通</span></div>
<div class='富人3'><span id='4'>中通</span></div>
<div class='捅人意'><span id='5'>通</span></div>
"""

# ?P<分组名字>正则 可以单独从正则匹配的内容中进一步提取内容
obj = re.compile(r"<div class='(?P<xm>.*?)'><span id='(?P<id>\d+)'>(?P<dz>.*?)</span></div>", re.S)  # re.S:让.能匹配到换行符

result = obj.finditer(s)
for s in result:
    print(s.group('xm', 'id', 'dz'))
