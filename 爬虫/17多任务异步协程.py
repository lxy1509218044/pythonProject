#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/17 9:58
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 17多任务异步协程.py
# @Software: PyCharm
# import time

# python编写协程的程序
import asyncio
import time

# 程序 1
# async def func():
#     print("你好啊, 我叫赛利亚")
# if __name__ == '__main__':
#     g = func()  # 此时的函数是异步协程函数. 此时函数执行得到的是一个协程对象
#     # print(g)
#     asyncio.run(g)  # 协程程序运行需要asyncio模块的支持


# 程序 2
# async def func1():
#     print("你好啊, 我叫潘金莲")
#     # time.sleep(3)  # 当程序出现了同步操作的时候. 异步就中断了
#     await asyncio.sleep(3)  # 使用异步操作的代码,await=挂起
#     print("你好啊, 我叫潘金莲")
#
# async def func2():
#     print("你好啊, 我叫王建国")
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print("你好啊, 我叫王建国")

# async def func3():
#     print("你好啊, 我叫李雪琴")
#     await asyncio.sleep(4)
#     print("你好啊, 我叫李雪琴")
#
# if __name__ == '__main__':
#     f1 = func1()
#     f2 = func2()
#     f3 = func3()
#     tasks = [f1, f2, f3]
#     t1 = time.time()
#     asyncio.run(asyncio.wait(tasks)) # 一次性启动多个任务(协程)
#     t2 = time.time()
#     print(t2 - t1)

# # 标准写法:
# async def func1():
#     print("你好啊, 我叫潘金莲")
#     await asyncio.sleep(3)
#     print("你好啊, 我叫潘金莲")
#
#
# async def func2():
#     print("你好啊, 我叫王建国")
#     await asyncio.sleep(2)
#     print("你好啊, 我叫王建国")
#
#
# async def func3():
#     print("你好啊, 我叫李雪琴")
#     await asyncio.sleep(4)
#     print("你好啊, 我叫李雪琴")
#
#
# async def main():
#     # 第一种写法
#     # f1 = func1()
#     # await f1  # 一般await挂起操作放在协程对象前面
#     # 第二种写法(推荐)
#     tasks = [
#         func1(),
#         func2(),
#         func3()
#         # asyncio.create_task(func1()),  # py3.8以后加上asyncio.create_task()
#         # asyncio.create_task(func2()),
#         # asyncio.create_task(func3())
#     ]
#     await asyncio.wait(tasks)
#
# if __name__ == '__main__':
#     t1 = time.time()
#     # 一次性启动多个任务(协程)
#     asyncio.run(main())
#     t2 = time.time()
#     print(t2 - t1)


# 伪代码,异步协程在爬虫领域的应用
async def download(url):
    print("准备开始下载")
    await asyncio.sleep(2)  # 网络请求  requests.get()
    print("下载完成")

async def main():
    urls = [
        "http://www.baidu.com",
        "http://www.bilibili.com",
        "http://www.163.com"
    ]
# 首先:
    # 准备异步协程对象列表
    tasks = []
    for url in urls:
        d = download(url)
        tasks.append(d)

    # tasks = [download(url) for url in urls]  # 这么干也行哦~
# 然后:
    # 一次性把所有任务都执行
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())





