my_list = [8, 15, 15.5, 30]
my_list.append(9)
#my_list.insert(1, "insert")
my_list.remove(15)
#my_list.pop() #remueve el último elemento de la lista
my_list.sort() #ascendente
my_list.sort(reverse = True) #Descendente

my_list_two = [23, 50]
my_list.extend(my_list_two)

print(my_list)