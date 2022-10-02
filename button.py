import pprint
from traceback import format_list
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])

def button():
    if request.method == 'POST':
        if request.form.get('action1') == 'See text':
            pass
    elif request.method == 'GET':
        return render_template('button.html', )

    return render_template ("button.html", form=form)


if __name__ == '__main__':
        app.run()