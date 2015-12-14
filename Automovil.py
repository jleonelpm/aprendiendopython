class Automovil (object):
    matricula = ""
    modelo = ""
    marca = ""
    color=""

    def __init__(self, mat=None, mode=None, mar=None, col=None): #constructor
        #No existe constructor, pudiendose sustituir por lo siguiente
        if mat is not None:
            self.matricula = mat
        if mode is not None:
            self.modelo = mode
        if mar is not None:
            self.marca = mar
        if col is not None:
            self.color = col

    def setMatricula(self,mat):
        self.matricula = mat

    def getMatricula(self):
        return self.matricula

    def setModelo(self,mode):
        self.modelo = mode

    def getModelo(self):
        return self.modelo

    def setMarca(self,mar):
        self.marca = mar

    def getMarca(self):
        return self.marca

    def setColor(self,col):
        self.color = col

    def getMarca(self):
        color = self.color
        return color