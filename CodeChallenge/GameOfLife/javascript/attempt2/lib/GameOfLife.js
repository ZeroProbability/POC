/*jslint browser:true */

function GameOfLife(board) {
    this.board = board;
    this.leny = board.length;
    this.lenx = board[0].length;
}

GameOfLife.prototype.computeNextGen = function(yi, xi) {
    var neighboursCount=0;
    var xmin, ymin, xmax, ymax;
    var x, y;

    if(xi == 0) { xmin = 0; } else { xmin = xi - 1; }
    if(xi == (this.lenx - 1)) { xmax = this.lenx - 1; } else { xmax = xi + 1; }
    if(yi == 0) { ymin = 0; } else { ymin = yi - 1; }
    if(yi == (this.leny - 1)) { ymax = this.leny - 1; } else { ymax = yi + 1; }

    for (y = ymin; y <= ymax; y++) {
        for (x = xmin; x <= xmax; x++) {
            if(this.board[y][x]) {
                neighboursCount++;
            }
        }
    }

    if(this.board[yi][xi]) { neighboursCount--; };

    if(this.board[yi][xi] ) {
        return (neighboursCount == 2 || neighboursCount == 3);
    } else {
        return (neighboursCount == 3);
    }

};

GameOfLife.prototype.computeNextBoard = function() {
    var x, y;
    var newGrid = [];
    var newRow = [];

    for (y = 0; y < this.leny; y++) {
        newRow = [];
        for (x = 0; x < this.lenx; x++) {
            newRow.push(this.computeNextGen(y, x));
        }
        newGrid.push(newRow);
    }

    return newGrid;

};


module.exports = GameOfLife;
