/*
 * More docu for PGNV or PgnViewerJS on:
 * https://mliebelt.github.io/PgnViewerJS/
 * https://mliebelt.github.io/PgnViewerJS/examples.html#1000
 * https://github.com/jhlywa/chess.js
 * https://github.com/lichess-org/chessground
 * 
 * */


/*
 * Initial HTML related setup 
 * Call only once
 * jquery.js and pgnv.js must be included
 */

//This is the only function to call to activate NextMoves feature
function placeNextMoveElement() {
    var newDiv = createNextMoveElement();
    var insertBeforeElement = document.getElementById("boardButton");
    var parentElement = insertBeforeElement.parentNode;

    parentElement.insertBefore(newDiv, insertBeforeElement);

    attachToClickEvents();
}

//Vytvori novy div HTML prvok, pre zobrazovanie dalsich tahov
function createNextMoveElement() {
    var newDivTextElement = document.createElement('div');
    newDivTextElement.innerHTML = "Next moves: ";

    var newDivNextMovesElement = document.createElement('div');
    newDivNextMovesElement.setAttribute('id', 'NextMoves');

    var newParentDivElement = document.createElement('div'); 
    newParentDivElement.setAttribute('style', 'margin-left: 420px ' , 'width:100px');
    newParentDivElement.appendChild(newDivTextElement);
    newParentDivElement.appendChild(newDivNextMovesElement);

    return newParentDivElement;
}

//
function attachToClickEvents() {
    //pripoj sa na udalost "click" tlacitka
    var buttonSpan = $('.buttons');
    buttonSpan.each(function () {
        $(this).parent().unbind('click').click(function (event) {
            afterMove();
        });
    });

    //pripoj sa na udalost "click" v notacii tahov
    var movesSan = $('san');
    movesSan.each(function () {
        $(this).parent().unbind('click').click(function (event) {
            afterMove();
        });
    });
}

/*
 * Vysetrovanie tahov a navigacia
 */

//Vukona sa po uskutocneni tahu: Zaborazi dalise tahy a scroll notacie
function afterMove() {
    displayNextMoves('NextMoves');
    scrollToCurrentMoveNotation();
}

//Vrati Move - objekt z pola vsetkych tahov MOVES
function getCurrentMove() {
    var currentFen = PgnViewer.base.chess.fen(); // see FEN on https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation
    var MOVES = PgnViewer.base.getPgn().getMoves();
    var currentMove = MOVES.find(x => x.fen == currentFen);
    return currentMove;

}

//Vrati pole notacii vsetkych dalsich tahov
function getVariations() {
    var currentMove = getCurrentMove();
    var MOVES = PgnViewer.base.getPgn().getMoves();
    var nextMoveMainLine = MOVES[currentMove.next];
    var nextMoves = [];
    if (nextMoveMainLine == null)
    {
        return nextMoves;
    }

    nextMoves.push(nextMoveMainLine.notation.notation);
    nextMoveMainLine.variations.forEach(variation =>
        nextMoves.push(variation.notation.notation)
    );
    return nextMoves;
}

//Analyza aktualneho tahu, zistenie dalsich tahov a ich zobrazenie
function displayNextMoves(divId) {
    var variations = getVariations();

    var divNode = document.getElementById(divId);
    divNode.innerHTML = ""
    variations.forEach(x => divNode.innerHTML += "<div><a href=\"javascript:doMove('" + x + "');\"> " + x + " </a></div>")
    divNode.innerHTML += ""
}

//Vykobaj dalsi tah
function doMove(move) {
    PgnViewer.base.manualMove(move);
    afterMove();
}

//Scroll v notacii na dany tah
function scrollToCurrentMoveNotation() {
    var currentMove = getCurrentMove();
    var moveNotation = document.getElementById('boardMoves' + currentMove.index);
    if (moveNotation != null) {
        moveNotation.scrollIntoView()
    }
}
