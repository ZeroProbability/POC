#!/usr/bin/env python
# encoding: utf-8
import curses
import time
import random

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

class GameOver(Exception):
    pass

class Snake(object):

    def __init__(self, coordinates=None, default_length=4):
        self.coordinates = coordinates if coordinates is not None \
                else [(10, i) for i in xrange(3, 3+default_length)]


    def add_head(self, direction):
        current_head = self.coordinates[-1]
        new_head = (current_head[0] + direction[0], 
                current_head[1] + direction[1])
        self.coordinates.append(new_head)
        return new_head

    def pop_tail(self):
        return self.coordinates.pop(0)

    def set_head(self, loc):
        self.coordinates.pop()  # previous head
        self.coordinates.append(loc)

class Board(object):

    def __init__(self, starty = 0, startx = 0, leny = 30, lenx = 80, default_length=4):
        self.startx, self.starty, self.lenx, self.leny = \
                startx, starty, lenx, leny

        self.snake = Snake(default_length=default_length)
        self.snake_direction = RIGHT
        self.place_apple_at_random()
        self.score = 0

    def move_snake(self):
        new_head = self.snake.add_head(self.snake_direction)

        if new_head in self.snake.coordinates[:-1]:
            raise GameOver("GameOver: Your score was {}".format(self.score))

        if new_head[0] == self.starty:
            self.snake.set_head((self.starty + self.leny -2, new_head[1]))
        elif new_head[0] == self.starty + self.leny - 1:
            self.snake.set_head((self.starty + 1, new_head[1]))
        if new_head[1] == self.startx:
            self.snake.set_head((new_head[0], self.startx + self.lenx -2))
        elif new_head[1] == self.startx + self.lenx - 1:
            self.snake.set_head((new_head[0], self.startx + 1))

        if new_head == self.apple_location:
            self.place_apple_at_random()
            self.score += 1
        else:
            self.snake.pop_tail()

    def change_direction(self, new_direction):
        self.snake_direction = new_direction

    def place_apple_at_random(self):
        all_coordinates = set([])
        for y in xrange(self.starty + 1, self.starty + self.leny - 2):
            for x in xrange(self.startx + 1, self.startx + self.lenx -2):
                all_coordinates.add((y, x))

        all_coordinates.difference_update(self.snake.coordinates)

        random_location = random.sample(all_coordinates, 1)[0]

        self.place_apple_at(random_location[0], random_location[1])

    def place_apple_at(self, y, x):
        self.apple_location = (y, x)


class BoardView(object):

    def __init__(self, board):
        self.board = board

    def __enter__(self):
        curses.initscr()
        window = curses.newwin(self.board.leny, self.board.lenx, 
                self.board.starty, self.board.startx)
        window.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        window.border()
        window.nodelay(1)

        self.window = window

        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        curses.endwin()


    def render(self):
        self.window.erase()
        self.window.border()
        for c in self.board.snake.coordinates:
            self.window.addch(c[0], c[1], '#')

        self.window.addch(self.board.apple_location[0], 
                self.board.apple_location[1], '*')

        self.window.addstr(0, 3, ' Score : %5d '%(self.board.score))

    def handle_key(self, key):
        self.window.addstr( 3, 3, str(key))
        if key == curses.KEY_UP and not board.snake_direction == DOWN:
            board.change_direction(UP)
        elif key == curses.KEY_DOWN and not board.snake_direction == UP:
            board.change_direction(DOWN)
        elif key == curses.KEY_RIGHT and not board.snake_direction == LEFT:
            board.change_direction(RIGHT)
        elif key == curses.KEY_LEFT and not board.snake_direction == RIGHT:
            board.change_direction(LEFT)
        else:
            pass # just ignore

if __name__ == '__main__':
    board = Board(default_length=20)

    try:
        with BoardView(board) as view:
            view.render()

            while True:
                time.sleep(0.10)
                key = view.window.getch()
                view.handle_key(key)
                board.move_snake()
                view.render()
    except GameOver as g:
        print g.message


#--------------------------------------------------------------------------------

def test_board():
    board = Board()
    board.place_apple_at(1,1)

    assert board.snake.coordinates == [(10, 3), (10, 4), (10, 5), (10, 6)]

    board.move_snake()
    assert board.snake.coordinates == [(10, 4), (10, 5), (10, 6), (10, 7)]

    board.change_direction(UP)
    board.move_snake()
    assert board.snake.coordinates == [(10, 5), (10, 6), (10, 7), (9, 7)]

    board.place_apple_at(8, 7)
    board.move_snake()
    assert board.snake.coordinates == [(10, 5), (10, 6), (10, 7), (9, 7), (8, 7)]
    assert not board.apple_location == (8, 7)

    board.snake.coordinates = [(2, 30), (1, 30)]
    board.change_direction(UP)
    board.move_snake()

    assert board.snake.coordinates == [(1, 30), (28, 30)]

    board.snake.coordinates = [(27, 30), (28, 30)]
    board.change_direction(DOWN)
    board.move_snake()

    assert board.snake.coordinates == [(28, 30), (1, 30)]

