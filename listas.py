my_list = [8, 15, 15.5, 30]
my_list.append(9)
#my_list.insert(1, "insert")
my_list.remove(15)
#my_list.pop() #remueve el último elemento de la lista
my_list.sort() #ascendente
my_list.sort(reverse = True) #Descendente

my_list_two = [23, 50]
my_list.extend(my_list_two) #junta las dos listas

lista = [valor for valor in range(0, 101) if valor % 2 == 0] #inicializa lista con 101 elementos
print(lista)

print(my_list)