#!/usr/bin/env python
# encoding: utf-8
import curses

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

class Snake(object):

    def __init__(self, coordinates=None):
        self.coordinates = coordinates if coordinates is not None \
                else [(10, i) for i in xrange(3, 7)]


    def add_head(self, direction):
        current_head = self.coordinates[-1]
        new_head = (current_head[0] + direction[0], 
                current_head[1] + direction[1])
        self.coordinates.append(new_head)
        return new_head

    def pop_tail(self):
        return self.coordinates.pop(0)


class Board(object):

    def __init__(self, starty = 0, startx = 0, leny = 30, lenx = 80):
        self.startx, self.starty, self.lenx, self.leny = \
                startx, starty, lenx, leny

        self.snake = Snake()
        self.snake_direction = RIGHT

    def move_snake(self):
        self.snake.add_head(self.snake_direction)
        self.snake.pop_tail()

    def change_direction(self, new_direction):
        self.snake_direction = new_direction


class BoardView(object):

    def __init__(self, board):
        self.board = board

    def render(self):
        curses.initscr()
        win = curses.newwin(20, 60, 0, 0)
        win.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        win.border()
        win.nodelay(0)
        key = win.getch()
        curses.endwin()

#--------------------------------------------------------------------------------

def test_board():
    board = Board()
    assert board.snake.coordinates == [(10, 3), (10, 4), (10, 5), (10, 6)]

    board.move_snake()
    assert board.snake.coordinates == [(10, 4), (10, 5), (10, 6), (10, 7)]

    board.change_direction(UP)
    board.move_snake()
    assert board.snake.coordinates == [(10, 5), (10, 6), (10, 7), (9, 7)]


