my_string = "Hola mundo 'Samuel'"
my_string = """Este es un string que contiene salto de linea\nComo puede verse """
entero = 1
course = "Python3"
name = "Samuel"

final_message = my_string + course #1
final_message = "Nuevo curso de %s por %s" %(course, name) #2
final_message = "Nuevo curso de {} por {} vale {}".format(course,name, entero) #3
#print(my_string)
print(final_message)