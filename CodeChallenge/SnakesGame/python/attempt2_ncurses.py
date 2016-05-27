#!/usr/bin/env python
# encoding: utf-8
import curses

UP  = (-1, 0)
DOWN  = (1, 0)
RIGHT  = (0, 1)
LEFT  = (0, -1)

class Snake(object):
    def __init__(self, coordinates=None):
        self._coordinates = coordinates if coordinates is not None \
                else [(10, i) for i in xrange(3, 9)]

    def head(self):
        return self._coordinates[-1]

    def tail(self, pop=True):
        if pop:
            return self._coordinates.pop(0)
        else:
            return self._coordinates[0]

    def add_head(self, new_head):
        self._coordinates.append(new_head)
        

class Board(object):
    def __init__(self, starty=0, startx=0, leny=30, lenx=80):
        self.starty = starty
        self.startx = startx
        self.leny = leny
        self.lenx = lenx
        self.game_ended = False

        self.snake = Snake()

        self.snake_direction = RIGHT

        self.apple_location = self.place_apple()

    def next_iteration(self, direction=None):
        if direction is None:
            direction = self.snake_direction

        current_head = self.snake.head()
        new_head = (current_head[0] + self.snake_direction[0], 
                       current_head[1] + self.snake_direction[1])

        self.snake.add_head(new_head)
        current_tail = self.snake.tail(pop = True)


    def place_apple(self):
        pass

        
class BoardView(object):

    def __init__(self, board):
        self.board = board

    def __enter__(self):
        board = self.board

        curses.initscr()
        window = curses.newwin(board.leny, board.lenx, board.starty, board.startx)
        window.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        window.border()
        window.nodelay(0)

        self.window = window
        
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        key = self.window.getch()
        curses.endwin()
    
    def render(self):
        pass

if __name__ == '__main__':
    board = Board()
    with BoardView(board) as view:
        pass

#-------------------------------------------------------------------------------

def test_board():
    board = Board()
    assert board.snake._coordinates == [(10, i) for i in range(3, 9)]

    board.next_iteration()
    assert board.snake._coordinates == [(10, i) for i in range(4, 10)]


