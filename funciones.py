def factorial(numero):
	factorial = 1
	while numero > 0:
		factorial = factorial * numero
		numero -= 1
	return factorial

def suma(valor1, valor2):
	return valor1 + valor2

def multiplicacion(valor1, valor2 = 10):
	return valor1 * valor2

#Regresa array con múltiples valores
def multiples_valores():
	return "String", 1, True, 25.6

def mostrar_resultado(funcion):
	print(funcion(6,8))

def palindromo():
	nuevo_valor = frase.replace(" ", "")
	return nuevo_valor == nuevo_valor[::-1]

mi_variable = multiplicacion #puntero a la función
resultado = mi_variable(6,8)
print(resultado)
"""
frase = "anita lava la tina"
print(frase)
resultado = palindromo()
print(frase)
print(resultado)

"""


def valor_global():
	global variable_global #Se modifica variable global. Sin el global no se podría modificar el valor
	variable_global = "Nuevo valor"

variable_global = "Esto es una variable global"
"""
print(variable_global)
valor_global()
print(variable_global)
"""

def crear_variable_global():
	global nueva_variable_global
	nueva_variable_global = "Esto es una variable global dentro de una función"

crear_variable_global()
print(nueva_variable_global)

#print(factorial(5))
#print(suma(1,2))
"""
print(suma(valor2 = 100, valor1 = 20))
print(multiplicacion(10,5))
string, entero, bol, floa = multiples_valores()
print(multiples_valores())

mi_funcion = multiplicacion
mostrar_resultado(mi_funcion)
"""

