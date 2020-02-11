def hapus_msg():
	gas = Other()
	confirm_execute("menu.m7")
	gas.dump_sts_wclass('https://mbasic.facebook.com/messages', True, 'Lihat Pesan Sebelumnya', 0, 'messages/read', href_na=True)
	echo("[+] Total: " + str(len(gas.id)))
	gas.hapus_msg()
	print()
	echo("[+] Done!")
	enter("menu.m7")

def downloader():
	try: os.mkdir('output')
	except: pass
	os.system('cls' if os.name == "nt" else 'clear')
	logo(n=True)
	menu = Menu()
	gas = Other()
	menu = menu.m8()
	if menu == 0:
		m = Menu()
		m.m7()
	elif menu == 1:
		os.system('clear')
		logo(n=True)
		echo("[+] Select Your Album To Download")
		gas.tampilkan_album()
		tempat = gas.album.split("/")[-2]
		os.chdir('output')
		try: os.mkdir(tempat)
		except: pass
		os.chdir('..')
		download_proces(gas.album, f"output/{tempat}")
	elif menu == 2:
		url = str(input("   [?] Album Url (use mbasic fb): "))
		if not 'mbasic.facebook.com' in url:
			echo("[+] Url Not Valid")
			enter("menu.m7")
		elif not 'https://' in url or 'http://' in url:
			echo("[+] Url Not Valid")
			enter("menu.m7")
		data = gas.o_url(url)
		nama = str(parser(data, 'html.parser').find('title')).replace('<title>', '').replace('</title>', '')
		if 'Konten Tidak Ditemukan' == nama:
			echo("[+] Album Not Found")
			enter("menu.m7")
		echo("[+] Album Name: " + nama)
		tempat = url.split("/")[-2]
		os.chdir('output')
		try: os.mkdir(tempat)
		except: pass
		os.chdir('..')
		download_proces(url, f"output/{tempat}")
		
	else:
		downloader()
		

def download_proces(url, path):
	gas = Other()
	gas.dump_sts_wclass(url, True, 'Lihat Foto Lainnya', 0, None, href_na=True, filter=False)
	gas.id = filter(lambda x: "photo.php?" in x or "photos" in x, gas.id)
	gas.id = list(gas.id)
	echo("[+] Total: " + str(len(gas.id)))
	#print(gas.id)
	gas.download(path)
	print()
	echo(f"[+] Done! photos saved in {path}")
	enter("menu.m7")
		