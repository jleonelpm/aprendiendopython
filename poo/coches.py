from Automovil import Automovil
from Camioneta import Camioneta

coche = Automovil()

coche.setMatricula("MEX1420L")
print (coche.getMatricula())

camion = Camioneta()
camion.setPotencia("4 Caballos de Fuerza")
print (camion.getPotencia())
