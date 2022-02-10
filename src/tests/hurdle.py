from line_ui import *
from random import randint

a=0

def print_ch(a):
  if a==0:
    draw_at(5, " ")
  elif a==1 or a==5:
    draw_at(5, ".")
  elif a==2 or a==4:
    draw_at(5, ":")
  elif a==3:
    draw_at(5, "!")

c=0.5

x=2
def on_key():
  global x
  k=get_key()
  if k=="KEY_RIGHT":
    x=x+1
    if x>10:
      x=0
      print("win")
      beep()
    draw_all()
  elif k=="KEY_LEFT" and x>0:
    x=x-1
    draw_all()

def on_ready():
  print_ch(a)
  draw_at(x, "A")
  schedule(c, f1)
def f1():
  global a
  global c
  a=a+1
  if a>5:
    a=0
  print_ch(a)
  if a==3:
    c=0.1*randint(3, 8)
  schedule(c, f1)

def draw_all():
  erase()
  print_ch(a)
  draw_at(x, "A")
  if x==5 and a>0:
    print("loss")
    beep()

start(globals())
