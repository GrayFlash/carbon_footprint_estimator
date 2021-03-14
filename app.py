from flask import Flask, render_template, redirect, flash, request
from utils.dte_scraper import *
from flask import url_for
from utils.db import get_db

# Configure application
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('/index.html')

@app.route('/fetch_news', methods=['GET','POST'])
def fetch_news():
    news_list = scrap()
    print("new_list=> ",news_list)
    return render_template('/news_dte.html', news_list=news_list)

@app.route('/contact_us', methods=['POST', 'GET'])
def contact_us():
    return render_template('/contact.html')

@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('/about.html')

@app.route('/blog', methods=['POST', 'GET'])
def view_blog():
    db = get_db()
    posts = db.execute(
        "SELECT id, title, body, created, author_name"
        " ORDER BY created DESC"
    ).fetchall()
    return render_template('/blog_gaurav.html', posts=posts)


@app.route('/create_blog', methods=['POST', 'GET'])
def create_blog():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        author_name = request.form["author_name"]
        error = None

        if not title:
            error = "Title is required."
        if not body:
            error="Body is required"
        if not author_name:
            error = "No anonymous publication allowed"

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO post (title, body, author_name) VALUES (?, ?)",
                (title, body, author_name),
            )
            db.commit()
            return redirect(url_for("index"))
    return render_template('/create_blog.html')