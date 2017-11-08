course = "Curso"
my_string = "Código Facilito!"

result = "{a} de {b}".format(a = course, b = my_string)
#result = result.lower()
#result = result.title()

pos = result.find('Código')
count = result.count('C')

new_string = result.replace("c", "x")
new_split = result.split(" ")

print(result)
print(pos)
print(count)
print(new_string)
print(new_split)