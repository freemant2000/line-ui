from line_ui import *
from random import randint

x=5
c=1
a=0
d=randint(3, 5)*0.1

def draw_all():
  if a==0:
    draw_at(10, ".")
  else:
    draw_at(10, "!")
  draw_at(x, "A")

def on_ready():
  draw_all()
  schedule(d, f1)

def f1():
  global x
  global c
  global d
  erase()
  if x==0 and c<0:
    c=1
  if x==9 and c>0 and a==1:
    c=-1
  if x==9 and c>0 and a==0:
    print("loss")
    x=-1
  x=x+c
  if x==0:
    d=randint(3, 5)*0.1
  draw_all()
  schedule(d, f1)

def on_key():
  global a
  k=get_key()
  if k=="KEY_UP":
    if a==1:
      print("loss")
    else:
      a=1
      draw_all()
      schedule(1, f2)

def f2():
  global a
  a=0
  draw_all()

start()
