def generador(*args):
	"""Recibe n cantidad de números y regresa..."""
	for valor in args:
		yield valor * 10, True

#for valor1, valor2 in generador(1,2,3,4,5): #Regresa un objeto con dos valores, se hace for para imprimir dicho object
#	print(valor1, valor2)


#nombre = generador.__name__
#documentacion = generador.__doc__
#print(documentacion, nombre)

