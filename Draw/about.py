def printabout(window):
    window.clear()
    h, w = window.getmaxyx()
    msg = 'Terminal Drawing App'
    window.addstr(4, w//2-len(msg)//2, msg)  # Center
    msg = """
Usage:

    Click using mouse to paint
    Use arrow keys to change color
    Press ESC for main menu
"""
    height, width = window.getmaxyx()
    no_lines = msg.count('\n')
    starty = height//2 - no_lines//2
    startx = width//2 - max([len(_) for _ in msg.split('\n')])//2

    for index, m in enumerate(msg.split('\n')):
        window.addstr(starty+index, startx, m)

    window.refresh()
    while window.getch() != 27:  # Wait till ESC pressed
        pass
