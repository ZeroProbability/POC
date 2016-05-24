@Grab(group='org.spockframework', module='spock-core', version='0.7-groovy-2.0')
import spock.lang.*

class GridTest extends Specification {

    def "test_main_grid"() {  
        given: 
            def grid = new Grid(xlen: 80, ylen: 20)

        when:                                           
            grid.init()
            1000.times {
                System.out.print("\033[H\033[2J");
                println grid.display()
                grid = grid.computeNextGrid()
                Thread.currentThread().sleep(200)
            }

        then:                                           
            grid.board.size() == 20
            grid.board[0].size() == 80
    }
}

class Grid {
    int xlen;
    int ylen;

    Boolean[][] board;
    def rand = new Random()

    def init() {
        board = new Boolean[ylen][xlen];
        (0..(ylen-1)).each { y ->
            (0..(xlen-1)).each {  x ->
                board[y][x] = rand.nextBoolean()
            }
        }
    }

    def display() {
        board.collect { row ->
            row.collect { cell ->
                if(cell) return '*' else ' ';
            }.join('');
        }.join('\n')
    }

    def computeNextGrid() {
        def new_board = new Boolean[ylen][xlen];

        (0..(ylen-1)).each { y ->
            (0..(xlen-1)).each {  x ->
                new_board[y][x] = find_next_gen_for_cell(y, x)
            }
        }
        return new Grid(xlen: xlen, ylen: ylen, board: new_board)

    }

    def find_next_gen_for_cell(def y, def x) {
        def min_x, min_y, max_x, max_y;
        if(x==0) min_x = 0 
            else min_x = x-1;
        if(y==0) min_y = 0
            else min_y = y-1;
        if(x==xlen-1) max_x = xlen-1
            else max_x = x+1;
        if(y==ylen-1) max_y = ylen-1
            else max_y = y+1;

        def sum=0
        ((min_y)..(max_y)).each { yn ->
            ((min_x)..(max_x)).each { xn ->
                if(xn == x && yn == y) {
                    // nothing
                } else {
                    if(board[yn][xn]) sum+=1
                }
            }
        }
        if(sum == 3) {
            return true;
        }
        if(board[y][x] && sum==2) {
            return true;
        }
        return false;

    }

}
