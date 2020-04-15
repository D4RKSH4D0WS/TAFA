# fbparser
# i made this for tafa
# you can also use it
# coded by: salism3
# start: 08-04-2020 10:50

from .import_me import *

def find_id_friend(ses, query):
	html = ses.session.get("https://mbasic.facebook.com/search/people/?q=" + query)
	check(ses, html)
	url = parsing.parsing_href(html, "?refid=", one = True)
	html = ses.session.get(url)
	data = parsing.parsing_href(html, "?owner_id=", one = True)
	name = parsing.to_bs4(html).find("title").text
	id_ = data.split("=")[-2].split("&")[0]
	if not data or not "removefriend.php?friend_id" in html:
		return None, None
	return name, id_
	
def find_id_group(ses, query):
	html = ses.session.get("https://mbasic.facebook.com/search/groups/?q=" + query)
	check(ses, html)
	url = parsing.parsing_href(html, "?refid=", one = True)
	html = ses.session.get(url)
	data = parsing.to_bs4(html)
	name = data.find("title").text
	id_ = url.split("?")[0].split("/groups/")[1]
	return name, id_