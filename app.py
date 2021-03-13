from flask import Flask, render_template
from utils.dte_scraper import *
# Configure application
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('/index.html')

@app.route('/fetch_news', methods=['GET','POST'])
def fetch_news():
    news_list = scrap()
    print("new_list=> ",news_list)
    return render_template('/news.html', news_list=news_list)
