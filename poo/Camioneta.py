from Automovil import Automovil
class Camioneta (Automovil):
    potencia = ""

    def __init__(self, mat=None, mode=None, mar=None, col=None, pot=None):
        Automovil.__init__(self, mat, mode, mar, col)
        if pot is not None:
            self.potencia = pot

    def setPotencia(self,pot):
        self.potencia = pot

    def getPotencia(self):
        potencia = self.potencia
        return potencia
