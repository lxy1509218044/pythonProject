#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/17 10:48
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 17异步http aiohttp模块的应用.py
# @Software: PyCharm
import aiohttp
import asyncio
# requests.get() == 异步操作的aiohttp
urls = [
    'http://kr.shanghai-jiuxin.com/file/mm/20211129/01yknsrg145.jpg',
    'http://kr.shanghai-jiuxin.com/file/mm/20211129/b2dpup0y0jv.jpg',
    'http://kr.shanghai-jiuxin.com/file/mm/20211129/pdmvwk4yjcd.jpg'
]
# 发送请求,得到图片内容,保存到文件
# aiohttp.ClientSession()  <==>  相当于requests
# requests.get()  <==>   .post()
# s.get  <==>    .post
async def aiodownload(url):
    # 设置图片名字
    name = url.rsplit("/",1)[1] # 从右面开始切,切一次==取最后一个/的后面内容
    # 异步操作每一步都要加await
    async with aiohttp.ClientSession() as session: # requests
        async with session.get(url) as resp: # resp = requests.grt()
            # 请求回来了,写入文件
            with open(name,mode='wb') as f: # 创建文件
                f.write(await resp.content.read()) #读取内容是异步的,需要awat挂起 resp.text()
    print(name, '搞定')
async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())
