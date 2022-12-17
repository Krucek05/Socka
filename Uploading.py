from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__, 
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def uploadFile():
   return render_template('Uploading.html')


# @app.route('/uploader', methods = ['GET', 'POST'])
# def UploadingGame():
#    if request.method == 'POST':
#       f = request.files['file']
#       f.save(secure_filename(f.filename))
#       return render_template("Uploading.html")
      
if __name__ == '__main__':
   app.run()





	
     