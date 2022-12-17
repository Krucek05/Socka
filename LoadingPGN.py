from flask import Flask , render_template, redirect, url_for, request

app = Flask(__name__, 
            static_url_path='', 
            static_folder='static',
            template_folder='templates')


@app.route('/',methods=['GET', 'POST'])
def pgnviewer():
    pgnString = ""
    return render_template('LoadingPGN.html', Mypgn=pgnString)


def board():
   pgnString1 = "1. e4 c5 { The ambitious Sicilian Defense! Black is fighting for the center but from the side, without going for a symmetrical pawn structure. } 2. Nf3 d6 3. d4 { The Open Sicilian. The first five moves of the Sicilian Dragon are the same as in the Najdorf on which I also have a freshly published course. } 3... cxd4 4. Nxd4 Nf6 5. Nc3 { Up until this point, it is not clear what type of Sicilian Black is going to play. There is the Classical Sicilian with  5...Nc6  and the Najdorf with  5...a6  , but this course deals with the most romantic and aggressive of all Sicilians: The Dragon. } 5... g6 { The move that defines the Dragon Sicilian. This opening is named after the pawn structure h7-g6-f7-e7-d6 that has the shape of a Dragon @@StartBracket@@at least that's what they brainwashed me to believe when I was a kid@@EndBracket@@ and, incidentally, the name also reflects the spirit of the variation.  The Dragon is notoriously ambitious, risky and reckless. However, when going over the lines during one of my many training sessions for the Candidates tournament, I discovered that its reputation for being dubious is rather undeserved. The Dragon has always been a popular and very successful opening for amateurs and club players, but I believe that, in light of the groundbreaking discoveries I will present in this course, it can be played all the way up to the very highest level.  Now that I have some experience with the French and the Najdorf course, I believe I can strike a very fine balance between presenting cutting-edge, top-level chess theory and offering clear and practical guidance to players of all levels. } 6. Be3 { By far the most played and also the most dangerous setup, called the Yugoslav Attack. It makes up the main body of this course, but of course, all the sidelines on move 6 are thoroughly covered, too. } 6... Bg7 { The idea of the Dragon is to develop the bishop to the long diagonal, while also keeping the central pawn structure e7-d6 intact. Interestingly, this often means that, besides going for an attack on the queenside, Black is also often happy to enter an endgame, as his pawn structure is excellent and there is not much White can offer in return for our pressure along the semi-open c-file. White, on the other hand, will try to trade off the pride of our position @@StartBracket@@the g7-bishop@@EndBracket@@ with Qd2 and Bh6 @@StartBracket@@or Bd4 in some cases@@EndBracket@@ and use the g6-pawn as a target for an attack on the kingside with h4-h5. } 7. f3 O-O { The trendy, so-called Dragodorf system with  7...a6!?  in which Black tries to stay flexible and play a combination of the Dragon @@StartBracket@@6... g6@@EndBracket@@ and the Najdorf @@StartBracket@@6... a6@@EndBracket@@, played a couple of times by Magnus Carlsen @@StartBracket@@!@@EndBracket@@ will be covered in the bonus chapter, but the main recommendation is the traditional Dragon, which I find more reliable and sound. } 8. Qd2 Nc6 { And now we landed in the main tabia of the Dragon Yugoslav Attack. Here, White has to choose between the old main line with  9.Bc4  and the more modern approach with  9.O-O-O  allowing d5, which, as it turns out, doesn't immediately solve all the opening problems. } 9. Bc4 Nxd4 { My mainrecommendation. It will be thoroughly examined in the course. } *"
   return render_template('Pgnviewer.html',Mypgn=pgnString1)

if __name__ == '__main__':
   app.run()
   