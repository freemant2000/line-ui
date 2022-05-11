from line_ui import *
from random import randint

a=0
b=""

def on_ready():
  draw(str(a))
  draw_r(b)
  schedule(0.8, "f1")

def on_key():
  global a, b
  k=get_key()
  if k=="KEY_IC":
    if a==9:
      a=0
    else:
      a=a+1
    draw(str(a))
  elif k=="KEY_DC":
    b=b.replace(str(a), "", 1)
    erase()
    draw(str(a))
    draw_r(b)

def f1():
  global b
  b=b+str(randint(0, 9))
  if len(b)==11:
    quit()
  draw_r(b)
  schedule(0.8, "f1")

start(globals())
