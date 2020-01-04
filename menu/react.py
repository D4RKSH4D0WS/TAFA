def bom_react_friend():
	id = str(input("   [?] Id Target: "))
	if wrong_id(id,p=True):
		print("   [+] Invalid Id")
		enter()
	limit = int(input("   [?] Limit (int): "))
	print("   1). Super")
	print("   2). Haha")
	print("   3). Wow")
	print("   4). Sad")
	print("   5). Angry")
	while 1 == 1:
		pilih = int(input('   >>> '))
		if pilih >= 1 and pilih <= 5:
			break
	gas = React()
	print("\n   [+] Spamming React To: " + gas.get_name(id))
	gas.dump_sts("https://mbasic.facebook.com/profile.php?id="+id, "Suka", "Lihat Berita Lain", limit, "like.php")
	print("   [+] Total: " + str(len(gas.id)))
	gas.hajar(pilih)
	print("\n   [+] Done!")
	enter()

def bom_react_grup():
	id = str(input("   [?] Id Group: "))
	if wrong_id(id,g=True):
		print("   [+] Invalid Id")
		enter()
	limit = int(input("   [?] Limit (int): "))
	print("   1). Super")
	print("   2). Haha")
	print("   3). Wow")
	print("   4). Sad")
	print("   5). Angry")
	while 1 == 1:
		pilih = int(input('   >>> '))
		if pilih >= 1 and pilih <= 5:
			break
	gas = React()
	print("\n   [+] Spamming React To: " + gas.get_name(id))
	gas.dump_sts("https://mbasic.facebook.com/groups/"+id, "Suka", "Lihat Postingan Lainnya", limit, "like.php")
	print("   [+] Total: " + str(len(gas.id)))
	gas.hajar(pilih)
	print("\n   [+] Done!")
	enter()

def bom_react_home():
	limit = int(input("   [?] Limit (int): "))
	print("   1). Super")
	print("   2). Haha")
	print("   3). Wow")
	print("   4). Sad")
	print("   5). Angry")
	while 1 == 1:
		pilih = int(input('   >>> '))
		if pilih >= 1 and pilih <= 5:
			break
	gas = React()
	print("\n   [+] Spamming Like in Home ")
	gas.dump_sts("https://mbasic.facebook.com/", "Suka", "Lihat Berita Lain", limit, "like.php")
	print("   [+] Total: " + str(len(gas.id)))
	gas.hajar(pilih)
	print("\n   [+] Done!")
	enter()