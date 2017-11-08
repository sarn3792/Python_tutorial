try:
	lista = [1,2]
	print(lista[9])

except ZeroDivisionError as ex:
	print(ex)
except IndexError as ex:
	print(ex)
except Exception as ex:
	print(ex)

finally:
	print("Se terminó el script")

