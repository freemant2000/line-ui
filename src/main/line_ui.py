from curses import wrapper, curs_set
from time import sleep
import importlib

mod=None
win=None
key=None
line_size=10

def main_func(w):
  global win
  win=w
  win.nodelay(True)
  curs_set(0)
  mod.init()
  n=0
  while True:
    k=safe_get_key()
    if k!="":
      global key
      key=k
      mod.on_key()
    n+=1
    if n==20:
      mod.on_second()
      n=0
    mod.on_update()
    sleep(1/20)

def show(s):
  show_at(0, s)

def show_r(s):
  show_at(line_size-len(s), s)

def show_at(x, s, erase=True):
  if x<0:
    d=-x
    x=0
    s=s[d:]
  if x>=line_size:
    return
  max_len=line_size-x
  if len(s)>max_len:
    s=s[:max_len]
  if erase:
    win.erase()
  win.addstr(0, x, s)
  win.refresh()

def get_key():
  return key

def safe_get_key():
  try:
    return win.getkey()
  except:
    return ""

def start(mod_name):
  global mod
  mod=importlib.import_module(mod_name)
  wrapper(main_func)

