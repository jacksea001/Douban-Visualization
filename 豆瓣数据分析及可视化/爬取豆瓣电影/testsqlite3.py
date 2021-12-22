# -*- codeing = utf-8 -*-
# @Time : 2021/3/26 18:46
# @Author : jack_sea
# @File : testsqlite3.py
# @Software : PyCharm


import sqlite3
# 创建数据库
conn = sqlite3.connect("test.db")
print("opened database successfully")

c = conn.cursor()  # 获取游标
sql = '''
    create table company
         (id int primary key not null,
         name text not null,
         age int not null,
         address char(50),
         salary real) ;      
'''

c.execute(sql)  # 执行sql语句
conn.commit()  # 提交数据库操作
conn.close()   # 关闭数据库链接

print("成功建表")