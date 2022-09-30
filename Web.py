
from flask import Flask, render_template, Markup
import chess
import chess.svg
import sys
from markupsafe import escape
from flask import url_for
from flask import request

app = Flask(__name__)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'
    

@app.route("/world")
def world():
    return "<h1>Hello, World<h1>" 


@app.route("/chess")
def funkica_meno():
    return render_template('template.html', num=12)

@app.route('/')
def index():
    return 'index'

@app.route('/user/<username>')
def profile(username):
    return f'{escape(username)}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('profile', username='Kristian Rucek'))

#@app.route('/login', methods=['GET', 'POST'])
#def login():
    #if request.method == 'POST':
   #     return do_the_login()
  #  else:
 #       return show_the_login_form()
#
#url_for('static', filename='style.css')#


@app.route("/<name>")
def hello(name):
    return f" {escape(name)}!"

 
if __name__ == '__main__':
    app.run( debug=True )


