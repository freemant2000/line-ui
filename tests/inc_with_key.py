from line_ui import start, show, show_r, get_key

n=0

def init():
  show_r(str(n))

def on_update():
  pass

def on_second():
  global n
  n=n+1
  show_r(str(n))

def on_key():
  global n
  k=get_key()
  if k=="KEY_UP":
    n=n+1
    show_r(str(n))

start("f3")

