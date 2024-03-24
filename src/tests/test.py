from line_ui import *

a=5
c=1

def on_ready():
  w=get_ui()
  w.a=2
  print(a)

def on_second():
  global a
  a=a+c
  print(a)

def on_key():
  global c
  c=2
  w=get_ui()
  print(w.a)
  
start()
