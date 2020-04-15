# fbparser
# i made this for tafa
# you can also use it
# coded by: salism3
# start: 08-04-2020 10:50

import urllib3
import requests as r

class HttpRequest(urllib3.PoolManager):
	hulu = {"User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36"}
	
	def request(self, method, url, **kwargs):
		data = super().request(method, url, headers = self.hulu, **kwargs)
		return data
	
	def get(self, url):
		return self.request("GET", url).data.decode()
	
	def r_get(self, url):
		return r.get(url, headers = self.hulu)
	
	def set_kuki(self, kuki):
		self.hulu["cookie"] = kuki