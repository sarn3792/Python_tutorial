class Animal:
	@property
	def terrestre(self):
		return True

class Felino(Animal): #Clase padre
	@property
	def garras_restractiles(self):
		return True

	def cazar(self):
		print("El felino está cazando")

class Mascota:
	def __init__(self, nombre):
		self.nombre = nombre

	def mostrar_nombre(self):
		print(self.nombre)

class Gato(Felino, Mascota):
	def __init__(self, nombre):
		Mascota.__init__(self, nombre)

	def gato_cazador(self):
		self.cazar()

	def mostrar_nombre(self): #Sobre escritura de métodos
		Mascota.mostrar_nombre(self)
		print("El nombre del gato es: {}".format(self.nombre))



gato = Gato("Patricio")
gato.mostrar_nombre()
#gato.gato_cazador()

