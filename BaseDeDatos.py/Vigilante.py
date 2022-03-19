import Sucursal
from main import mainP
from Banco import Banco
from Sucursal import Sucursal
global listVigilante


class Vigilante(Sucursal):

    def listaVigilante(self):
        listVigilante = []
        vi=Vigilante()
        suclist=Sucursal()
        opVi=int(input("Cunatos vigilantes son? \n >"))
        for i in range(opVi):
          vi.fechaVigilante=str(input("Ingrese fecha de contratacion:\n Ejemplo: (16/Marzo/2027) \n >"))
          vi.armaVigilante=int(input(input("Tiene arma? \n 1.- Si \n 2.-No")))
          vi.contratado= suclist.contratarSucursal()
          listVigilante.append(listVigilante)
        vi.mainVigilante()

    def visualizarVigilante(self):
        vi=Vigilante()
        for vi in listVigilante:
            print("**Registro Juez*")
            print("-------------")
            print("Fecha de contratacion", vi.fechaVigilante, "\nCuenta con arma?:", vi.armaVigilante, "\n Estado de contratacion", vi.contratado)
            print("-------------")
        vi.mainVigilante()


    def mainVigilante(self):
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



