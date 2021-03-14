from flask import Flask, render_template
from utils.dte_scraper import *
from utils.blogs import *
from flask import url_for

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
    print("Move to about")
    return render_template('/about.html')
    
@app.route('/blogs',methods=['POST','GET'])
def blogs():
    blog_list = getblogs()
    return render_template('/blogs.html' , blogs=blog_list)
