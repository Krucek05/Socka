from flask import Flask, render_template, request

app = Flask(__name__, 
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def AllTogether():
   return render_template('AllTogether.html')


if __name__ == '__main__':
   app.run()
