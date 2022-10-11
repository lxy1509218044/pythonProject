#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/7 10:14
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 09 北京新发地.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup

url = "http://zhongdapeng.com/shucaijiage/993.html"
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=head)
# print(resp.text) # 输出网页源码代码

# 解析数据
# 把页面源代码交给BeautifulSoup进行处理
page = BeautifulSoup(resp.text, "html.parser")  # 指定html解析器
# 从bs对象中查找数据
# find(标签,属性=值)
# find_all(标签,属性=值)
# table = page.find("ol", class_="grid_view")  # class 是python的关键字,不能直接使用
table = page.find("tr", attrs={"height": "36"})  # 改进,使用字典就只可以直接用.和上一行是一个意思
# 输出网页查找结果
print(table)
# 拿到所有数据行,通过find_all找到所有的tr [1:]开始做切片
trs = table.find_all("tr")[1:]
for tr in trs:  # 每一行数据
    tr.find_all("td")  # 再通过循环拿到每一行中的td
    name = tds[0].text  # .text拿到被标签标记的内容
    hight = tds[1].text
    kind = tds[2].text
    gui = tds[3].text
    data = tds[4].text
    tds = tds[5].text
    print(name,hight,kind,gui, data,tds)
    # 每次关闭页面
    resp.close()

    # 最后可添加文件保存
