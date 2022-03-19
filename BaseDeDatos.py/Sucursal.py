from main import mainP
from Banco import Banco
from Vigilante import Vigilante
global listSucursal
global listContratacion



class Sucursal:

    def mainSucursal(self):
        print("Menu Sucursal")
        print("---------")
        print("Añadir Sucursal\n, 2.- Visualizar Sucursal\n 3.-Contratar Viglante\n 4.- Visualizar Contratacion \n 5.-Regresar a menu principal\n 6. Regresar a menu banco ")
        opMSu = (int(input(">")))
        if opMSu==1:
            mainSu=Sucursal()
            mainSu.listaSucursal()
        elif opMSu==2:
            mainSu=Sucursal()
            mainSu.visualizarSurcusal()
        elif opMSu==3:
            mainSu=Sucursal()
            mainSu.contratarSucursal()
        elif opMSu ==4:
            mainSu = Sucursal()
            mainSu.visualizarContrato()
        elif opMSu==5:
            mainP()
        elif opMSu==6:
            mainbancoSu=Banco()
            mainbancoSu.mainBanco()
        else:
            print("error regresando al menu principal \n ")
            sumain=Sucursal()
            sumain.mainSucursal()

    def listaSucursal(self):
        listSucursal =[]
        su = Sucursal()
        opS = int(input("¿Cuantos sucursales  tiene el banco?"))
        for i in range(opS):
            su.codigoSucursal = int(input("Ingrese la clave de la sucursal"))
            su.edadSucursal = int(input("Ingrese los años de la sucursal\n>"))
            listSucursal.append(listSucursal)
        su.mainSucursal()

    def visualizarSurcusal(self):
        su=Sucursal()
        for su in listSucursal:
            print("**Registro Sucursal*")
            print("-------------")
            print("Clave de la sucursal:", su.codigoSucursal, "\nAños que tiene la sucursal:", su.edadSucursal)
            print("-------------")
        su.mainSucursal()



    def contratarSucursal(self):
        VI2=Vigilante()
        VI2.visualizarVigilante()
        print("¿Desea contrarta al vigilante?\n"
              "1.- SI\n"
              "2.- No\n")
        opMCon=int(input(">"))
        if opMCon==1:
            vi=Vigilante()
            vi.vigilante="Vigilante contratado"
            return (vi.vigilante)
        elif opMCon==2:
            vi = Vigilante()
            vi.vigilante = "Vigilante NO contratado"
            return (vi.vigilante)
        else:
            print("Error")
            sucon=Sucursal()
            sucon.contratarSucursal()

    def visualizarContrato(self):
        listSContratacion = []
        su=Sucursal()
        for jc in listSContratacion:
            print("**Registro Juez*")
            print("-------------")
            print("Numero de Juez", jc.numuez, "\nCaso juez:", jc.casoJuez, "\n Lo va condenar?", jc.tipoCondena,
                  "\n Tipo de condena:", jc.tipoCondena,
                  "\nTiempo de condena", jc.tiempoCondena)
            print("-------------")
        su.mainSucursal()






