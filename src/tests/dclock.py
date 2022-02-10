from line_ui import *

minutes=2
seconds=59

def on_ready():
  draw(str(minutes)+":"+str(seconds))

def on_second():
  global minutes
  global seconds
  seconds=seconds+1
  if seconds==60:
    seconds=0
    minutes=minutes+1
  m=str(minutes)
  if minutes<10:
    m="0"+m
  s=str(seconds)
  if seconds<10:
    s="0"+s
  draw(m+":"+s)


start(globals())
