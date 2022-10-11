# 网站链接:http://www.91kanju2.com/
import requests
import re
# url = 'https://v4.cdtlas.com/20220505/ZykPl7mY/1100kb/hls/index.m3u8' # 要爬取的视频网址
# head = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
# }
# resp = requests.get(url,headers=head) #解析网页url
# # print(resp.text)
#
# # 下载m3u8文件
# with open("中国合伙人.m3u8", mode="wb") as f:
#     f.write(resp.content) # 下载二进制内容
#     print("下载完毕")
# resp.colse()

# 解析m3u8文件
n=1
with open("中国合伙人.m3u8",'r',encoding='utf-8') as mp:
    for line in mp:
        line = line.strip() #先去掉空格,空白,换行符
        if line.startswith("#"):
            continue
        print(line)
# 下载视频片段
        resp1 = requests.get(line)
        f = open(f"中国合伙人/{n}.ts",'wb')
        f.write(resp1.content)
        n+=1
        print('完成一个')
# 合并视频
    # 使用工具合并