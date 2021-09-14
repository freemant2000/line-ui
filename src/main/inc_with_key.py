from line_ui import *

n=0

def on_ready():
  show_r(str(n))

def on_update():
  pass

def on_second():
  global n
  n=n+1
  show_r(str(n))
  print("got dddde "+str(n))


def on_key():
  global n
  k=get_key()
  if k=="KEY_UP":
    n=n+1
    show_r(str(n))

start("inc_with_key")

