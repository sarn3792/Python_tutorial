import random
import datetime
import sys
import time

valor = random.randint(0,10)
lista = [1,2,3,4]
#print(lista)
#random.shuffle(lista) #desordena la lista
#print(lista)

#valor = random.choice(lista) #valor aleatorio en la lista
#print(valor)

#print(datetime.datetime.now())

for i in range(100):
	time.sleep(0.5)
	sys.stdout.write("\r%d %%" % i)
	sys.stdout.flush()



