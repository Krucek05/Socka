from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__, 
            static_url_path='', 
            static_folder='static',
            template_folder='templates')


@app.route('/',methods=['GET', 'POST'])
def board():
   

   return render_template('Uploading.html')

  
if __name__ == '__main__':
   app.run()