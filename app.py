from flask import Flask, render_template, redirect, flash, request
from utils.dte_scraper import *
from utils.blogs import *
from flask import url_for

from utils.db import get_db
import pandas as pd
import numpy as np
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
    countries = []
    df = pd.read_csv("data.csv",error_bad_lines=False, delimiter=";")
    f = np.array(df)
    data = {}
    for i in f:
        countries.append(i[0])
        data[i[0]] ={"Coal":i[1],"Gas":i[2],"Oil":i[3],"Hydro":i[4], "Renewable":i[5],"Nuclear":i[6]}
    # print(data)
    return render_template('/contact.html', con=countries, data=data)

@app.route('/about', methods=['POST', 'GET'])
def about():
    print("Move to about")
    return render_template('/about.html')
    
@app.route('/blogs',methods=['POST','GET'])
def blogs():
    blog_list = getblogs()
    print(blog_list)
    return render_template('/blogs.html' , blogs=blog_list)

