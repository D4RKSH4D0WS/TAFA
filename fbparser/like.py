# fbparser
# i made this for tafa
# you can also use it
# coded by: salism3
# start: 08-04-2020 10:50

from .import_me import *

def like_core(ses, url, next, string_next):
	html = ses.session.get(url if not next else next)
	check(ses, html)
	data = parsing.parsing_href(html, "like.php")
	next = sorting.to_mbasic(parsing.parsing_href(html, string_next, one = True))
	return Output(items = data, next = next, html = html)

def like_post_home(ses, next = None):
	return like_core(ses, "https://mbasic.facebook.com", next, "?aftercursorr=")

def like_post_friend(ses, id = None, next = None):
	if id == None and next == None:
		raise ArgumentError("id")
		
	return like_core(ses, "https://mbasic.facebook.com/profile.php?id={}&v=timeline".format(id), next, "?cursor")

def like_post_fanspage(ses, username = None, next = None):
	if username == None and next == None:
		raise ArgumentError("username")
	
	return like_core(ses, "https://mbasic.facebook.com/{}".format(username), next, "?sectionLoadingID=")
	
def like_post_grup(ses, id = None, next = None):
	if id == None and next == None:
		raise ArgumentError("id")

	return like_core(ses, "https://mbasic.facebook.com/groups/{}".format(id), next, "?bacr=")