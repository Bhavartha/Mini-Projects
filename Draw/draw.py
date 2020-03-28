import curses
from curses import textpad


block = u"\u2588"
opt2color = {
    'White': 1,
    'Red': 2,
    'Magenta': 3,
    'Green': 4,
    'Cyan': 5,
    'Blue': 6,
    'Yellow': 7,
    'Black': 99,
}
options = list(opt2color.keys())


def disp_options(window, selected):
    height, width = window.getmaxyx()
    x = 1
    y = height//2-len(opt2color)
    for index, o in enumerate(options):
        if o == selected:
            window.attron(curses.color_pair(99))
            window.addstr(y+index, x, o)
            window.attroff(curses.color_pair(99))
            window.addstr(0, width//2-5, 'Color: ')
            window.attron(curses.color_pair(opt2color[selected]))
            window.addstr(0, width//2+2, block*3)
            window.attroff(curses.color_pair(opt2color[selected]))
        else:
            window.addstr(y+index, x, o)


def update_selected(selected, value):
    return options[(options.index(selected)+value) % len(options)]


def draw(window):
    window.clear()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)
    curses.init_pair(2, curses.COLOR_RED, -1)
    curses.init_pair(3, curses.COLOR_MAGENTA, -1)
    curses.init_pair(4, curses.COLOR_GREEN, -1)
    curses.init_pair(5, curses.COLOR_CYAN, -1)
    curses.init_pair(6, curses.COLOR_BLUE, -1)
    curses.init_pair(7, curses.COLOR_YELLOW, -1)
    curses.mousemask(1)
    curses.curs_set(0)
    height, width = window.getmaxyx()
    box = [[1, 10], [height-2, width-3]]
    textpad.rectangle(window, box[0][0], box[0][1], box[1][0], box[1][1])
    opt_selected = 'White'
    window.attron(curses.color_pair(opt2color[opt_selected]))
    for y in range(box[0][0]+1, box[1][0]):
        for x in range(box[0][1]+1, box[1][1]):
            window.addstr(y, x, block)
    window.attroff(curses.color_pair(opt2color[opt_selected]))

    window.refresh()
    while True:
        disp_options(window, opt_selected)
        key = window.getch()
        if key == 27:
            break
        elif key == curses.KEY_DOWN:
            opt_selected = update_selected(opt_selected, 1)
        elif key == curses.KEY_UP:
            opt_selected = update_selected(opt_selected, -1)
        elif key == curses.KEY_MOUSE:
            _, x, y, _, _ = curses.getmouse()
            if x <= box[0][1] or x >= box[1][1] or y <= box[0][0] or y >= box[1][0]:
                continue
            window.attron(curses.color_pair(opt2color[opt_selected]))
            window.addstr(y, x, block)
            window.attroff(curses.color_pair(opt2color[opt_selected]))
        window.refresh()
