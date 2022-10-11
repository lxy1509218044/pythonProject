#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/16 11:19
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 17 进程池和线程池.py
# @Software: PyCharm
# 线程池: 一次性开辟一些线程. 我们用户直接给线程池子提交任务. 线程任务的调度交给线程池来完成
# 导入线程池和进程池
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
# 创建线程池
def fn(name):
    for i in range(1000):
        print(name, i)
if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn, name=f"线程{i}")
    # 等待线程池中的任务全部执行完毕. 才继续执行(守护)
    print("123")

# 创建进程池
# def fn(name):
#     for i in range(1000):
#         print(name, i)
# if __name__ == '__main__':
#     # 创建进程池
#     with ProcessPoolExecutor(50) as t:
#         for i in range(100):
#             t.submit(fn, name=f"线程{i}")
#     # 等待线程池中的任务全部执行完毕. 才继续执行(守护)
#     print("123")