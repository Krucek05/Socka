from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__, 
            static_url_path='', 
            static_folder='static',
            template_folder='templates')




@app.route('/',methods=['GET', 'POST'])
def init():
    segments = getPgnSegment()
    return render_template('TestPrint.html', TemplateHeaders = segments[0], TemplateMoves = segments[1])


def getPgnSegment():
    pgnString = '[Event "2. liga B Belusa - Batorove Kosihy"] [Site "?"] [Date "2022.10.09"] [Round "2"] [White "Bednar Jaromir"] [Black "Peter Sarok"] [Result "1-0"] [WhiteElo "2205"] [WhiteUrl ""] [WhiteCountry ""] [WhiteTitle ""] [BlackElo "2147"] [BlackUrl ""] [BlackCountry "HU"] [BlackTitle ""] 1. e4 e6 2. d3 d5 3. Nd2 Nf6 4. Ngf3 Nc6 5. c3 e5 6. h3 Be7 7. g3 O-O 8. Qe2 Re8 9. Bg2 h6 10. O-O Bf8 11. Nh2 Be6 12. f4 dxe4 13. dxe4 Qd6 14. f5 Bd7 15. Nb3 a5 16. Be3 b6 17. g4 a4 18. Nd2 Bc8 19. b4 axb3 20. axb3 Bb7 21. h4 Rxa1 22. Rxa1 Ra8 23. Rxa8 Bxa8 24. g5 hxg5 25. hxg5 Ne8 26. b4 Bb7 27. Ng4 g6 28. Nc4 Qd7 29. fxg6 fxg6 30. b5 Na7 31. Ncxe5 Qxb5 32. Qa2+ Kh8 33. Nxg6+ Kg7 34. N6e5 Nd6 35. Qe6 Qb1+ 36. Kh2 Bxe4 37. Qh6+ Kg8 38. Nf6# 1-0'
    
    #x = len(pgnString)
    #for i in range (x):
    headers = []
    moves = ""
    startSearch = 0
    startIndex = pgnString.find("[", startSearch) 
    endIndex = pgnString.find("]", startSearch + 1)
    while startIndex >= 0 :
        if startIndex >= endIndex :
            print("Unexpected error: startIndex >= endIndex")
            return headers, moves
        oneHeader = pgnString[startIndex + 1:endIndex]
        print(oneHeader)
        headers.append(oneHeader)
        lastHeaderIndex = endIndex + 1
        startSearch = lastHeaderIndex
        startIndex = pgnString.find("[", startSearch) 
        endIndex = pgnString.find("]", startSearch + 1)
    moves = pgnString[lastHeaderIndex:]
    print(moves)
    return headers, moves

if __name__ == '__main__':
   app.run()

  