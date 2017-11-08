class Usuario:
	def __new__(cls):
		print("Este método es el primero que se ejecuta")
		return super().__new__(cls)

	def __init__(self):
		print("Este método es el segundo que se ejecuta")
		self.__password = "Es secreto"

	def __str__(self): #ToString() del objeto
		return "Esto se imprime cuando intento mostrar el objeto"

	def __getattr__(self, atributo):
		print("Aquí mostramos que no se encontró el atributo")

	def mostrar_password(self):
		print(self.__password)

usuario = Usuario()
usuario.__password = "No secreto" #Nuevo atributo, no es el mismo de la clase
#print(usuario.__dict__)
usuario.mostrar_password()
print(usuario)
usuario.apellido