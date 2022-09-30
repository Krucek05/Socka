from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def board():
   return render_template('cboard.html')
if __name__ == '__main__':
   app.run()