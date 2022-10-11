import re
import requests
import csv
import time


a = "https://movie.douban.com/top250?start="
c = '&filter='
for x in range(0,11):
    b = (25 * x)
    url = "https://movie.douban.com/top250?start=" + str(b) + "&filter"
    print(url)
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=head)

    # 输出页面源代码
    # print(resp.text)
    # 正则表达式解析数据
    re1 = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?'
                     r'<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                     r'<span class="rating_num" property="v:average">(?P<pf>.*?)</span>.*?'
                     r'<span class="inq">(?P<pl>.*?)</span>', re.S)
    # 使用obj.finditerl分离源代码里的正则内容
    resul = re1.finditer(resp.text)
    for it in resul:
        print(it.group("name", "year", "pf", "pl"))
    # newline = ""为了写入文件后不会出现空行
    # "a"字符打开文件夹
    # encoding='utf-8’ 添加编码格式
    # 现在创建一个新的csv文件
    with open("www.csv", 'w', newline='') as f:
        file = csv.writer(f)
    # 然后打开这个csv文件
    write_on = open("www.csv", "a", newline="")
    # 将正则后的内容写入打开的这个文件内
    witer_in = csv.writer(write_on)
    for a in resul:
        dic = a.groupdict()
        dic['year'] = dic['year'].strip()
        witer_in.writerow(dic.values())
        # 将每次爬取结果显示出来
        print(a.group("name", "year", "pf", "pl"))
    # 关闭打开的文件
    write_on.close()
    print("over")
    # 休眠10秒
    time.sleep(10)
    # 关闭每次打开的网页
    resp.close()

