matrizVigilante=[]
listaVigilante=[]
class Vigilante():

    def listaVigilante(self):
        global matrizVigilante
        global listaVigilante
        print("Porfavor llenar la lista mediante las siguiente indicaciones\n"
              "Numero dato 0 ---> Fecha de contratacion --- Ejem: 17 Noviembre del 2019\n"
              "Numero dato 1 ---> Cuenta con arma --- Ejem: Si/No\n"
              "Numero dato 2 ---> Quien lo contrata --- Ejem: Lic. Perez")
        f = input("Enterr >>>>")
        columnas = int(input("Ingrese el numero de bancos que desea agregar"))
        matrizVigilante = []
        for ren in range(columnas):
            listaVigilante = []
            for col in range(3):
                print("Numero de banco", ren, "Numero dato", col)
                aVig = str(input(">"))
                listaVigilante.append(aVig)
            matrizVigilante.append(listaVigilante)
        viP = Vigilante()
        return viP.mainVigilante()

    def visualizarVigilante(self):
        print(matrizVigilante)
        viBa = Vigilante()
        viBa.mainVigilante()
    
    def mainVigilante(self):
        from main import mainP
        from banco import  Banco
        from sucursal import Sucursal
        print("Menu Vigilante")
        print("---------")
        print("Añadir vigilante\n, 2.- Visualizar vigilante\n 3.Regresar menu Banco\n 4.-Regresar menu Sucursal\n  5.Regresar a menu principal")
        opMVig = (int(input(">")))
        if opMVig==1:
            mainvi=Vigilante()
            mainvi.listaVigilante()
        elif opMVig==2:
            mainvi=Vigilante()
            mainvi.visualizarVigilante()
        elif opMVig==3:
            mainBaVi=Banco()
            mainBaVi.mainBanco()
        elif opMVig==4:
            mainSucVi=Sucursal()
            mainSucVi.mainSucursal()
        elif opMVig==5:
            mainP()
        else:
            print("error loa regraremos al menu principal \n ")
            mainP()
