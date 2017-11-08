"""
lista = []
for valor in range(0, 101):
	lista.append(valor)
"""

#valor a agregar a lista, luego el for
lista = [ valor for valor in range(0, 101) if valor % 2 == 0]
print(lista)

tupla = tuple((valor for valor in range(0, 101) if valor % 2 != 0))
print(tupla)

diccionario = {indice:valor for indice, valor in enumerate(lista) }
print(diccionario)