#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/23 11:07
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 22 selenium(无界面浏览器).py
# @Software: PyCharm
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys # 按钮导入
from selenium.webdriver.support.select import Select #列表导入

web =Chrome()
web.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')
# 定位到下拉列表
sel_el = web.find_element(By.XPATH,'//*[@id="OptionDate"]').click()
# 对元素进行包装,包装成下拉列表
sel = Select(sel_el)
# 让浏览器进行选项调整
for i in range(10): # i就是每一个下拉列表的索引位置
    sel.select_by_index(i) # 按照索引进行切换
    time.sleep(2)
    table = web.find_element(By.XPATH,'//*[@id="TableList"]/table')
    print(table.text) # 打印索引






