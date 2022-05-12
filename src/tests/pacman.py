from line_ui import *

x=2
s=0

def on_ready():
  draw_at(14, "C")

def on_key():
  global x, s
  k=get_key()
  if k=="KEY_RIGHT":
    x=x+1
    s=s+1
    erase()
    if s%2==0:
      look="C"
    else:
      look="c"
    draw_at(x, look)
  elif k=="KEY_LEFT":
    x=x-1
    erase()
    draw_at(x, "A")
start()
