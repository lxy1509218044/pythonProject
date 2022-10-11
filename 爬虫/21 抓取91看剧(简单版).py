#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/19 10:19
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 21 抓取91看剧(简单版).py
# @Software: PyCharm
# 流程:
# 1:拿到网页源代码
# 2:从源代码中提取m3u8的url
# 3:下载m3u8
# 4:读取m3u8文件,下载视频
# 5:合并视频
# m3u8不在网页源代码里的
# 首先查看网页源代码里是否包含m3u8的url链接
# 如果不包含链接,链接就被存放在js里,
# 这时候需要通过f12找到m3u8的url地址,然后对url进行请求

# 网站链接:http://www.91kanju2.com/
import requests
import re


url = 'http://www.91kanju2.com/vod-play/9985-1-1.html' # 要爬取的视频网址
head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
resp = requests.get(url,headers=head) #解析网页url

obj = re.compile(r"url: '(?P<url>.*?)',", re.S)  # 用来提取m3u8的url地址

m3u8_url = obj.search(resp.text).group("url")  # 拿到m3u8的地址

print(m3u8_url)
# # 下载m3u8内容文件
# resp2 = requests.get(m3u8_url, headers=head)
# with open("中国合伙人.m3u8", mode="wb") as f:
#     f.write(resp2.content)
#     print("下载完毕")
# resp2.close()

# 解析m3u8文件
n=1
with open("中国合伙人.m3u8",'r',encoding='utf-8') as mp:
    for line in mp:
        line = line.strip() #先去掉空格,空白,换行符
        if line.startswith("#"):
            continue
        print(line)
# 下载视频片段
        resp1 = requests.get(line)
        f = open(f"中国合伙人/{n}.ts",'wb')
        f.write(resp1.content)
        n+=1
        print('完成一个')
# 合并视频
    # 使用工具合并



resp.close()
