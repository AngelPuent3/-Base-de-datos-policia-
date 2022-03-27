class Sucursal:
    def __init__(self,codigo,edad):
        self.codigo=codigo
        self.edad=edad

    def __str__(self):
        return "Sucursal:<Codigo {0}, Años {1}>".format(self.codigo,self.edad)

class Sucursales:
    def __init__(self):
        self.diccionarioSucursal=[]

    def agregarSucursal(self,newSucursal):
        self.diccionarioSucursal.append(newSucursal)

    def registroSucursal(self):
        print("Registro Sucursal")
        for sucursal in self.diccionarioSucursal:
            print(sucursal)

class MenuSucursal:
    def __init__(self):
        self.matrizSucursal= Sucursales()

    def mainSucursal(self):
        while True:
            print("Menu Sucursal")
            print("---------")
            print("1.-Añadir Sucursal\n, 2.- Visualizar Sucursal\n 3.-Contratar Viglante\n 4.- Visualizar Contratacion \n 5.-Regresar a menu principal\n 6. Regresar a menu banco ")

            opcion = int(input("> "))
            if 1 == opcion:
                self.agregarSucursal()
            elif 2 == opcion:
                self.printSucursales()
            elif 3 == opcion:
                from Vigilante import MenuVigilante
                menuSucursal=MenuVigilante()
                menuSucursal.mainVigilante()
            elif 4 == opcion:
                from bancos import MenuBanco
                menuSucursal = MenuBanco()
                menuSucursal.mainBanco()
            elif 5 == opcion:
                from main import mainP
                mainP()
            else:
                print('Esa opcion no existe')

    def agregarSucursal(self):
        codigo = input("Ingrese el codigo de la sucursal:\n>")
        domicilio = input("Ingrese el domicilio de la sucursal:\n>")
        newSucursal = Sucursal(codigo, domicilio)
        self.matrizSucursal.agregarSucursal(newSucursal)

    def printSucursales(self):
        self.matrizSucursal.registroSucursal()











