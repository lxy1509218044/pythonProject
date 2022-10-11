# 拿到contID
# 拿到videoStatus返回的json. -> srcURL
# 对srcURl里的内容进行修复
# 下载视频

import requests
# 视频原始url
url = "https://www.pearvideo.com/video_1764559"
# split()：拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）
contID = url.split("_")[1]
# 拿到抓包工具里的Request URL,然后对url进行修复得到真正的直链视频url
url1 = f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.19786460056378763"

# 使用requests解析
videoStatus = url1
head = {
    # UA
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    # 防盗链:Referer:源,当前本次请求的上一级是谁
    # "Referer" : "https://www.pearvideo.com/video_1764559"
    # 此网页防盗链就是url
    "Referer" : url
}
# 使用requests.get解析
resp = requests.get(videoStatus,headers=head)
# print(resp.text)
dict = resp.json()
# print(dic)
# 然后拿到抓包工具里的preview里的srcurl
srculr = dict['videoInfo']['videos']['srcUrl']
# print(srculr)
# 分离出srcurl中不一样的地方
systemTime = dict['systemTime']
# 真实的视频链接  https://video.pearvideo.com/mp4/third/20220606/cont-1764559-15898186-172529-ld.mp4
# srcurl的链接  https://video.pearvideo.com/mp4/third/20220606/1654658244484-15898186-172529-ld.mp4
# 只需要将 1654658244484 换成  cont-1764559就可以得到正确的视频链接
# replace()是一个替换函数 其使用格式为
# 变量 .replace('要替换的值','替换后的值')
srculr = srculr.replace(systemTime,f"cont-{contID}")
print(srculr)
# 下载视频
# with open('文件路径', '打开模式') as f:
with open("b.mp4","wb") as f:
# 连续写入文字：文件名.writre('写入内容'，模式选择)
    f.write(requests.get(srculr).content)
    print('over')
resp.close()

