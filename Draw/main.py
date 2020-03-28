import curses
from options import *


def main(window):
    art = r"""
$$$$$$$\
$$  __$$\
$$ |  $$ |$$$$$$\ $$$$$$\ $$\  $$\  $$\
$$ |  $$ $$  __$$\\____$$\$$ | $$ | $$ |
$$ |  $$ $$ |  \__$$$$$$$ $$ | $$ | $$ |
$$ |  $$ $$ |    $$  __$$ $$ | $$ | $$ |
$$$$$$$  $$ |    \$$$$$$$ \$$$$$\$$$$  |
\_______/\__|     \_______|\_____\____/
"""
    curses.curs_set(0)
    window.clear()
    height, width = window.getmaxyx()
    no_lines = art.count('\n')
    starty = height//2 - no_lines//2 - 4
    startx = width//2 - max([len(_) for _ in art.split('\n')])//2

    for index, msg in enumerate(art.split('\n')):
        window.addstr(starty+index, startx, msg)
    msg = 'Press any key to continue'
    window.addstr(height//2+no_lines//2, width//2-len(msg)//2, msg)
    window.refresh()

    window.getch()
    return options(window)


curses.wrapper(main)
