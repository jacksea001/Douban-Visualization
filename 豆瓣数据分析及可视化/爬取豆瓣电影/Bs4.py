# -*- codeing = utf-8 -*-
# @Time : 2021/3/24 23:26
# @Author : jack_sea
# @File : Bs4.py
# @Software : PyCharm

from bs4 import BeautifulSoup
file =open("./douban.html","rb") # rb--read bite 二进制读取
html = file.read()
bs = BeautifulSoup(html, "html.parser")

print(bs.title)
print(type(bs.title))

#1.Tag 标签及其内容，拿到他找到的第一个内容

print(bs.title.string)
print(type(bs.title.string))

#2.NavigableString 标签里的内容




