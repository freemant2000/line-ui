from line_ui import *

def on_ready():
  draw_r("Hi")
  schedule(1, on_sched)

def on_sched():
  draw_r("Hello")
  schedule(1, on_sched2)

def on_sched2():
  draw_r("Heee")
  schedule(1, on_sched)


def on_update():
  pass


start(globals())

