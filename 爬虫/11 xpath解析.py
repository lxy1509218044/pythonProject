# xpath是在XML文档中搜索文档的一种语言
# html是xml的一个子集import requests
from fake_useragent import UserAgent
import requests
import html
from lxml import html
etree = html.etree

url = 'https://movie.douban.com/top250'
ua = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
resp = requests.get(url,headers=ua)
print(resp.text)
# print(soup.prettify())
tree = etree.HTML(resp.content)
result = tree.xpath("/ol/li/div/div/a/span[@class='title']./text()")
                # "/html/body/div[3]/div[1]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]./texe()"
print(result)
resp.close()