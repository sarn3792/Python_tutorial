class Circulo:
	_pi = 3.1416 #Variable stática

	def __init__(self, radio):
		self.radio = radio

	def area(self): #Métodos de instancia
		return self.radio * self.radio * Circulo.pi()

	@staticmethod #Métodos státicos
	def pi():
		return 3.1416

circulo_uno = Circulo(4)
print(circulo_uno.area())
print(circulo_uno.pi())
#print(circulo_uno.__dict__)