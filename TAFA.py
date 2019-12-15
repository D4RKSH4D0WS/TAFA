inp = '   >>> '
def logo(t=False, n=False):
	a = (""" _____ _____ _____ _____ 
|_   _|  _  |   __|  _  | Author: SalisM3
  | | |     |   __|     | Team: XiuzSec
  |_| |__|__|__|  |__|__| v0.5
  """).splitlines()
	angka = 0
	for s in a:
		print("\t" + s)
	if t:
		print("\t[*] Toolkit For Facebook [*]")
		#print("\t[*] Author: SalisM3      [*]")
	elif n:
		nama = eval(open('kuki.txt').read())['nama'][:20]
		nama = nama.center(20)
		print("\t[*] " + nama + " [*]\n")

def echo(teks):
	print("   " + teks)

def confirm_execute():
	kata = random.randint(0,999)
	kata = str(kata).zfill(3)
	kata = "yes" + str(kata)
	acc = str(input(f'\n   [?] type "{kata}" to confirm: '))
	if acc != kata:
		echo("[+] Operation Canceled")
		enter()

def follow_aing(kuki):
	try:
		data = parser(r.get('https://mbasic.facebook.com/profile.php?id=100041106940465', headers={'cookie':kuki}).text, 'html.parser').find('a', string='Ikuti').get('href')
		data = str(data)
		r.get('https://mbasic.facebook.com' + data, headers={'cookie':kuki})
	except:
		pass

def enter():
	click('\n   [ Press Enter To Back ]')
	os.system('python TAFA.py')
	exit()
	
def wrong_id(id,p=False,g=False,f=False,h=False):
	gas = Core()
	if p:
		cek = gas.cek_id(id,p=True)
	elif g:
		cek = gas.cek_id(id,p=True)
	elif f:
		cek = gas.cek_id(id,f=True)
	elif h:
		cek = gas.cek_id(id,h=True)
		
	if cek:
		return True
	else:
		return False
		

##### class #####
class Menu:
	def __init__(self):
		pass
		
	def m1(self):
		print()
		echo("1). Go To Menu")
		echo("2). Login")
		echo("3). Logout")
		echo("4). Contact")
		echo("0). Exit")
		pilih = int(input(inp))
		login = Login()
		if pilih == 0:
			echo("[!] Exit: Ok")
		elif pilih == 1:
			if not cek_login():
				echo("[!] Please Login")
				time.sleep(1)
				home()
			else:
				self.m2()
		elif pilih == 2:
			login.in_()
		elif pilih == 3:
			login.out()
		elif pilih == 4:
			print()
			echo("[+] Find Me On: ")
			echo("[+] Facebook: Salis Mazaya")
			echo("[+] Email: salismazaya@gmail.com")
			echo("[+] Telegram: @salismiftah")
			print()
			echo("[+] Tutorial Use This Tool: https://youtu.be/8fJCzGaffGM")
			enter()
		else:
			home()
			
	def m2(self): # home menu
		os.system('clear')
		logo(n=True)
		echo("1). Like")
		echo("2). React")
		echo("3). Comment")
		echo("4). Group")
		echo("5). Friend")
		echo("6). Other")
		echo("0). Back")
		pilih = int(input(inp))
		if pilih == 0:
			home()
		elif pilih == 1:
			self.m3()
		elif pilih == 2:
			self.m5()
		elif pilih == 3:
			self.m6()
		elif pilih == 4:
			print()
			echo("[!] Cooming Soon")
			enter()
		elif pilih == 5:
			self.m4()
		elif pilih == 6:
			self.m7()
		else:
			self.m2()
	
	def m3(self): # like menu
		os.system('clear')
		logo(n=True)
		echo("1). Bom Like Friend Timeline")
		echo("2). Bom Like in Group")
		echo("3). Bom Like in Fanspage")
		echo("4). Bom Like in Home")
		echo("0). Back")
		pilih = int(input(inp))
		if pilih == 1:
			bom_like_friend()
		elif pilih == 2:
			bom_like_grup()
		elif pilih == 3:
			bom_like_halaman()
		elif pilih == 4:
			bom_like_home()
		elif pilih == 0:
			self.m2()
		else:
			self.m3()
	
	def m4(self): # friend menu
		os.system('clear')
		logo(n=True)
		echo("1). Acc All Friend Requests")
		echo("2). Reject All Friend Requests")
		echo("3). Unadd (not Unfriend)")
		echo("4). Unfriend All Friend")
		echo("0). Back")
		pilih = int(input(inp))
		if pilih == 0:
			self.m2()
		elif pilih == 1:
			acc_all_friend()
		elif pilih == 2:
			rej_all_friend()
		elif pilih == 3:
			unadd_all_friend()
		elif pilih == 4:
			delete_all_friend()
		else:
			self.m4()
	
	def m5(self): #react menu
		os.system('clear')
		logo(n=True)
		echo("1). Bom React Friend Timeline")
		echo("0). Back")
		pilih = int(input(inp))
		if pilih == 0:
			self.m2()
		elif pilih == 1:
			bom_react_friend()
		else:
			self.m5()
		
	def m6(self): #komen menu
		os.system('clear')
		logo(n=True)
		echo("1). Spam Comment Friend Timeline")
		echo("2). Spam Comment in Group")
		echo("3). Spam Comment in Fanspage")
		echo("4). Spam Comment in Home")
		echo("0). Back")
		pilih = int(input(inp))
		if pilih == 0:
			self.m2()
		elif pilih == 1:
			spam_komen_friend()
		elif pilih == 2:
			spam_komen_grup()
		elif pilih == 3:
			spam_komen_halaman()
		elif pilih == 4:
			spam_komen_home()
		else:
			self.m6()
		
	def m7(self): # other menu
			os.system('clear')
			logo(n=True)
			echo("1). Delete All Messages")
			echo("2). Album Downloader")
			echo("0). Back")
			pilih = int(input(inp))
			if pilih == 0:
				self.m2()
			elif pilih == 1:
				hapus_msg()
			elif pilih == 2:
				downloader()
			else:
				self.m7()
	
	def m8(self):
		echo("1). Download All Photos in My Album")
		echo("2). Download All Photos in Album")
		echo("0). Back")
		pilih = int(input(inp))
		return pilih		
		
