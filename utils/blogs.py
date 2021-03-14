from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'gray'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Password@123'
app.config['MYSQL_DATABASE_DB'] = 'Blogs'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

def add_blog(data):
    conn = mysql.connect()
    cursor =conn.cursor()
    curr = cursor.execute("SELECT * FROM post")
    cursor.execute("""INSERT INTO post(id,author_name,title,body) VALUES(%(id)s ,%(author)s ,%(title)s ,%(body)s )"""
                    ,{'id':int(curr)+1,'author':data[1],'title':data[0],'body':data[2]})
    conn.commit()

def getblogs():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * FROM post")
    data = cursor.fetchall()
    return data
    
def getblog(k):
    conn = mysql.connect()
    cursor =conn.cursor()
    k = int(k)
    cursor.execute("SELECT * FROM post WHERE id = " + str(k))
    data = cursor.fetchone()
    return data
