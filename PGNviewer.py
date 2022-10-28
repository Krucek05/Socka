from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__, 
            static_url_path='', 
            static_folder='static',
            template_folder='templates')


@app.route('/',methods=['GET', 'POST'])
def board():
   pgnString = "1. e4 e6 2. d4 d5 3. e5 (3. exd5 exd5 4. Nf3 (4. c4 Nf6 5. Nf3 Bb4+ 6. Nc3 O-O 7. Be2 dxc4 8. Bxc4 Bg4 9. O-O Nc6 10. Be3 Rb8) (4. Bd3 c5 5. Nf3 Nc6 6. Qe2+ Be7 7. dxc5 Nf6 8. O-O O-O 9. c3 Bxc5 10. h3 Re8 11. Qc2 Qd6) 4... c6 5. Bd3 Bd66. O-O Ne7 7. h3 h6 8. Re1 Be6 9. Nbd2 Nd7 10. Nf1 Qc7 11. c3 O-O-O 12. b4 g5)(3. Nd2 Nf6 4. e5 Nfd7 5. Bd3 (5. f4 c5 6. c3 Nc6 7. Ndf3 cxd4 8. cxd4 a5 9. Bd3(9. a4 Qb6 10. Ne2 f6) 9... Nb6 10. Ne2 Bd7 11. O-O a4 12. Ng3 (12. a3 Na5)12... g6 13. Bd2 Nb4 14. Be2 a3 15. b3 Nc8) 5... c5 6. c3 Nc6 7. Ne2 (7. Ngf3 Be7 8. O-O g5 9. dxc5 g4 10. Nd4 Ncxe5 11. Be2 (11. Bc2 Bxc5 (11... Nxc5 12. f4)12. f4 Nc6 13. Qxg4) 11... Bxc5 (11... Nxc5 12. Bxg4 Nxg4 13. Qxg4 e5 14. Nf5))7... cxd4 8. cxd4 f6 9. Nf4 (9. exf6 Nxf6) 9... Nxd4 10. Qh5+ Ke7 11. Ng6+ hxg6 12. exf6+ Nxf6 13. Qxh8 Kf7 14. Qh4 e5 15. Nf3) (3. Nc3 Nf6 4. e5 (4. Bg5 dxe4 5. Nxe4 Be7 6. Nxf6+ (6. Bxf6 gxf6 7. Nf3 a6 8. c3 (8. Bc4 b5 9. Bb3 f5 10. Ng3 c5 11. c3 c4 12. Bc2 Bb7 13. O-O h5 14. Re1 h4 15. Nf1 h3 16. g3 Qd5) (8. c4 f5 9. Nc3 Bf6 10. Qd2 c5 11. d5 O-O 12. O-O-O Bg7 13. Kb1 (13. h4 b5 14. Kb1 e5 15.cxb5 e4 16. Ng5 axb5 17. Bxb5 Qa5) 13... exd5 14. Nxd5 Nc6 15. h4 b5 16. h5 h6)(8. Qe2 f5 9. Ned2 c5 10. dxc5 (10. O-O-O cxd4 11. Nb3 Nc6 12. Nbxd4 Nxd4 13.Nxd4 Qa5) 10... Qa5) 8... f5 9. Nc5 Bxc5 10. dxc5 Qxd1+ 11. Rxd1 Ke7 12. Be2 Nd7 13. b4 a5 14. a3 axb4 15. axb4 Ra3) 6... Bxf6 7. Bxf6 Qxf6 8. Nf3 O-O 9. c3 b6)4... Ne4 5. Bd3 (5. Nce2 f6 6. f3 (6. Nf4 g6) 6... Ng5 7. Bxg5 fxg5 8. f4 c5 9.Nf3 g4 10. Nd2) (5. Nxe4 dxe4 6. Be3 (6. Bc4 a6 7. a4 (7. Ne2 b5 8. Bb3 c5 9. c3 Bb7 10. O-O Nc6) 7... b6 8. Nh3 Bb7 9. Nf4 Nc6 10. Be3 g6) 6... c5 7. Bb5+ (7.dxc5 Nd7 8. Qg4 (8. c3 Qc7 9. Qa4 Bxc5 10. Bxc5 Qxc5 11. Bb5 a6 12. Bxd7+ Bxd7 13. Qxe4 Bc6) 8... Nxc5 9. Bxc5 Bxc5 10. Qxg7 Qa5+ 11. c3 Rf8 12. b4 Bxb4) 7...Bd7) 5... Nxc3 6. bxc3 c5) 3... c5 4. c3 Nc6 5. Nf3 Bd7 6. a3 (6. Bd3 cxd4 7.cxd4 Qb6 8. O-O Nxd4 9. Nxd4 Qxd4 10. Nc3 a6) (6. Be2 Nge7 7. Na3 cxd4 8. cxd4 Nf5 9. Nc2 Qb6 10. O-O Na5 11. g4 Ne7 12. Nfe1 Bb5 13. Nd3 h5 14. gxh5 Nf5 15.Be3 Nc6 16. a4 Bc4 17. b4 Qd8 18. Bg4 Nxe3 19. fxe3 Qg5) 6... f6 7. exf6 (7. b4 fxe5 8. Nxe5 (8. dxe5 Qc7) (8. b5 Nxd4 9. cxd4 exd4) 8... Nxe5 9. dxe5 Qc7) 7...Nxf6 *";
   return render_template('Pgnviewer.html',Mypgn=pgnString)
if __name__ == '__main__':
   app.run()