# 原理:通过第三方的一个机器去请求
# 免费代理IP网站   https://www.zdaye.com/dayProxy/ip/333442.html
import requests

# 代理ip:端口号  39.130.150.23:80
proxies = {
    "http": "http://39.130.150.44:80"
}
# proxies:代理模块
resp = requests.get("https://www.bilibili.com", proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)
