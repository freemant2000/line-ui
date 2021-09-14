from line_ui import *
a=""

def on_ready():
  draw(a)

def on_second():
  global a
  a=a+"B"
  draw(a)

def on_key():
  stop()


start(globals())