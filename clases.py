class Lapiz:
	def __init__(self, color, contiene_borrador = True, usa_grafito = True):
		self.color = color
		self.contiene_borrador = contiene_borrador
		self.usa_grafito = usa_grafito

	def dibujar(self):
		print("El lapiz está dibujando")

	def borrar(self):
		if self.is_valido_para_borrar():
			print("El lapiz está borrando")
		else:
			print("No es posible borrar")

	def is_valido_para_borrar(self):
		return self.contiene_borrador
#Objeto de tipo lápiz
lapiz_generico = Lapiz("Verde")
lapiz_generico.borrar()
