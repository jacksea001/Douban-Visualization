# -*- codeing = utf-8 -*-
# @Time : 2021/3/24 22:48
# @Author : jack_sea
# @File : sample.py
# @Software : PyCharm


import bs4   # 网页解析，数据获取
import re    # 正则表达式，进行文字匹配
import urllib.request, urllib.error # 制定URL,获取网页数据
#import xlwt                       #进行Excel操作
import sqlite3         # 进行SQLite数据操作

url="https://movie.douban.com"
headers = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))





