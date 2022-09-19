from flask import Flask, render_template, Markup
import chess
import chess.svg
import sys
from markupsafe import escape



app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/chess")
def funkica_meno():
    return render_template('template.html', num=12)

@app.route("/user")
def user():
    return "<h1>Welcome user of this website</h1> "
 
if __name__ == '__main__':
    app.run( debug=True )


