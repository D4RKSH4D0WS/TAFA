# fbparser
# i made this for tafa
# you can also use it
# coded by: salism3
# start: 08-04-2020 10:50

from . import parsing
from . import sorting
import urllib3

def open_url(ses, url):
	return ses.session.request("GET", url)

def comment(ses, url, text):
	ses = ses.session
	html = ses.get(url)
	try:
		data = parsing.to_bs4(html).find("form")
		url = sorting.to_mbasic(data["action"])
		data = data.find_all("input", type = "hidden")
		fb_dtsg = data[0]["value"]
		jazoest = data[1]["value"]
		return ses.request("POST", url, fields = dict(fb_dtsg = fb_dtsg, jazoest = jazoest, comment_text = text))
	except:
		return html

def react(ses, url, type = "love"):
	ses = ses.session
	html = ses.get(url)
	data = parsing.to_bs4(html)
	try:
		if type == "haha":
			url = sorting.to_mbasic(data.find("a", href = lambda x: "&reaction_type=4" in x)["href"])
		elif type == "wow":
			url = sorting.to_mbasic(data.find("a", href = lambda x: "&reaction_type=3" in x)["href"])
		elif type == "sad":
			url = sorting.to_mbasic(data.find("a", href = lambda x: "&reaction_type=7" in x)["href"])
		elif type == "angry":
			url = sorting.to_mbasic(data.find("a", href = lambda x: "&reaction_type=8" in x)["href"])
		else:
			url = sorting.to_mbasic(data.find("a", href = lambda x: "&reaction_type=2" in x)["href"])
	except:
		return html
	return ses.get(url)

def dump(ses, func, arg = [], kwargs = {"next":None}, limit = 100):
	if kwargs.get("next") == None:
		kwargs["next"] = None
	arg.insert(0, ses)
	
	angka = 0
	rv = []
	data = func(*arg, **kwargs)
	for x in data.items:
		angka += 1
		rv.append(x)
		if angka == limit:
			break
	else:
		penentu = data.next
		while penentu:
			data = func(ses, next = data.next)
			for x in data.items:
				angka += 1
				rv.append(x)
				if angka == limit:
					penentu = False
					break
			if not data.next:
				penentu = False
	
	return rv
	
	