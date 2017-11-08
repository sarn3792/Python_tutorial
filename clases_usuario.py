class Usuario:
	def __init__(self, username, password, email):
		self.username = username
		self.__password = self.__generar_password(password) #Atributos privados
		self.email = email

	def __generar_password(self, password): #Métodos privados
		return password.upper()

	@property
	def password(self):
		return self.__password

	@password.setter
	def password(self, value):
		self.__password =  self.__generar_password(value)

samuel = Usuario("Samuel", "samuel", "samuel@hotmail.com")
print(samuel.password)
samuel.password = "Nuevo password"
print(samuel.password)

