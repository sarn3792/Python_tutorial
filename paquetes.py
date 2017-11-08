from animales_paquetes import Gato
from animales_paquetes import creador_gatos
from animales_paquetes import CONSTANTE	

gato = creador_gatos("Nuevo gato por paquete")
print(gato.nombre)
print(gato.comer())