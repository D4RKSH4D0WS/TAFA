# fbparser
# i made this for tafa
# you can also use it
# coded by: salism3
# start: 08-04-2020 10:50

def to_mbasic(url):
	if not url:
		return url
	if not "https://mbasic.facebook.com" in url:
		return "https://mbasic.facebook.com" + url
	return url