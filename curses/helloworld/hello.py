#!/usr/bin/env python
# encoding: utf-8

import curses

screen = curses.initscr()

screen.addstr(0, 0, 'hello world!!!')

screen.refresh()

screen.getch()

curses.endwin()
