# :https://www.umei.cc/?adfwkey=cof73
# 拿到主页面的页面源代码,提取到子页面的链接地址,HERF
# 通过herf拿到子页面的内容,从子页面拿到推片的下载地址 img >
import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umei.cc/?adfwkey=cof73"
resp = requests.get(url)
resp.encoding = "utf-8"
# print(resp.text)
# 把源代码交给bs
page = BeautifulSoup(resp.text, "html.parser")
img = page.find("div", class_="pic-box").find_all("a")  # 范围第一次缩小,再拿到a标签
# print(img)
hurl = "https://www.umei.cc/"
for a in img[1:]:  # [1:]跳过第一个空链接
    hrefs = hurl + a.get('href')
    # print(hrefs) # 输出网页链接
    # 拿到子页面的源代码
    child_resp = requests.get(hrefs)
    child_resp.encoding = "utf-8"
    # 从子页面拿到图片下载地址
    child_resp = BeautifulSoup(child_resp.text, "html.parser")
    se = child_resp.find("section", class_="img-content")
    img2 = se.find("img")  # 找到img标签
    src = img2.get("src")  # 再次找到img下面的src属性
    print(src)
    # 下载图片
    img_resp = requests.get(src)
    img_resp.content  # 这里拿到的是字节
    img_name = src.split("/")[-1]  # 拿到url中最后一个/之后的内容
    with open("img1/" + img_name, mode="wb") as f:
        f.write(img_resp.content)  # 图片内容写入文件
        print("over", img_name)

    time.sleep(1)
resp.close()
