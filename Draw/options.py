import curses

from exit import *
from about import *
from draw import *


menu = [' Draw ', ' How to use ', ' Quit ']


def printmenu(window, selected):
    window.clear()
    height, width = window.getmaxyx()
    for n, m in enumerate(menu):
        x = width//2 - len(m)//2
        y = height//2 - len(menu)//2 + n
        if selected == n:
            window.attron(curses.color_pair(99))
            window.addstr(y, x, m)
            window.attroff(curses.color_pair(99))
        else:
            window.addstr(y, x, m)
    window.refresh()


def options(window):
    curses.init_pair(99, curses.COLOR_BLACK, curses.COLOR_WHITE)
    selected = 0
    while True:
        printmenu(window, selected)
        key = window.getch()
        if key == curses.KEY_UP:
            selected = (selected-1) % len(menu)
        elif key == curses.KEY_DOWN:
            selected = (selected+1) % len(menu)
        elif key == curses.KEY_ENTER or key in (10, 13):
            if selected == 2:  # Quit
                exitmsg(window)
                break
            elif selected == 1:  # Info
                printabout(window)
            else:
                draw(window)
