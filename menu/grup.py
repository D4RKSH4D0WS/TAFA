def myGrup():
	gas = Grup()
	gas.getListGrup()
	gas.id.pop()
	print()
	echo(f"[+] Total {len(gas.id)}")
	for x in range(len(gas.id)):
		echo(f"{x + 1}). {gas.id[x][0]}")
	enter("menu.m9")

def outGrup():
	gas = Grup()
	gas.getListGrup()
	print()
	echo("[?] Choose groups to out:")
	echo(f"[+] Total groups: {len(gas.id) - 1}")
	echo("0). Back")
	for x in range(len(gas.id)):
		echo(f"{x + 1}). {gas.id[x][0]}")
	pilih = None
	while True:
		if pilih == -1:
			enter("menu.m9")
			exit()
		try:
			pilih = int(input(inp)) - 1
			if pilih < 0 or pilih > len(gas.id) - 1: raise Exception
			break
		except:
			echo("[!] operation cancelled" if pilih == -1 else "[!] not found")
	print()
	echo("[+] Group to Out: " + (gas.id[pilih][0] if gas.id[pilih][0] != "All" else "All Groups"))
	confirm_execute("menu.m9")
	if pilih != len(gas.id) - 1:
		gas.out(gas.id[pilih][1])
		echo("[+] Succcess")
		enter("menu.m9")
	else:
		for x in gas.id[-1][1]:
			gas.out(x)
			gas.hitung_process()
		print()
		echo("[+] Done!")
		enter("menu.m9")

def inGrup():
	gas = Grup()
	print()
	query = input("   [?] Query: ")
	limit = int(input("   [?] Limit (int): "))
	gas.getListGrup(forOut = False, query = query, limit = limit)
	print(gas.id)
	# for x in gas.id:
	# 	gas.o_url(x)
	# 	gas.hitung_process()
	# echo("[+] Done!")
	# enter("menu.m9")


	