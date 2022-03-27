class Banda:
    def __init__(self,numeroBanda,numMienbros):
        self.numeroBanda=numeroBanda
        self.numMiembro=numMienbros

    def __str__(self):
        return "Banda: <Numero banda:,{0},numMiembro:,{1}>".format(self.numero,self.numMiembro)

class Bandas:
    def __init__(self):
        self.diccionarioBanda=[]

    def agregarBanda(self,newBanda):
        self.diccionarioBanda.append(newBanda)

    def registroBanda(self):
        print("Registro Banda\n")
        for banda in self.diccionarioBanda:
            print(banda)

class MenuBanda:
    def __init__(self):
        self.matrizBanda=Bandas()

    def mainBanda(self):
        while True:
            print("Menu Banda")
            print("---------")
            print("1.- Añadir Banda\n, 2.- Visualizar banda\n 3.-Menu Ladron\n 4.-Menu juez\n 5.Regresar a menu principal")

            opcion = int(input("> "))
            if 1 == opcion:
                self.agregarBanda()
            elif 2 == opcion:
                self.printBanda()
            elif 3 == opcion:
                from Ladron import MenuLadron
                menuBanda=MenuLadron()
                menuBanda.mainLadron()
            elif 4 == opcion:
                from Juez import M
            elif 5 == opcion:
                break
            else:
                print('Esa opcion no existe')

    def agregarBanda(self):
        numeroBanda = input("Ingrese el numero de la banda:\n>")
        numMiembros = input("Ingrese el numero de miembros de la banda:\n>")
        newBanda = Banda(numeroBanda, numMiembros)
        self.matrizBanda.agregarBanda(newBanda)

    def printBanda(self):
        self.matrizBanda.registroBanda()
        return
