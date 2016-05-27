#!/usr/bin/env python
# encoding: utf-8

UP  = (0, -1)
DOWN  = (0, 1)
RIGHT  = (1, 0)
LEFT  = (1, 0)

class Snake(object):
    def __init__(self, coordinates):
        self._coordinates = coordinates if coordinates is not None \
                else [(10, i) for i in xrange(3, 9)]

    def head(self):
        return self._coordinates[-1]

    def tail(self):
        return self._coordinates[0]
        

class Board(object):
    def __init__(self, starty=0, startx=0, leny=30, lenx=80):
        self._starty = starty
        self._startx = startx
        self._leny = leny
        self._lenx = lenx
        self.game_ended = False

        self.snake = Snake()

        self.snake_direction = RIGHT

        self.apple_location = self.place_apple()

    def next_iteration(self):
        pass

    def place_apple(self):
        pass

        
class BoardView(object):

    def __init__(self):
        pass

    def render(self):
        pass

#-------------------------------------------------------------------------------

def test_board():
    assert 1 == 2
