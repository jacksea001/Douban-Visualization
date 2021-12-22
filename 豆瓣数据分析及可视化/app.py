from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/movie')
def movie():
    datalist = []
    con = sqlite3.connect("doubanmovie.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()



    return render_template("movie.html", movies = datalist)


@app.route('/score')
def score():
    score = [] #评分多少种
    num =[] #每个评分的电影数量
    con = sqlite3.connect("doubanmovie.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        num.append(item[1])
    cur.close()
    con.close()
    return render_template("score.html", score=score, num=num)

@app.route('/Actors')
def Actors():
    return render_template("Actors.html")

@app.route('/world')
def world():
    return render_template("world.html")

@app.route('/moviecounts')
def moviecounts():
    return render_template("moviecounts.html")

@app.route('/movieyears')
def movieyears():
    return render_template("movieyears.html")

@app.route('/moviestype')
def moviestype():
    return render_template("moviestype.html")

@app.route('/team')
def team():
    return render_template("team.html")




if __name__ == '__main__':
    app.run()
