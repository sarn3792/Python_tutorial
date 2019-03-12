def main_decorator(is_valid):

	def funcion_decorator(func): #A
		def before_action():
			print("Se agrega código antes para decorar")

		def after_action():
			print("Se agrega código después para decorar")

		def nueva_funcion(*args, **kwargs): #C, recibe N argumentos para que sea para cualquier función que reciba parámetros o no
			#Se agrega código antes si se quisiera
			if(is_valid):
				before_action()

			result = func(*args, **kwargs)
			#Se agrega código después si se quisiera
			after_action()
			return result
		return nueva_funcion; #C

	return funcion_decorator



@main_decorator
def saluda():
	print("Hola mundo")

@main_decorator(True)
def suma(num_uno, num_dos):
	return num_uno + num_dos

#saluda()
print(suma(10,5))

#A, B, C son funciones. A recibe como parámetro B para poder crear C