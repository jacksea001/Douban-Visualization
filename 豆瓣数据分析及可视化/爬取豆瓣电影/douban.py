# -*- codeing = utf-8 -*-
# @Time : 2021/3/26 19:29
# @Author : jack_sea
# @File : douban.py
# @Software : PyCharm



import bs4   # 网页解析，数据获取
import re    # 正则表达式，进行文字匹配
import urllib.request, urllib.error # 制定URL,获取网页数据
import xlwt                       #进行Excel操作
import sqlite3         # 进行SQLite数据操作
from bs4 import BeautifulSoup

def main():
    baseurl = "https://movie.douban.com/top250?start="

    #1.获取网页
    datalist = getData(baseurl)
    #savepath = ".\\豆瓣电影Top250.xls" #保持数据到excel表中
    dbpath = "doubanmovie.db"  #保存数据到数据库中
    #3.保存数据
    #saveDate(datalist, savepath)
    saveDateDB(datalist, dbpath)



#影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')  #创建正则表达式对象，表示规则（字符串模式）
#影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
#影片片名
findTitle = re.compile(r'<span class="title">(.*?)</span>')
#影片分数
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#影片评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#影片主题
findquote = re.compile(r'<span class="inq">(.*)</span>')
#影片相关内容——导演/演员/上映时间/剧情类型
findBd = re.compile(r'<p class="">(.*?) </p>', re.S)

#获取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10): #左闭右开,调取页面信息的函数10次
        url = baseurl + str(i*25)
        html = askURL(url) #保存获取网页的源码

        #2.逐一解析
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            data = []
            item = str(item)

            #影片详情的链接
            link = re.findall(findLink, item)[0]  #re库用来正则表达式查找指定的字符串
            data.append(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc) #添加图片
            titles = re.findall(findTitle, item) #片名可能只有一个中文名，没有外国名
            if(len(titles)==2):
                ctitle = titles[0]
                data.append(ctitle)  #添加中文名
                otitle = titles[1].replace("/", "") #去掉无关符号
                data.append(otitle)  #添加英文名
            else:
                data.append(titles[0])
                data.append(" ") #留空

            rating = re.findall(findRating, item)[0]
            data.append(rating)
            judgenum = re.findall(findJudge, item)[0]
            data.append(judgenum)

            quote = re.findall(findquote, item)
            if len(quote) != 0:
                quote = quote[0].replace("。", "") #去掉句号
                data.append(quote)
            else:
                data.append("  ")
            bd = re.findall(findBd , item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)', " ", bd) #去掉<br/>
            bd = re.sub('/', " ", bd) #替换/
            data.append(bd.strip())  #去掉前后的空格

            datalist.append(data)  #把处理好的一部电影信息放入datalist
    print(datalist)
    return datalist



#得到指定一个URL的网页内容
def askURL(url):
    head = {
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
    }

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html



#保存数据
def saveDate(datalist, savepath):
    print("save....")
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('豆瓣电影top250', cell_overwrite_ok=True)
    col = ("电影详情链接", "图片链接", "中文影片名", "外文英文名", "评分" ,"评分人数","影片主题","概述","国家","剧情","年份")
    for i in range(0,11):
        sheet.write(0, i, col[i])
    for i in range(0,250):
        print("第%d条" %i)
        data = datalist[i]
        for j in range(0, 11):
            sheet.write(i+1, j, data[j])
    book.save(savepath)


def saveDateDB(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index ==4 or index==5:
                continue
            data[index]='"'+data[index]+'"'
        sql = '''
                insert into movie250(
                info_link, pic_link, cname, ename,score,judgenum,quote,info
                )
                values(%s) ''' %",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()

    cur.close()
    conn.close()




def init_db(dbpath):
    sql = '''
        create table movie300
         (id integer primary key autoincrement,
         info_link text not null,
         pic_link text not null,
         cname varchar,
         ename varchar,
         score numeric ,
         judgenum numeric ,
         quote text,
         info text
         ); 
    ''' #创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)  # 执行sql语句
    conn.commit()  # 提交数据库操作
    conn.close() # 关闭数据库链接











if __name__ == '__main__':
    #init_db("movietest.db")   #创建数据库
    main()









