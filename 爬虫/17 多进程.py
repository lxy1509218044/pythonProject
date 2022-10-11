#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/16 11:08
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 17 多进程.py
# @Software: PyCharm
# 多进程
from multiprocessing import Process # 进程类
def fun():
    for i in range(10):
        print('子进程',i)
if __name__ == '__main__':
    p = Process(target=fun)
    p.start()
    for i in range(10):
        print('主进程',i)



