/*jslint browser:true */

function GameOfLife(board) {
    this.board = board;
    this.leny = board.length;
    this.lenx = board[0].length;
}

GameOfLife.prototype.compute_next_board = function() {
    var x, y;
    for (y = 0; y < this.leny; y++) {
        for (x = 0; x < this.lenx; x++) {
            console.log("info");
        }
    }

};
