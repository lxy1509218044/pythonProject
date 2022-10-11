#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/19 16:58
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 21 抓取91视频(复杂版).py
# @Software: PyCharm

# 和之前简单版本的不同之处在于这个网页的源代码里不包含m3u8的url了
# 也就是说这是一套全新的网页视频爬取方式
# 网页链接: http://www.91kanju2.com/vod-play/541-1-1.html
# 加密视频的操作,m3u8里包含kye的
"""
思路:
    1. 拿到主页面的页面源代码, 找到iframe
    2. 从iframe的页面源代码中拿到m3u8文件的地址
    3. 下载第一层m3u8文件 -> 下载第二层m3u8文件(视频 存放路径)
    4. 下载视频
    5. 下载秘钥, 进行解密操作
    6. 合并所有ts文件为一个mp4文件
"""
import requests
import re
from lxml.html import etree
from bs4 import BeautifulSoup
def get_li_href(url):
    resp = requests.get(url)
    # print(resp.text)
    html = etree.HTML(resp.text)
    request = html.xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/li[1]/a/@href')
    print(request)
    url1='http://www.91kanju2.com/'
    for u in request:
        ss = url1 + u
        print(ss)

        resp1 = requests.get(ss)
        # print(resp1.text)
        # 使用re解析,获取m3u8链接
        obj = re.compile(r"playerSwitch.*?line[lineIndex]+(?P<url>.*?)", re.S)  # 用来提取m3u8的url地址
        result = obj.finditer(resp1.text)
        for s in result:
            print(s.group('url'))



        resp.close()
        resp1.close()

def main(url):
    ifname_src = get_li_href(url)


if __name__ == '__main__':
    url = 'http://www.91kanju2.com/vod-detail/60886.html'
    main(url)