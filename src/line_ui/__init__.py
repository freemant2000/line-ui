from curses import wrapper, curs_set
import curses
from time import sleep


class LineUIApp:
    FRAMES_PER_SECOND = 20

    def __init__(self):
        self.line_pane_c = None
        self.console_c = None
        self.key = None
        self.line_size = 11
        self.console_height = 5
        self.console_lines = []
        self.sched_count = -1
        self.mod = None

    def print(self, x):
        self.console_lines.append(str(x))
        while len(self.console_lines) > self.console_height:
            self.console_lines.pop(0)
        self.console_c.erase()
        for i in range(len(self.console_lines)):
            s = self.console_lines[i]
            if len(s) > self.line_size:
                s = s[: self.line_size]
            LineUIApp.safe_addstr(self.console_c, i, 0, s)
        self.console_c.refresh()

    def init_line_pane(self):
        line_pane = self.scr.derwin(3, self.line_size + 2, 0, 0)
        line_pane.border()
        line_pane.refresh()
        self.line_pane_c = line_pane.derwin(1, self.line_size, 1, 1)

    def init_console(self):
        console = self.scr.derwin(
            self.console_height + 2, self.line_size + 2, 3, 0)
        console.border()
        console.refresh()
        self.console_c = console.derwin(
            self.console_height, self.line_size, 1, 1)

    @staticmethod
    def safe_addstr(win, y, x, s):
        h, w = win.getmaxyx()
        if y == h - 1 and x + len(s) == w:
            win.insstr(y, x, s)
        else:
            win.addstr(y, x, s)

    def main_loop(self, scr):
        self.scr = scr
        self.scr.nodelay(True)
        self.init_line_pane()
        self.init_console()
        curs_set(0)
        self.call_handler("on_ready")
        self.done = False
        n = 0
        while not self.done:
            k = self.safe_get_key()
            if k != "":
                self.key = k
                self.call_handler("on_key")
            n += 1
            if n == LineUIApp.FRAMES_PER_SECOND:
                self.call_handler("on_second")
                n = 0
            if self.sched_count >= 0:
                if self.sched_count == 0:
                    self.call_handler(self.sched_handler_name)
                self.sched_count -= 1
            self.call_handler("on_update")
            sleep(1 / LineUIApp.FRAMES_PER_SECOND)

    def call_handler(self, handler_name):
        if isinstance(handler_name, str):
            h = self.mod.get(handler_name)
        elif callable(handler_name):  # actually a func?
            h = handler_name
        else:
            raise ValueError("a handler name or function is required")
        if h:
            h()

    def schedule(self, seconds, handler_name):
        if self.sched_count > 0:
            raise RuntimeError("At most one task can be scheduled")
        self.sched_count = int(seconds*LineUIApp.FRAMES_PER_SECOND)
        self.sched_handler_name = handler_name

    def stop(self):
        self.done = True

    def draw_at(self, x, s, erase=True):
        if erase:
            self.line_pane_c.erase()
            self.line_pane_c.refresh()
        if x < 0:
            d = -x
            x = 0
            if d >= len(s):
                return
            s = s[d:]
        if x >= self.line_size:
            return
        last = x + len(s)
        if last > self.line_size:
            d = last - self.line_size
            s = s[: len(s) - d]
        LineUIApp.safe_addstr(self.line_pane_c, 0, x, s)
        self.line_pane_c.refresh()

    def draw_r(self, s, erase=True):
        self.draw_at(self.line_size - len(s), s, erase)

    def draw_m(self, s, erase=True):
        self.draw_at(int((self.line_size - len(s)) / 2), s, erase)

    def safe_get_key(self):
        try:
            k = self.scr.getkey()
            if k == "\n":
                k = "ENTER"
            return k
        except:
            return ""


line_ui_app = LineUIApp()


def draw(s, erase=True):
    draw_l(s, erase)


def draw_at(x, s, erase=True):
    line_ui_app.draw_at(x, s, erase)


def draw_l(s, erase=True):
    line_ui_app.draw_at(0, s, erase)


def draw_r(s, erase=True):
    line_ui_app.draw_r(s, erase)


def draw_m(s, erase=True):
    line_ui_app.draw_m(s, erase)


def get_key():
    return line_ui_app.key


def print(x):
    line_ui_app.print(x)


def schedule(seconds, handler_name):
    line_ui_app.schedule(seconds, handler_name)


def beep():
    curses.beep()


def stop():
    line_ui_app.stop()


def start(mod):
    line_ui_app.mod = mod
    wrapper(line_ui_app.main_loop)
