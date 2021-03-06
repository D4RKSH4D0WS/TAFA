# fbparser
# i made this for tafa
# you can also use it
# coded by: salism3
# start: 08-04-2020 10:50

from .urllib3_session import HttpRequest
from .like import *
from .comment import *
from .react import *
from .friend import *
from .other import *
from .exception import *
from .import_me import *

class Account:
	__number = 0
	__logged = False
	__name = None
	__id = None
	__cookies = None
	__session = None
	__session_active = False
	
	def __init__(self, kuki):
		self.__number_account = self.__tambah()
		self.__cookies = kuki
		ses = HttpRequest()
		ses.set_kuki(self.cookies)
		self.__session = ses
		url = ses.r_get("https://mbasic.facebook.com/me").url
		html = ses.get(url)
		if "/zero/optin/write/?action=confirm" in html:
			html = self.antiFree(html)
		if "mbasic_logout_button" in html:
			self.__ganti(html)
	
	def __repr__(self):
		return "<logged: {}, name: {}, id: {}, cookies: {}, session_active: {}>".format(self.logged, self.name, self.id, self.cookies, self.session_active)
	
	def __ganti(self, html):
		self.__logged = True
		self.__session_active = True
		self.__name = parsing.getName(html)
		self.__id = parsing.getId(html)
	
	@classmethod
	def __tambah(cls):
		cls.__number += 1
		return cls.__number

	@staticmethod
	def random_string():
		string = "qwertyuiopasdfghjklzxcvbmmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
		acak = "".join([random.choice(string) for _ in range(10)])
		return acak

	def reset(self):
		self.__logged = False
		self.__name = None
		self.__id = None
		self.__session = None
		self.__session_active = False
	
	def reCheck(self, html = None):
		if not html:
			html = self.session.get("https://mbasic.facebook.com/me").text
		if parsing.refsrc(html):
			self.reset()
		
	def antiFree(self, html):
		url = parsing.parsing_href(html, "?action=cancel", one = True)
		html = self.session.get(url)
		url = parsing.to_bs4(html).find("form", action = lambda x: "?action=confirm" in x)
		url = sorting.to_mbasic(url["action"])
		fb_dtsg, jazoest = parsing.jazoestDtsg(html)
		self.session.request("POST", url, fields = {"fb_dtsg":fb_dtsg, "jazoest":jazoest})
		return self.session.get("https://mbasic.facebook.com")
		
	@property
	def number(self):
		return self.__number_account
		
	@property
	def logged(self):
		return self.__logged
	
	@property
	def name(self):
		return self.__name
	
	@property
	def id(self):
		return self.__id
	
	@property
	def cookies(self):
		return self.__cookies
	
	@property
	def session(self):
		return self.__session
	
	@property
	def session_active(self):
		return self.__session_active
	
	def myGroup(self):
		html = self.session.get("https://mbasic.facebook.com/groups/?seemore")
		data = parsing.parsing_href(html, "/groups/", bs4_class = False)
		del data[0:2]
		name = [x.text for x in data]
		id = [x["href"].replace("/groups/", "").split("?")[0] for x in data]
		return Output(items = list(zip(name,id)), html = html)
