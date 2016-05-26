#!/usr/bin/env python
# encoding: utf-8

import curses
import random

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

class Board(object):
    def __init__(self, beginx=0, beginy=0, width=80, height=30):
        self._beginx = beginx
        self._beginy = beginy
        self._width = width
        self._height = height
        self._score = 0

    def __enter__(self):
        curses.initscr()                        
        win = curses.newwin(self._height, self._width, self._beginy, self._beginx)       
               # height, width, top, left       
        win.keypad(1)                           
        curses.noecho()                         
        curses.curs_set(0)                      
        win.border()                            
        win.nodelay(1)                          
        self._win = win
        self._game_over = False
        return self

    def __exit__(self, *args):
        key = self._win.getch()                       
        curses.endwin()

    def is_game_over(self):
        return self._game_over

    def draw_char(self, y, x, char):
        self._win.addch(y, x, char)

    def getch(self):
        return self._win.getch()

    def place_apple(self, snake_cordinates):
        x = random.randint(1, self._width-2)
        y = random.randint(1, self._height-2)

        self._apple = (y, x)

        self.draw_char(y, x, '*')

    def is_apple(self, y, x):
        return self._apple[0] == y and self._apple[1] == x

    def display_score(self, increment=False):
        if increment:
            self._score += 1 
        self._win.addstr(0, 3, "Score : %5d"%self._score)

    def endgame(self):
        self._win.addstr(3, 3, "Game over!!")
        self._game_over = True

class Snake(object):
    def __init__(self, board):
        self._cordinates = [(10,3), (10,4), (10,5), (10, 6), (10, 7), (10, 8)]
        self._cordinates
        self._direction = RIGHT
        self._board = board

    def move(self):
        if self._board._game_over:
            return

        head = list(self._cordinates[-1])
        head[0] += self._direction[0]
        head[1] += self._direction[1]

        if head[0] in (self._board._beginy, self._board._beginy + self._board._height - 1)  \
            or head[1] in ( self._board._beginx, self._board._beginx + self._board._width - 1) \
            or tuple(head) in self._cordinates:
                self._board.endgame()
                return 

        self._cordinates.append(tuple(head))
        self._board.draw_char(head[0], head[1], '#')
        if self._board.is_apple(head[0], head[1]):
            self._board.place_apple(self._cordinates)
            self._board.display_score(increment=True)
        else:
            tail = self._cordinates.pop(0)
            self._board.draw_char(tail[0], tail[1], ' ')

    def draw(self):
        for c in self._cordinates:
            self._board.draw_char(c[0], c[1], '#')

    def change_direction(self, key):
        if key == curses.KEY_LEFT and not self._direction == RIGHT:
            self._direction = LEFT
        elif key == curses.KEY_RIGHT and not self._direction == LEFT:
            self._direction = RIGHT
        elif key == curses.KEY_UP and not self._direction == DOWN:
            self._direction = UP
        elif key == curses.KEY_DOWN and not self._direction == UP:
            self._direction = DOWN
        else:
            pass

if __name__ == '__main__':
    final_score = 0
    with Board() as b:
        snake = Snake(b)
        snake.draw()
        b.place_apple(snake._cordinates)
        b.display_score()
        while True:
            snake.move()
            user_key = b.getch()
            snake.change_direction(user_key)
            import time; time.sleep(0.1)
            if b.is_game_over():
                final_score = b._score
                break

    print "Your score was ", final_score
