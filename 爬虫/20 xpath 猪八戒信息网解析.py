#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/15 19:10
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 20 xpath 猪八戒信息网解析.py
# @Software: PyCharm
# 网址:https://www.zbj.com/index.php
import requests
from UA_info import ua
from lxml.html import etree
# 网页:https://huhehaote.zbj.com/search/f/?kw=%E5%89%8D%E7%AB%AF
url = 'https://huhehaote.zbj.com/search/f/?kw=%E5%89%8D%E7%AB%AF'
resp = requests.get(url, headers=ua)
# print(resp.text)
# 解析
html = etree.HTML(resp.text)

# 第一种方法,先定位路径再进行拼接,适用于要寻找的一段文字之间有 被标签分隔开 的情况
# 先把路径定位到到整个页面所有服务商服务名字的div
request = html.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')

for d in request:
    # 再把路径定位到具体的名字'p'标签上
    s = d.xpath('./div/div/a[2]/div[2]/div[2]/p/text()')
    # 绝对路径:/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div[1]/div/div/a[2]/div[2]/div[2]/p
    # 由于'前端'两个字作为搜索路径被高亮显示了它的路径为'h1'没有被我们加入进来,所以得到的结果是一个由 , 分开的两个词
    # print(s)
    # 通过使用join函数将两个词拼接完完整的一个词以供我们使用
    Splicing= '前端'.join(s)
    # print(Splicing)
    f= list(s) # 转换为列表
    # print(f)
    # print(type(Spl))
# 第二种方法.直接找每个服务商服务的价格等..各种内容,适用于要寻找的一段文字之间没有被标签分隔开的情况
# 直接找到服务价格
request1 = html.xpath('//*[@id="utopia_widget_76"]/a[2]/div[2]/div[1]/span[1]/text()')
# print(request1)
# 直接找到产品公司名称
request3 = html.xpath('//*[@id="utopia_widget_76"]/a[1]/div[1]/p/text()')
# print(type(request3))
# print(request3)
# 合并获取到的信息,通过zip函数压缩,再for出来
# z = zip(f,request3,request1)
# for a in z:
#     print(a)

resp.close()
