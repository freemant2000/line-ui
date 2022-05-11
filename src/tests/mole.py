from line_ui import *
from random import randint

def on_ready():
  schedule(0.3, f1)

a=0
def f1():
  global a
  erase()
  a=randint(0, 3)
  draw_at(a, "B")
  draw_r(str(score))
  schedule(0.8, f1)

score=0

def on_key():
  global score
  k=get_key()
  if (k=="a" and a==0) or (k=="s" and a==1) or (k=="d" and a==2) or (k=="f" and a==3):
    score=score+1
    draw_r(str(score))
    draw_at(a, " ")    
    beep()
  else:
    score=score-1
    draw_r(str(score))

start()
