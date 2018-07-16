from flask import Flask, render_template, flash, request, jsonify, session
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import json
import requests 
import sys
import re 
from bs4 import BeautifulSoup
import models as dbHandler
import sqlite3


 
# App config.

#DEBUG = True
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    li = {}
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        url = request.form['url']
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        name = soup.h1.text
        address = soup.address.text
        dbHandler.insertUser(url, name, address)
        li = dbHandler.retrieveUsers()
        return render_template('index1.html', data=li)

if __name__ == "__main__":
    app.run(debug=True)