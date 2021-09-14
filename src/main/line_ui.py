from curses import wrapper, curs_set
from time import sleep
import importlib

class LineUIApp:
	def __init__(self):
		self.win=None
		self.key=None
		self.line_size=11
		self.mod=None      
	def load_mod(self, mod_name):
		self.mod=importlib.import_module(mod_name)
	def main_loop(self, w):
		self.win=w
		self.win.nodelay(True)
		self.console=w.derwin(8, 8, 2, 2)
		curs_set(0)
		self.mod.init()
		n=0
		while True:
			k=self.safe_get_key()
			if k!="":
				self.key=k
				self.mod.on_key()
			n+=1
			if n==20:
				self.mod.on_second()
				n=0
			self.mod.on_update()
			sleep(1/20)
	def show_at(self, x, s, erase=True):
		if x<0:
			d=-x
			x=0
			s=s[d:]
		if x>=self.line_size:
			return
		last=x+len(s)
		if last>self.line_size:
			d=last-self.line_size
			s=s[:len(s)-d]
		if erase:
			self.win.erase()
		self.win.addstr(0, x, s)
		self.win.refresh()
	def show_r(self, s):
		self.show_at(self.line_size-len(s), s)
	def show_m(self, s):
		self.show_at(int(self.line_size-len(s)/2), s)
	def safe_get_key(self):
		try:
			return self.win.getkey()
		except:
			return ""
	def print(self, x):
		self.console.erase()
		self.console.addstr(3, 4, x)

line_ui_app=LineUIApp()

def show(s):
	line_ui_app.show_at(0, s)

def show_r(s):
	line_ui_app.show_r(s)

def show_m(s):
	line_ui_app.show_m(s)

def get_key():
	return line_ui_app.key

def print(x):
	line_ui_app.print(x)

def start(mod_name):
	line_ui_app.load_mod(mod_name)
	wrapper(line_ui_app.main_loop)

