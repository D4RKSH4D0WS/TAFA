# fbparser
# i made this for tafa
# you can also use it
# coded by: salism3
# start: 08-04-2020 10:50

from .exception import *
from . import parsing
from . import sorting

class Output:
	def __init__(self, items = None, next = None, html = None):
		self.items = items
		self.html = html
		self.__next = next
	
	def __repr__(self):
		return "<total_items: {}, next: {}>".format(len(self.items), self.next)

	def bs4(self):
		return parsing.to_bs4(self.html)	
			
	@property
	def next(self):
		return self.__next

def check(ses, html):
	ses.reCheck(html = html)
	if not ses.logged:
		raise LoginInvalid(ses)