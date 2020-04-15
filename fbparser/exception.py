# fbparser
# i made this for tafa
# you can also use it
# coded by: salism3
# start: 08-04-2020 10:50

class ArgumentError(ValueError):
	def __init__(self, arg):
		super().__init__("argument '{}' can not be empty".format(arg))
	
class LoginInvalid(ValueError):
	def __init__(self, ses):
		number = ses.number
		cookies = ses.cookies[0:21] + "..."
		super().__init__("login is false in account number {} and cookies {}".format(number, cookies))