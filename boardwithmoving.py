

#board = chess.Board()

#for i in board.legal_moves:
	#print(i)

#board.push_san("e4")
#board.push_san("e5")

#print(board)

from flask import Flask, render_template, redirect, url_for, request
import chess

app = Flask(__name__)
@app.route('/',methods=['GET', 'POST'])


def board():
   return render_template('board.svg')

def button():
    if request.method == 'POST':
             return render_template("board.html")
    elif request.method == 'GET':
        return render_template('boardbutton.html')


if __name__ == '__main__':
   app.run()




  
