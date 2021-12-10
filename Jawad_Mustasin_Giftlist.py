if __name__ == '__main__':
    print('PyCharm')
from flask import Flask, render_template, request
import sqlite3
import os
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('login.html')
database={'seller1':'p455w0rd','seller2':'p455w0rd'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name = request.form['username']
    pwd = request.form['password']
    if name not in database:
        return render_template('login.html', info='Invalid User')
    else:
        if database[name] != pwd:
            return render_template('login.html', info='Invalid password')
        else:
            return render_template('dash.html', name=name)

@app.route("/my_items",methods=['POST','GET'])
def my_items():
    return render_template('my_items.html')

@app.route("/sell_new_item",methods=['POST','GET'])
def sell_new_item():
    return render_template('sell_new_item.html')

if __name__ == "__main__":
    app.run(debug=True)