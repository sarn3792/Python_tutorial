class TinyIntError(Exception):
	def __init__(self):
		self.message = "El número no cuenta con las características de un tiny_int"

	def __str__ (self):
		return self.message

def validate_tiny_int(val):
	try:
		return val >= 0 and val <=255
	except Exception as ex:
		return ex

def validate_val(val):
	try:
		return isinstance(int(val), int)	
	except ValueError as error:
		return False

def tiny_int(val, call_back_function = None):
	try:
		if validate_val(val) and validate_tiny_int(val):
			return True
		else:
			raise TinyIntError()
	except TinyIntError as error:
		return error


def call_back_function():
	print("Esto se ejecuta cuando existe un error!")

print(tiny_int("1234", call_back_function))