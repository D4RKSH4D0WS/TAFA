# fbparser
# i made this for tafa
# you can also use it
# coded by: salism3
# start: 08-04-2020 10:50

from bs4 import BeautifulSoup as parser
from . import sorting

def to_bs4(html):
	return parser(html, "html.parser")

def refsrc(html):
	data = to_bs4(html).find("form", action = lambda x: x and "refsrc=" in x)
	return True if data else False

def getName(html):
	data = to_bs4(html).find("title").text
	return data

def getId(html):
	data = to_bs4(html).find("a", href = lambda x:"/allactivity" in x)["href"].split("/")[1]
	return data

def parsing_href(html, href, one = False, bs4_class = True):
	data = to_bs4(html)
	if one:
		data = data.find("a", href = lambda x: x and href in x)
		if data and sorting: data = sorting.to_mbasic(data["href"])
	else:
		data = data.find_all("a", href = lambda x: x and href in x)
		if bs4_class:
			data = [sorting.to_mbasic(x["href"]) for x in data]
	return data

def jazoestDtsg(html):
	data = to_bs4(html).find_all("input", autocomplete = "off", autocorrect = False)
	if len(data) < 2: return None, None
	data = tuple([x["value"] for x in data])
	return data

def friendRequestParser(html):
	rv = []
	confirm = parsing_href(html, "?confirm=")
	reject = parsing_href(html, "?delete=")
	for x in zip(confirm, reject):
		data = {}
		data["confirm"], data["reject"] = x
		rv.append(data)
	next = parsing_href(html, "?ppk=", one = True)
	return {"items":rv, "next":next}

	
