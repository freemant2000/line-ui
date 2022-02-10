from line_ui import *

a=0

def on_ready():
  schedule(0.8, f1)

def f1():
  global a
  if a==0:
    draw_at(5, ".")
  elif a==2:
    draw_at(5, "!")
  else:
    draw_at(5, ":")
  a=a+1
  if a==4:
    a=0
  schedule(0.8, f1)

start(globals())
