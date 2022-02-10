from line_ui import *

s=0
p=0

def on_ready():
  draw("C")

def on_key():
  global s, p
  k=get_key()
  if k=="KEY_RIGHT":
    p=p+1
    s=s+1
  if s%2==0:
    look="C"
  else:
    look="c"
  draw_at(p, look)


start(globals())
