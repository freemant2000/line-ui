import curses

def f1(screen):
    screen.addstr(0, 79, "y")
    box1 = screen.derwin(1, 3, 0, 0)
    box1.addstr(0, 0, "x")
    box1.addstr(0, 1, "y")
    box1.insstr(0, 2, "z")
    screen.getch()

curses.wrapper(f1)