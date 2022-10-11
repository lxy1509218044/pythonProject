#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/23 9:05
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 22 selenium各种操作(抓拉钩网).py
# @Software: PyCharm
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys # 按钮导入
# 前置操作
web = Chrome()
web.get('https://www.lagou.com/')
# 找到某个元素,再使用 点击事件 点击这个元素
el = web.find_element(By.XPATH,'//*[@id="changeCityBox"]/ul/li[1]/a').click()
# el.click() #使用点击事件
time.sleep(2) # 让浏览器缓一会
# 找到输入框,输入python => 然后输入回车(Keys.ENTER)/或者是/点击搜索按钮
web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys('python',Keys.ENTER)

# 找到页面中存放数据的所有li

li_list = web.find_elements(By.XPATH,'//*[@id="jobList"]/div[1]')
for li in li_list:
    # 找到个li的要求职位
    job_name = li.find_element(By.XPATH,'./div/div/div/div/a').text
    job_jiage = li.find_element(By.XPATH,'./div/div/div/div[2]/span').text
    print(job_name,job_jiage)