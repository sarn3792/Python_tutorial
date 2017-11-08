class Animal:
	volador = True

class Cocodrilo(Animal):
	def __init__(self, nombre):
		self.nombre = nombre

	@classmethod #Pueden acceder a los atributos y métodos de las clases que están heredando
	def new(cls, nombre):
		cls.volador = False
		return Cocodrilo(nombre) #Retorna una instancia de cocodrilo


cocodrilo = Cocodrilo.new("coco")
print(cocodrilo.nombre)
print(cocodrilo.volador)