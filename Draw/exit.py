from time import sleep


def exitmsg(window):
    window.clear()
    h, w = window.getmaxyx()
    text = 'Thank you'
    window.addstr(h//2, w//2 - len(text)//2, text)  # Center
    window.refresh()
    sleep(1)
