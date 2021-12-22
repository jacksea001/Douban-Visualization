# -*- codeing = utf-8 -*-
# @Time : 2021/3/28 19:13
# @Author : jack_sea
# @File : test_wordCloud.py
# @Software : PyCharm

import jieba  # 分词
from matplotlib import pyplot as plt  # 绘图，数据可视化
from wordcloud import WordCloud  # 词云
from PIL import Image  # 图片处理
import numpy as np   # 矩阵运算
import sqlite3

con = sqlite3.connect('doubanmovie.db')
cur = con.cursor()
sql = 'select quote from movie250'
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
#print(text)
cur.close()
con.close()

cut = jieba.cut(text) # 分词
string = '  '.join(cut)
print(string)

img = Image.open(r'.\static\assets\img\tree.jpg')
img_array = np.array(img) # 将图片转换为二维数组
wc = WordCloud(
    background_color='white',
    mask = img_array,
    font_path="msyh.ttc"
)
wc.generate_from_text(string)

#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off') # 是否显示坐标轴
# plt.show() # 显示生成图云图片

plt.savefig(r'.\static\assets\img\wordcloud.jpg',dpi=500)


