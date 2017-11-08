contador = 0
while contador < 10:
	print(contador)
	contador+=1

	if contador == 5:
		continue
	elif contador == 6:
		break
else:
	print("El while ha terminado")
