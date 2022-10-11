import requests

_in = input('输入想要翻译的单词:')
url = 'https://fanyi.baidu.com/sug'
ua = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
date = {
    'kw': _in
}
resp = requests.post(url,headers=ua,data= date)
print(resp.apparent_encoding)
print(resp.cookies)
# json()方法拿到JSON数据
for a in resp.json()['data']:
    print(a)


