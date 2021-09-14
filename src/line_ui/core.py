from curses import wrapper, curs_set
from time import sleep
import importlib


class LineUIApp:
    def __init__(self):
        self.line_pane_c = None
        self.console_c = None
        self.key = None
        self.line_size = 11
        self.console_height = 5
        self.console_lines = []
        self.mod = None

    def load_mod(self, mod_name):
        self.mod = importlib.import_module(mod_name)

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
        console = self.scr.derwin(self.console_height + 2, self.line_size + 2, 3, 0)
        console.border()
        console.refresh()
        self.console_c = console.derwin(self.console_height, self.line_size, 1, 1)

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
        self.done=False
        n = 0
        while not self.done:
            k = self.safe_get_key()
            if k != "":
                self.key = k
                self.call_handler("on_key")
            n += 1
            if n == 20:
                self.call_handler("on_second")
                n = 0
            self.call_handler("on_update")
            sleep(1 / 20)

    def call_handler(self, handler_name):
      h=self.mod.get(handler_name)
      if h:
        h()

    def stop(self):
      self.done=True

    def draw_at(self, x, s, erase=True):
        if x < 0:
            d = -x
            x = 0
            s = s[d:]
        if x >= self.line_size:
            return
        last = x + len(s)
        if last > self.line_size:
            d = last - self.line_size
            s = s[: len(s) - d]
        if erase:
            self.line_pane_c.erase()
        LineUIApp.safe_addstr(self.line_pane_c, 0, x, s)
        self.line_pane_c.refresh()

    def draw_r(self, s):
        self.draw_at(self.line_size - len(s), s)

    def draw_m(self, s):
        self.draw_at(int((self.line_size - len(s)) / 2), s)

    def safe_get_key(self):
        try:
            k=self.scr.getkey()
            if k=="\n":
              k="ENTER"
            return k
        except:
            return ""

line_ui_app = LineUIApp()

def draw(s):
    line_ui_app.draw_at(0, s)

def draw_at(x, s):
    line_ui_app.draw_at(x, s)

def draw_r(s):
    line_ui_app.draw_r(s)

def draw_m(s):
    line_ui_app.draw_m(s)

def get_key():
    return line_ui_app.key

def print(x):
    line_ui_app.print(x)

def stop():
    line_ui_app.stop()

def start(mod):
    line_ui_app.mod=mod
    wrapper(line_ui_app.main_loop)
