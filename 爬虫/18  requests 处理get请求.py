import requests

_in = input('输入你要搜索的内容:')
url1 = 'https://www.sogou.com/sogou?pid=sogou-site-7985672db979303a&query='
url = str(url1 + _in)
print(url.strip())
ua = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
resp = requests.get(url,headers=ua)
resp.encoding = 'utf-8'
print(resp.text)