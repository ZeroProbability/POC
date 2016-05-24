/*jslint browser:true */

var gol = {
    xlen: 0,
    ylen: 0,
    grid: [], // this will be a 2d array of xlen x ylen

    init_game: function() {
        var x_width= 5;
        var y_width= 5;
        var c = document.getElementById("myCanvas");
        var ctx = c.getContext("2d");
        this.ctx = ctx;

        this.ctx.fillStyle = "#FF0000";
        this.xlen = Math.floor( this.ctx.canvas.width / x_width );
        this.ylen = Math.floor( this.ctx.canvas.height / y_width );
    },

    clear_canvas: function() {
        this.ctx.clearRect(0, 0, this.ctx.canvas.width, this.ctx.canvas.height);
    },

    mark_live : function (x, y) {
        var x_width= 5;
        var y_width= 5;
        var x_start = x * x_width;
        var y_start = y * y_width;

        this.ctx.fillRect(x_start, y_start, x_width, y_width);
    },

    init_random: function() {
        var x,y;
        var row;
        for (y = 0; y < this.ylen; y++) {
            row = [];
            for (x = 0; x < this.xlen; x++) {
                row.push(Math.floor(Math.random()*2));
            }
            this.grid.push(row);
        }
    },

    draw_grid: function() {
        var x,y;
        this.clear_canvas();
        for (y = 0; y < this.ylen; y++) {
            for (x = 0; x < this.xlen; x++) {
                if(this.grid[y][x] === 1) {
                    this.mark_live(x, y);
                }
            }
        }
    },

    compute_next_grid: function() {
        var x,y;
        var new_grid = [];
        var new_row = [];
        var owner = this;
        function compute_next_cell_gen(x, y) {
            var xmin, xmax, ymin, ymax;
            var x1, y1;
            var total_live_neighbours=0;
            if(x === 0) { xmin = 0; } else { xmin = x - 1;} 
            if(y === 0) { ymin = 0; } else { ymin = y -1; }
            if(x === owner.xlen-1) { xmax = owner.xlen-1; } else { xmax = x + 1; }
            if(y === owner.ylen-1) { ymax = owner.ylen-1; } else { ymax = y + 1; }

            for(x1=xmin; x1 < xmax+1; x1++) {
                for(y1=ymin; y1 < ymax+1; y1++) {
                    try {
                        total_live_neighbours += owner.grid[y1][x1];
                    } catch(err) {
                        console.log(x1, y1);
                    }
                }
            }

            total_live_neighbours -= owner.grid[y][x];

            if(total_live_neighbours === 3) {
                return 1;
            }
            if(owner.grid[y][x] === 1 ) { // is live 
                if(total_live_neighbours === 2) { 
                    return 1;
                }
                return 0;
            } 
            return 0;
        }

        for (y = 0; y < this.ylen; y++) {
            new_row = [];
            for (x = 0; x < this.xlen; x++) {
                new_row.push(compute_next_cell_gen(x, y));
            }
            new_grid.push(new_row);
        }

        this.grid = new_grid;

    }


};

gol.init_game();
gol.init_random();
function main_loop() {
    gol.draw_grid();
    gol.compute_next_grid();
    setTimeout(function() { main_loop() ; }, 100);
}

main_loop();
