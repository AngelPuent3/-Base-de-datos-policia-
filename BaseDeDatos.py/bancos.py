class Banco:
    def __init__(self,codigo,domicilio):
        self.codigo=codigo
        self.domicilio=domicilio

    def __str__(self):
        return "Banco:<Codigo {0}, Domicilio {1}>".format(self.codigo,self.domicilio)

class Bancos:
    def __init__(self):
        self.diccionarioBanco=[]

    def agregarBanco(self,newBanco):
        self.diccionarioBanco.append(newBanco)

    def registroBanco(self):
        print("Registro Bancos:\n")
        for banco in self.diccionarioBanco:
            print(banco)

class MenuBanco():
    def __init__(self):
        self.matrizBanco = Bancos()

    def mainBanco(self):
        while True:
            print("Menu Banco")
            print("---------")
            print("1.- Añadir Banco\n2.- Visualizar Banco\n3.- Agregar Sucursales\n4.- Contratar Vigilante\n5.- Salir\n ")

            opcion = int(input("> "))
            if 1 == opcion:
                self.agregarBanco()
            elif 2 == opcion:
                self.printBancos()
            elif 3 == opcion:
                from Sucursal import MenuSucursal
                menu=MenuSucursal()
                menu.mainSucursal()
            elif 4 == opcion:
                from Vigilante import MenuVigilante
                menu=MenuVigilante()
                menu.mainVigilante()
            elif 5 == opcion:
                break
            else:
                print('Esa opcion no existe')

    def agregarBanco(self):
        codigo = input("Ingrese el codigo del banco:\n>")
        domicilio = input("Ingrese el domicilio del banco:\n>")
        newBanco = Banco(codigo, domicilio)
        self.matrizBanco.agregarBanco(newBanco)


    def printBancos(self):
        self.matrizBanco.registroBanco()











