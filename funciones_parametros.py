def sumas(*args):
	#print(argumentos)
	result = 0
	for valor in args:
		result += valor

	return result
	#print(type(argumentos))
def suma(**kwargs):
	valor = kwargs.get("valor", "No contiene valor")
	print(valor)

print(sumas(10,20,30,40))

resultado = suma(valor = "Eduardo", x = 2, y = 9, z = True)

# * --> tuplas
# ** --> diccionarios



