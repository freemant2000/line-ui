from line_ui import *

a=5
c=1

def on_ready():
  print(a)

def on_second():
  global a
  a=a+c
  print(a)

def on_key():
  global c
  c=2
  
start()
