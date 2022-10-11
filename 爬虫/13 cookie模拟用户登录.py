# 登录 -> 带着cooki
# 带着cokie去请求到书架url -> 书架上的内容

# 必须把两个操作连起来
# 我们可以使用session进行请求 -> sessinon你可以认为是一串请求,在这个过程中的cookie不会丢失

import requests

# # 第一种:正常会话方式获取到cookie
# session = requests.session()
# # cookie数据
# data = {
#     "loginName": "18047491457",
#     "password": "lixinyu1834"
# }
# # 1.登录
#
# url ="https://passport.17k.com/ck/user/login"
# # 得到cookie
# resp = session.post(url,data = data)
# resp.encoding = "utf-8"
# print(resp.text)
# print(resp.cookies)
#
# # 2.登录拿书架上的数据
# # 刚才的session中是有cookie的
# # 找到书架,开发者抓包工具里搜索shelf,在preview源代码里可看到书籍名称,去headers里复制url
# resp = session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
# print(resp.json())
# resp.close()


# 第二种:使用requests.get,复制cooklie过来
url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
head = {
"Cookie": "GUID=3f9c6165-1a6a-472f-bbfc-6dfb22ab9ddd; sajssdk_2015_cross_new_user=1; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F05%252F25%252F95%252F96969525.jpg-88x88%253Fv%253D1654651196000%26id%3D96969525%26nickname%3D%25E4%25BB%258A%25E4%25BE%259D%25E5%25AD%2590%25E6%25B4%259B%26e%3D1670208911%26s%3D1b68e3ea4b75cb7c; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2296969525%22%2C%22%24device_id%22%3A%2218140e4659e38-05988200245b4-26021b51-1327104-18140e4659f90%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%223f9c6165-1a6a-472f-bbfc-6dfb22ab9ddd%22%7D"
}
resp = requests.get(url,headers=head)
print(resp.text)