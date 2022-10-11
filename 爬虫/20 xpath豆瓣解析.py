
#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/16 9:51
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 20 xpath豆瓣解析.py
# @Software: PyCharm
import requests
import time
import csv
from lxml.html import etree
a = "https://movie.douban.com/top250?start="
c = '&filter='
for x in range(250):
    url = "https://movie.douban.com/top250?start=" + str(x) + "&filter"
    # print(url)
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=head)

    html = etree.HTML(resp.text)
    # 查找电影名
    request = html.xpath('/html/body/div[3]/div[1]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]/text()')
    # print(request)
    # 查找评分
    request2 = html.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[2]/text()')
    # print(request2)
    # 查找评论
    request3 = html.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/p[2]/span/text()')
    # print(request3)
    # 合并数据
    for request4 in request+request2+request3:
        print(request4)

    # 保存数据
    with open('douban.csv','a',newline="")as f:
        f.write(request1)
        print('over')

    time.sleep(2)
    resp.close()