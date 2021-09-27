from line_ui import *

x=2

def on_ready():
  draw_at(14, "A")

def on_key():
  global x
  k=get_key()
  if k=="KEY_RIGHT":
    x=x+1
    draw_at(x, "A")
  elif k=="KEY_LEFT":
    x=x-1
    draw_at(x, "A")
start(globals())
