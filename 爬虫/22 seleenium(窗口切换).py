#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/23 10:05
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 22 seleenium(窗口切换).py
# @Software: PyCharm
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
web = Chrome()

web.get('https://www.lagou.com/')

el = web.find_element(By.XPATH,'//*[@id="changeCityBox"]/ul/li[1]/a').click()
time.sleep(2)

web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys('python',Keys.ENTER)
time.sleep(2)

web.find_element(By.XPATH,'//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()
time.sleep(2)

# 如何进入到新窗口进行下一步操作
# 注意,在selenium的眼中,新窗口默认是补切换不过来的
web.switch_to.window(web.window_handles[-1])

# 在新窗口中提取内容
job_detail = web.find_element(By.XPATH,'//*[@id="job_detail"]/dd[2]/div').text
print(job_detail)
# 关掉子窗口
web.close()
# 变更selemium的窗口视角,回到原来的窗口中
web.switch_to.window(web.window_handles[0])
# 检测是否回到原窗口
print(web.find_element(By.XPATH,'//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click())

