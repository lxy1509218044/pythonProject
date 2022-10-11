#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/23 8:37
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 22 selenium引入.py
# @Software: PyCharm

import requests
# 能不能让我的程序链接到浏览器,让浏览器完成各种复杂的操作,我们只接受最终的结果
# selenium:自动化测试工具
# 可以打开浏览器,像人一样去操作
# 程序员可以从selenium上直接提取网页上的各种信息
# 环境搭建: pip install selenium
#          下载浏览器驱动:http://chromedriver.storage.googleapis.com/index.html
#               把解压缩后的文件放到python解释器所在的文件夹 where python

# 让selenium启动谷歌浏览器
from selenium.webdriver import Chrome
import time
# 1.创建浏览器对象
web = Chrome()
# 2.打开一个网址
web.get('https://www.baidu.com')
time.sleep(3)
