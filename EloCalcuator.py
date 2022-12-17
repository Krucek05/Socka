from flask import Flask, render_template, request
import math



app = Flask(__name__, 
             static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route("/", methods=['GET', 'POST'])

def buttons():
    if request.method =='GET' :
        return render_template('button.html',ResultElo1 = -1, )
    else :
        Ra = float(request.form.get('Ra')) 
        Rb = float(request.form['Rb'])
        K = float(request.form['K'])

        EloDelta = Rb - Ra
        if (EloDelta > 0):
            if (EloDelta > 400):
                EloDelta = 400.0
        else:
            if (EloDelta < -400):
                EloDelta = -400.0

        Ea = 1.0 / (1.0 + pow(10, (EloDelta / 400.0))) 

        ResultElo1 = Ra + K * (1.0 - Ea)
        Delta1 = round(ResultElo1 - Ra, 1)
        ResultElo1 = round(ResultElo1, 1)

        ResultElo2 = Ra + K * (0.0 - Ea)
        Delta2 = round(ResultElo2 - Ra, 1)
        ResultElo2 = round(ResultElo2, 1)

        ResultElo3 = Ra + K * (0.5 - Ea)
        Delta3 = round(ResultElo3 - Ra, 1)
        ResultElo3 = round(ResultElo3, 1)

        return render_template('button.html', ResultElo1 = ResultElo1, ResultElo2 = ResultElo2, ResultElo3 = ResultElo3, Delta1 = Delta1, Delta2 = Delta2, Delta3 = Delta3, Ra = Ra, Rb = Rb, K = K)    




if __name__ == '__main__':
    app.run()

