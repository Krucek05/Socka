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

function createNextMoveElement() {
    var newDivTextElement = document.createElement('div');
    newDivTextElement.innerHTML = "Next moves: ";

    var newDivNextMovesElement = document.createElement('div');
    newDivNextMovesElement.setAttribute('id', 'NextMoves');

    var newParentDivElement = document.createElement('div'); 
    //newParentDivElement.setAttribute('style', 'grid-row:4; place-self: left; display: flex');
    newParentDivElement.setAttribute('style', 'margin-left: 420px ' , 'width:100px');
    newParentDivElement.appendChild(newDivTextElement);
    newParentDivElement.appendChild(newDivNextMovesElement);

    return newParentDivElement;
}

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
 * Moves investigation and navigation
 */

function afterMove() {
    displayNextMoves('NextMoves');
    scrollToCurrentMoveNotation();
}

function getCurrentMove() {
    var MOVES = PgnViewer.base.getPgn().getMoves();
    var currentFen = PgnViewer.base.chess.fen(); // see FEN on https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation
    var currentMove = MOVES.find(x => x.fen == currentFen);
    return currentMove;

}

function getVariations() {
    var currentMove = getCurrentMove();
    var MOVES = PgnViewer.base.getPgn().getMoves();
    var nextMove = MOVES[currentMove.next];
    var nextMoves = [];
    if (nextMove == null)
    {
        return nextMoves;
    }

    nextMoves.push(nextMove.notation.notation);
    nextMove.variations.forEach(variation =>
        nextMoves.push(variation.notation.notation)
    );
    return nextMoves;
}

function displayNextMoves(divId) {
    var variations = getVariations();

    var divNode = document.getElementById(divId);
    divNode.innerHTML = ""
    variations.forEach(x => divNode.innerHTML += "<div><a href=\"javascript:doMove('" + x + "');\"> " + x + " </a></div>")
    divNode.innerHTML += ""
}

function doMove(move) {
    PgnViewer.base.manualMove(move);
    afterMove();
}

function scrollToCurrentMoveNotation() {
    var currentMove = getCurrentMove();
    var moveNotation = document.getElementById('ChessBoardMoves' + currentMove.index);
    if (moveNotation != null) {
        moveNotation.scrollIntoView()
    }
}