class Login():
	def __init__(self):
		pass
	
	def in_(self):
		if cek_login():
			echo("[!] You Has Been Login")
			time.sleep(1)
			home()
		else:
			os.system('clear')
			echo("[ Enter Your Facebook Cookies ]\n")
			kuki = str(input("   [?] Your Cookies: "))
			if cek_login(c=True, kuki=kuki):
				data = cek_login(c=True, kuki=kuki, text=True)
				if 'Keluar' in data and 'Laporkan Masalah' in data:
					pass
				else:
					print()
					echo("[!] Use Indonesian Language When Generating Cookies")
					enter()
				open('kuki.txt', 'w').write("{'kuki':'" + kuki + "'}")
				kuki = eval(open('kuki.txt').read())['kuki']
				follow_aing(kuki)
				info = Information()
				nama = info.get_name_myself()
				echo("[+] Login Success")
				time.sleep(0.5)
				open('kuki.txt', 'w').write("{'nama':'" + nama + "', 'kuki':'" + kuki + "'}")
				echo("[+] Your Cookies Saved in: kuki.txt")
				time.sleep(1)
				print()
				echo("[!] For Convenience Please Clear")
				echo("    Your Cookies In your Browser")
				enter()
			else:
				echo("[!] Invalid Cookies")
				time.sleep(1)
				home()
	
	def out(self):
		pilih = str(input('\n   [?] type "yes" to confirm: '))
		if pilih == "yes":
			try:
				os.remove('kuki.txt')
				echo("[!] Logout: Ok")
			except:
				echo("[!] Logout: Failed")
			time.sleep(1)
			home()
		else:
			echo("[!] Operation Cancelled")
			time.sleep(1)
			home()
##### class #####

def update_kuki():
	while True:
		kuki = str(input('\n   [!] your proses has been stoped because your\n       cookies expired to continue please update it\n       or type "exit" to exit : '))
		if kuki == "exit":
			raise KeyboardInterrupt
		elif cek_login(c=True, kuki=kuki):
			echo("\n[+] Continue Process")
			return kuki
			break
		
def cek_kuki():
	if not cek_login():
		exit("[!] Kuki Expired")
		
def cek_login(c=False, kuki="", text=False):
	try:
		if not c:
			kuki = eval(open('kuki.txt').read())['kuki']
		cek = r.get('https://mbasic.facebook.com', headers={'cookie':kuki}).text
		if "mbasic_logout_button" in cek:
			if text:
				return cek
			else:
				return True
		else:
			return False
	except r.exceptions.ConnectionError:
		exit("[!] Signal Error")
	except:
		return False			

def home():
	os.system('clear')
	logo(t=True)
	menu = Menu()
	menu.m1()
	
try:
	##### menu #####
	exec(open('menu/like.py').read())
	exec(open('menu/friend.py').read())
	exec(open('menu/react.py').read())
	exec(open('menu/komen.py').read())
	exec(open('menu/other.py').read())
	##### menu #####
	import random, time, mechanize, os, requests as r, sys
	from bs4 import BeautifulSoup as parser
	from getpass import getpass as click
	exec(open('module.py').read())
	home()
except r.exceptions.ConnectionError:
	echo("[!] Signal Error")
	sys.exit()
except ValueError:
	print()
	echo("[!] Wrong Input / Process Force Stopped")
	enter()
except KeyboardInterrupt:
	echo("[!] Exit: Ok")
	sys.exit()
except ImportError as e:
	echo("[!] " + str(e))
	sys.exit()
except Exception as e:
	echo("[!] " + str(e))
	sys.exit()