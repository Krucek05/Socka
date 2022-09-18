from flask import Flask, render_template, Markup
import chess
import chess.svg
import sys


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name):
    return f"Hello, {name}!"

@app.route("/chess")
def funkica_meno():
    return render_template('template.html', num=12)
 
if __name__ == '__main__':
    app.run( debug=True )


