from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Mustafa@2856'
app.config['MYSQL_DATABASE_DB'] = 'Blogs'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

def addblog():
  pass

def getblogs():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * FROM post")
    data = cursor.fetchall()
    return data
