class Ladron:
    def __init__(self,codigo,nombre,perteneceBanda):
        self.codigo=codigo
        self.nombre=nombre
        self.perteneceBanda=perteneceBanda

    def __str__(self):
        return "Ladron:<Codigo ladron {0},Nombre ladron: {1},Pertence banda: {2}>".format(self.codigo,self.nombre,self.perteneceBanda)

class Ladrones:
    def __init__(self):
        self.diccionarioLadron=[]

    def agregarLadron(self,newLadron):
        self.diccionarioLadron.append(newLadron)

    def registroLadrones(self):
        print("Registro Ladron \n")

class MenuLadron:
    def __init__(self):
        self.matrizLadron=Ladrones()

    def mainLadron(self):
        while True:
            print("Menu Ladron")
            print("---------")
            print("Añadir Ladron\n2.- Visualizar ladron\n3.-Menu banda\n4.-Regresar menu Juez\n5.Regresar a menu principal")

            opcion = int(input("> "))
            if 1 == opcion:
                self.agregarLadron()
            elif 2 == opcion:
                self.printLadron()
            elif 3 == opcion:
                pass
            elif 4 == opcion:
                pass
            elif 5 == opcion:
                break
            else:
                print('Esa opcion no existe')

    def agregarLadron(self):
        codigo = input('Ingrese el codigo del ladron:\n>')
        nombre= input("Ingrese el nombre del ladron\n>")
        pertenceBanda = input('Ingrese si pertenece alguna banda:\n> ')

        newLadron = Ladron(codigo,nombre,pertenceBanda)
        self.matrizLadron.agregarLadron(newLadron)

    def printLadron(self):
        self.matrizLadron.registroLadrones()



