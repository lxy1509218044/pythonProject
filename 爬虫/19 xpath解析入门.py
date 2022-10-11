#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/15 18:19
# @Author  : super_lixinyu
# @Email   : 1509218044@qq.com
# @File    : 19 xpath解析入门.py
# @Software: PyCharm
from lxml.html import etree
xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷若</nick>
        <nick class="joy">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>热热热热热1</nick>
        </div>
        <span>
            <nick>热热热热热2</nick>
        </span>
    </author>

    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
"""
tree = etree.XML(xml)
# result = tree.xpath("/book/name")  # /表示层级关系,第一个/是根节点
result = tree.xpath("/book/name/text()")
result1 = tree.xpath("/book/author/nick/text()") # text()是拿里面的文本
result2 = tree.xpath("/book/author//nick/text()") # 寻找authon下所有的有关nick的标签
result3 = tree.xpath("/book/author/*/nick/text()") # * 任意节点,通配符匹配任意元素节点
result4 = tree.xpath("/book//nick/text()")
result5 = tree.xpath("/book/*/nick/text()")
print(result)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)