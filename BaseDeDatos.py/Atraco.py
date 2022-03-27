class Atraco:
    def __init__(self,fechaAtraco):
        self.fechaAtraco=fechaAtraco

    def __str__(self):
        return "Atraco: <Fecha atraco: {0}>".format(self.fechaAtraco)

class Atracos:
    def __init__(self):
        self.diccionarioAtracos=[]

    def agregarAtraco(self,newAtraco):
        self.diccionarioAtracos.append(newAtraco)

    def registroAtraco(self):
        print("Registro Atraco\n")
        for atraco in self.diccionarioAtracos:
            print(atraco)

class MenuAtraco:
    def __init__(self):
        self.matrizAtraco=Atracos()

    def mainAtraco(self):
        while True:
            print("Menu Banco")
            print("---------")
            print("1.- Añadir Atraco\n2.- Visualizar Atraco\n3.- Agregar Sucursales\n4.- Contratar Vigilante\n5.- Salir\n ")

            opcion = int(input("> "))
            if 1 == opcion:
                self.agregarAtraco()
            elif 2 == opcion:
                self.printAtraco()
            elif 3 == opcion:
                pass
            elif 4 == opcion:
                pass
            elif 5 == opcion:
                break
            else:
                print('Esa opcion no existe')

    def agregarAtraco(self):
        fechaAtraco=input("Ingrese la fecha del atraco\n>")
        newAtraco= Atraco(fechaAtraco)
        self.matrizAtraco.agregarAtraco(newAtraco)

    def printAtraco(self):
        self.matrizAtraco.registroAtraco()



