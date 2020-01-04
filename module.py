class Core:
	def __init__(self):
		self.angka = 1
		self.id = []
		try:
			self.kuki = eval(open('kuki.txt').read())['kuki']
		except:
			self.kuki = ""
	
	def hitung_process(self):
		global angka
		sys.stdout.write('\r   [+] Process: ' + str(self.angka))
		sys.stdout.flush()
		self.angka += 1
			
	def filter(self, str):
		data = filter(lambda x: str in x, self.id)
		return list(data)
	
	def cek_sts(self, cek):
		cek = str(cek)
		cek = parser(cek, 'html.parser').find('title')
		if "Konten Tidak Ditemukan" in str(cek):
			if not "mbasic_logout_button" in self.o_url("https://mbasic.facebook.com"):
				self.kuki = update_kuki()
		elif "Peringatan: Jangan Terlalu Cepat" in str(cek):
			print()
			echo("[!] Process Stoped, Because Your Account Can't Like")
			enter()
		elif "Tindakan Diblokir" in str(cek):
			print()
			echo("[!] Proses Stoped, Beacuse Your Account\n       Blocked Until 24 Hours")
			enter()
	
	def cek_id(self, id, p=False, g=False, f=False, h=False):
		if p:
			url = "https://mbasic.facebook.com/profile.php?id="+id
		elif g:
			url = "https://mbasic.facebook.com/groups/"+id
		elif f:
			url = "https://mbasic.facebook.com/"+id
		elif h:
			url = "https://mbasic.facebook.com/"
		if "Halaman yang diminta tidak bisa ditampilkan sekarang." in self.o_url(url):
			return True
		else:
			return False
	
	def ms_url(self, url, data, nr): #submit br data
		try:
			br = mechanize.Browser()
			br.set_handle_robots(False)
			br.addheaders = [('Cookie', self.kuki), ('User-Agent', 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36')]
			br.open(url)
			br.select_form(nr=nr)
			for s in data.split("&"):
					key = s.split("=")[0]
					value = s.split("=")[1]
					br.form[key] = value
			return br.submit().read()
		except ValueError:
			return "form error"
		
	def mo_url(self, url):
		br = mechanize.Browser()
		br.set_handle_robots(False)
		br.addheaders = [('Cookie', self.kuki), ('User-Agent', 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36')]
		return str(br.open(url).read())
	
	def o_url(self, url, bytes=False):
		data = r.get(url, headers={'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36', 'Cookie':self.kuki})
		if bytes:
			data = data.content
		else:
			data = data.text
		return data
	
	def dump_sts_wclass(self, url, stri, stri2, limit, kondisi, class_na=False, href_na=False, img=False, req=True, filter=True):
		penentu = 0
		angka = 0
		self.url = url
		while penentu == 0:
			if req:
				a = self.o_url(self.url)
			else:
				a = self.mo_url(self.url)
			b = parser(a, 'html.parser')
			if href_na:
				data = b.find_all('a', href=stri)
			elif img:
				data = b.find_all('img')
			else:
				data = b.find_all('a', class_=stri)
			for s in data:
				try:
					if img:
						self.id.append(s.get('src'))
					else:
						self.id.append("https://mbasic.facebook.com" + s.get('href'))
					angka += 1
					if angka == limit:
						penentu += 1
						break
				except:
					pass
			next = b.find('a', string=stri2)
			if "None" in str(next):
				break
			else:
				self.url = "https://mbasic.facebook.com" + next.get('href')
		if filter:
			self.id = self.filter(kondisi)
				
	def dump_sts(self, url, stri, stri2, limit, kondisi):
		penentu = 0
		angka = 0
		self.url = url
		while penentu == 0:
			a = self.o_url(self.url)
			b = parser(a, 'html.parser')
			for s in b.find_all('a', string=stri):
				self.id.append("https://mbasic.facebook.com" + s.get('href'))
				angka += 1
				if angka == limit:
					penentu += 1
					break
			next = b.find('a', string=stri2)
			if "None" in str(next):
				break
			else:
				self.url = "https://mbasic.facebook.com" + next.get('href')
		self.id = self.filter(kondisi)
		
class Information(Core):
	def get_name_myself(self):
		data = self.mo_url("https://mbasic.facebook.com/me")
		return str(parser(data, 'html.parser').find('title')).replace('<title>', '').replace('</title>', '')
	
	def get_name(self, id):
		data = self.mo_url("https://mbasic.facebook.com/profile.php?id="+id)
		return str(parser(data, 'html.parser').find('title')).replace('<title>', '').replace('</title>', '')

class Like(Information):
	def hajar(self):
		for ss in self.id:
			cek = self.mo_url(ss)
			self.cek_sts(cek)
			self.hitung_process()
			time.sleep(1)
		self.id.clear()
		
class React(Information):
	def hajar(self, re):
		if re == 1:
			stri = "Super"
		elif re == 2:
			stri = "Haha"
		elif re == 3:
			stri = "Wow"
		elif re == 4:
			stri = "Sedih"
		elif re == 5:
			stri = "Marah"
		for ss in self.id:
			ss = ss.split("&")[2].replace("ft_ent_identifier=", "")
			data = parser(self.mo_url('https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id='+ss), 'html.parser').find_all('a')
			for s in data:
				if stri in str(s):
					cek = self.mo_url("https://mbasic.facebook.com" + s.get('href'))
					self.cek_sts(cek)
					self.hitung_process()
				time.sleep(1)
					
class Friend(Information):
	def hajar(self):
		for ss in self.id:
			cek = self.o_url(ss)
			self.cek_sts(cek)
			self.hitung_process()
			time.sleep(1)
		self.id.clear()
	
	def delete_all_friend(self):
		for ss in self.id:
			try:
				data = parser(self.o_url(ss), 'html.parser').find('a', string='Lainnya').get('href')
				data = parser(self.o_url('https://mbasic.facebook.com' + data), 'html.parser').find('a', string='Batalkan pertemanan').get('href')
				br = mechanize.Browser()
				br.set_handle_robots(False)
				br.addheaders = [('Cookie', self.kuki), ('User-Agent', 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36')]
				br.open('https://mbasic.facebook.com' + data)
				br.select_form(nr=1)
				br.submit(name='confirm')
				self.hitung_process()
			except:
				pass
		self.id.clear()

class Komen(Information):
	def hajar(self, msg, nr):
		for ss in self.id:
			cek = self.ms_url(ss, "comment_text=" + msg, nr)
			self.cek_sts(cek)
			self.hitung_process()
			time.sleep(1.5)
		self.id.clear()
			
class Other(Information):
	def hapus_msg(self):
		for ss in self.id:
			try:
				br = mechanize.Browser()
				br.set_handle_robots(False)
				br.addheaders = [('Cookie', self.kuki), ('User-Agent', 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36')]
				br.open(ss)
				br.select_form(nr=2)
				data = br.submit(name='delete').read()
				data = parser(data, 'html.parser').find('a', string='Hapus').get('href')
				self.o_url('https://mbasic.facebook.com' + data)
				self.hitung_process()
			except:
				br.select_form(nr=1)
				data = br.submit(name='delete').read()
				data = parser(data, 'html.parser').find('a', string='Hapus').get('href')
				self.o_url('https://mbasic.facebook.com' + data)
				self.hitung_process()
		self.id.clear()
		
		
	def download(self, path):
		for s in self.id:
			name = str(time.strftime('%Y-%H-%M-%S'))
			data = parser(self.mo_url(s), 'html.parser').find_all('img')[1].get('src')
			data = self.o_url(data, bytes=True)
			open(f'{path}/{name}.jpg', 'wb').write(data)
			self.hitung_process()
		self.id.clear()
	
	def tampilkan_album(self):
		data = parser(self.mo_url('https://mbasic.facebook.com/me/photos'), 'html.parser').find_all('a', href=True)
		jumlah = 0
		for s in data:
			if '/albums/' in str(s):
				jumlah += 1
				self.id.append('https://mbasic.facebook.com' + s.get('href'))
				nama_album = str(s).split(">")[1].replace("</a", "")
				jumlah = str(jumlah)
				echo(f"{jumlah}). {nama_album}")
				jumlah = int(jumlah)
		jumlah = str(jumlah)
		echo("0" * len(jumlah) + "). Back")
		del jumlah, nama_album
		while True:
			try:
				pilih = int(input(inp))
				if pilih == 0:
					enter()
					break
				self.album = self.id[pilih - 1]
				break
			except:
				pass
		self.id.clear()
	
	def download_album(self):
		pass
			