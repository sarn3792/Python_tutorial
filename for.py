lista = [1,2,3,4,5,6,7,8,9,10]

for valor in lista:
	pass

nuevo_rango = range(0,10)
nuevo_rango = range(20)
nuevo_rango = range (0,20,2) #Del 0 al 19 de dos en 2
#for valor in nuevo_rango:
	#print(valor)

#for valor in range(0,20,1): #i = 0; i < 20 ; i++
	#print(valor)

for indice, valor in enumerate(lista):
	print(valor, "tiene el indice", indice)

for valor in range(0, len(lista)):
	pass

for valor in "Curso python":
	pass
	#print(valor)

diccionario = {"a" : 1, "b" : 2}
for llave, valor in diccionario.items():
	print("La llave", llave, "tiene el valor", valor)


