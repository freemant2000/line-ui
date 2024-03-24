from line_ui import *

def on_ready():
  u=get_ui()
  u.a=0

def on_second():
  u=get_ui()
  u.a=u.a+1
  print(u.a)

start()
