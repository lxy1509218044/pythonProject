# https://m.dytt8.net/index2.htm
import re
import requests
import csv

url = "https://m.dytt8.net/index2.htm"
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
# verify = False 去掉安全验证
# 打开网页
resp = requests.get(url, headers=head, verify=False)
# 读取网页源代码
response = requests.get(url)
print(response.encoding)
# 指定字符集
resp.encoding="ISO-8859-1"
# 输出网页源代码
# print(resp.text)
# 正则表达式
obj1 = re.compile(r"2020看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'",re.S)
# 使用obj.finditerl分离源代码里的正则内容
resul1 = obj1.finditer(resp.text)
for a in resul1:
    ul = a.group('ul')
    # 输出正则后的内容
    print(a.group("name"))
    # 提取子页面链接
    resul2 = obj2.finditer(ul)
    for b in resul2:
        # 拼接子页面url地址:域名+子页面地址
        child_href = url + b.group('href').strip("/")


# 关闭网页
resp.close()
