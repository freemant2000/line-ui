from line_ui import start, show_r, get_key, show_m, print

n=0

def init():
  show_m(str(n))

def on_update():
  pass

def on_second():
  global n
  n=n+1
  #show_r(str(n))
  #print("hi")

def on_key():
  global n
  k=get_key()
  if k=="KEY_UP":
    n=n+1
    #show_r(str(n))
    print("hi")

start("inc_with_key")

