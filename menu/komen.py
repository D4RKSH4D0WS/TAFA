def spam_komen_friend():
		gas = Komen()
		id = str(input("   [?] Id Target: "))
		if wrong_id(id,p=True):
			print("   [+] Invalid Id")
			enter("menu.m6")
		msg = str(input("   [?] Comment: "))
		limit = int(input("   [?] Limit (int): "))
		if limit <= 0 or limit > 150:
			limit = 150
		print("\n   [+] Spamming Comment To: " + gas.get_name(id))
		gas.dump_sts("https://mbasic.facebook.com/profile.php?id="+id, "Berita Lengkap", "Lihat Berita Lain", limit, "com")
		print("   [+] Total: " + str(len(gas.id)))
		gas.hajar(msg, 0)
		print("\n   [+] Done!")
		enter("menu.m6")

def spam_komen_grup():
		gas = Komen()
		id = str(input("   [?] Id Group: "))
		if wrong_id(id,g=True):
			print("   [+] Invalid Id")
			enter("menu.m6")
		msg = str(input("   [?] Comment: "))
		limit = int(input("   [?] Limit (int): "))
		if limit <= 0 or limit > 150:
			limit = 150
		print()
		echo("[+] Spamming Comment To: " + gas.get_name(id))
		gas.dump_sts("https://mbasic.facebook.com/groups/"+id, "Berita Lengkap", "Lihat Postingan Lainnya", limit, "com")
		echo("[+] Total: " + str(len(gas.id)))
		gas.hajar(msg, 1)
		print()
		echo("[+] Done!")
		enter("menu.m6")

def spam_komen_halaman():
		gas = Komen()
		id = str(input("   [?] Username Fanspage: "))
		if wrong_id(id,f=True):
			print("   [+] Invalid Id")
			enter("menu.m6")
		msg = str(input("   [?] Comment: "))
		limit = int(input("   [?] Limit (int): "))
		if limit <= 0 or limit > 150:
			limit = 150
		print()
		gas.dump_sts("https://mbasic.facebook.com/"+id, "Berita Lengkap", "Tampilkan lainnya", limit, "com")
		echo("[+] Total: " + str(len(gas.id)))
		gas.hajar(msg, 0)
		print()
		echo("[+] Done!")
		enter("menu.m6")

def spam_komen_home():
	gas = Komen()
	msg = str(input("   [?] Comment: "))
	limit = int(input("   [?] Limit (int): "))
	if limit <= 0 or limit > 150:
		limit = 150
	print()
	echo("[+] Spamming Comment in Home")
	gas.dump_sts("https://mbasic.facebook.com/", "Berita Lengkap", "Lihat Berita Lain", limit, "com")
	echo("[+] Total: " + str(len(gas.id)))
	gas.hajar(msg, 0)
	print()
	echo("[+] Done!")
	enter("menu.m6")