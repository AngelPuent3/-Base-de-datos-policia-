class Juez:
    def __init__(self,codigo,nombre,experiencia):
        self.codigo=codigo
        self.nombre=nombre
        self.experiencia=experiencia

    def __str__(self):
        return "Juez: <Codigo juez: {0}, Nombre juez: {1}, Años de experiencia: {2}>".format(self.codigo,self.nombre,self.experiencia)

class Jueces:
    def __init__(self):
        self.diccionarioJuez=[]

    def agregarJuez(self,newJuez):
        self.diccionarioJuez.append(newJuez)

    def registroJuez(self):
        print("Registro Juez\n")
        for juez in self.diccionarioJuez:
            print(juez)

class MenuJuez:
    def __init__(self):
        self.matrizJuez=Jueces()

    def mainJuez(self):
        while True:
            print("Menu Juez")
            print("---------")
            print("1.-Añadir Juez\n2.-Visualizar Juez\n3.-Determinar condena\n4.-Visualizar Condena\n5. Menu ladron \n6.Regresar a menu principal")

            opcion = int(input("> "))
            if 1 == opcion:
                self.agregarJuez()
            elif 2 == opcion:
                self.printJuez()
            elif 3 == opcion:
                from Sucursal import MenuSucursal
                menu=MenuSucursal()
                menu.mainSucursal()
            elif 4 == opcion:
                from Ladron import MenuLadron
                menuJuez=MenuLadron()
                menuJuez.mainLadron()
            elif 5 == opcion:
                from main import mainP
                mainP()
            else:
                print('Esa opcion no existe')

    def agregarJuez(self):
        codigo = input("Ingrese el codigo del juez:")
        nombre = input("Ingrese el nombre del juez:\n")
        experiencia = input("Ingrese los años de experiecia\n>")
        newJuez = Juez(codigo, nombre,experiencia)
        self.matrizJuez.agregarJuez(newJuez)

    def printJuez(self):
        self.matrizJuez.registroJuez()







