diccionario = {"a" : True, 5: "esto es un string", (1,2) : False, "a" : 100 } #Las claves o IDs tienen que ser inmutables
diccionario["c"] = "nuevo string" #Se agrega nueva llave y valor al diccionario
diccionario["a"] = 563 #Si la llave se encuentra actualiza, si no lo crea

respuesta = diccionario.get("z", False)
valor = diccionario["a"]

del diccionario["a"] #Remueve llave y valor de la llave a

#print(diccionario)
#print(valor)
#print(respuesta)

llaves = list(diccionario.keys()) #todas las llaves del diccionario
values = list(diccionario.values()) #todos los valores del diccionario

diccionario2 = {"z" : 23, "w" : 50}
diccionario.update(diccionario2)
print(llaves)
print(values)
print(diccionario)