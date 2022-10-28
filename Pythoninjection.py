from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__, 
            static_url_path='', 
            static_folder='static',
            template_folder='templates')


@app.route('/')
@app.route('/Pythoninjection')

def index():
    name = 'kristian'
    return render_template('Pythoninjection.html', title='Welcome', username=name)

app.run()