def division(num_uno, num_dos):
	def validacion():
		return num_uno > 0 and num_dos > 0

	if(validacion()):
		return num_uno / num_dos

def crear_funcion(num_uno, num_dos):
	def validacion():
		return num_uno > 0 and num_dos > 0
	return validacion #clousures

def aplicar_funcion(func):
	return func()
	
"""
resultado = division(10,0)
print(resultado)
"""

nueva_funcion = crear_funcion(10,5)
#aplicar_funcion(nueva_funcion)
print(aplicar_funcion(nueva_funcion))