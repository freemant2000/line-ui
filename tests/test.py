from line_ui.core import *

a=""

def on_ready():
  draw(a)

def on_key():
  global a
  b=get_key()
  if b=="ENTER":
    draw(str(int(a)*2))
  else:
    a=a+b
    draw(a)

start(globals())