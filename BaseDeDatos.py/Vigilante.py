class Vigilante:
    def __init__(self,fecha,arma, contrato):
        self.fecha=fecha
        self.arma=arma
        self.contrato=contrato

    def __str__(self):
        return "Vigilante:<Fecha de contrato: {0}, Arma: {1}>".format(self.fecha,self.arma,self.contrato)

class Vigilantes:
    def __init__(self):
        self.diccionarioVigilante=[]

    def agregarVigilante(self,newVigilante):
        self.diccionarioVigilante.append(newVigilante)

    def registroVigilante(self):
        print("Registro vigilante\n")
        for vigilante in self.diccionarioVigilante:
            print(vigilante)

class MenuVigilante:
    def __init__(self):
        self.matrizVigilante= Vigilantes()

    def mainVigilante(self):
        while True:
            print("Menu Vigilante")
            print("---------")
            print("Añadir vigilante\n, 2.- Visualizar vigilante\n 3.Regresar menu Banco\n 4.-Regresar menu Sucursal\n  5.Regresar a menu principal")

            opcion = int(input("> "))
            if 1 == opcion:
                self.agregarVigilante()
            elif 2 == opcion:
                self.printVigilantes()
            elif 3 == opcion:
                from bancos import MenuBanco
                menuVigilante=MenuBanco()
                menuVigilante.mainBanco()
            elif 4 == opcion:
                from Sucursal import MenuSucursal
                menuVigilante=MenuSucursal()
                menuVigilante.mainSucursal()
            elif 5 == opcion:
                from main import mainP
                mainP()
            else:
                print('Esa opcion no existe')

    def agregarVigilante(self):
        codigo = input("Ingrese el codigo del vigilante:\n>")
        arma = input("Ingrese el domicilio del vigilante:\n>")
        contrato= input("Quien lo contrato?\n>")
        newVigilante= Vigilante(codigo,arma,contrato)
        self.matrizVigilante.agregarVigilante(newVigilante)

    def printVigilantes(self):
        self.matrizVigilante.registroVigilante()









