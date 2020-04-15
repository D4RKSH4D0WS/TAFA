# fbparser
# i made this for tafa
# you can also use it
# coded by: salism3
# start: 08-04-2020 10:50

from .import_me import *

def friend_request(ses, next = None):
	html = ses.session.get("https://mbasic.facebook.com/friends/center/requests/" if not next else next)
	check(ses, html)
	data = parsing.friendRequestParser(html)
	return Output(**data, html = html)

def friend_requested(ses, next = None):
	html = ses.session.get("https://mbasic.facebook.com/friends/center/requests/outgoing/" if not next else next)
	check(ses, html)
	data = parsing.parsing_href(html, "/cancel/?")
	next = parsing.parsing_href(html, "?ppk=", one = True)
	return Output(items = data, next = next, html = html)