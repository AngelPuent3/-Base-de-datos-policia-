
listSucursal=list()
matrizSucursal=list()



class Sucursal:

    def mainSucursal(self):
        from main import mainP
        from banco import  Banco
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
        global matrizSucursal
        global listSucursal
        print("Porfavor llenar la lista mediante las siguiente indicaciones\n"
              "Numero dato 0 ---> Ingrese el codigo de sucursal\n"
              "Numero dato 1 ---> Edad de la sucursal\n")
        f = input("Enterr >>>>")
        columnas = int(input("Ingrese el numero de sucursales"))
        matrizSucursal = []
        for ren in range(columnas):
            listSucursal = []
            for col in range(6):
                print("Numero de sucursal", ren, "Numero dato", col)
                su = str(input(">"))
                listSucursal.append(su)
            matrizSucursal.append(listSucursal)
        suc = Sucursal()
        return suc.mainSucursal()

    def visualizarSurcusal(self):
        print(matrizSucursal)
        viSu = Sucursal()
        viSu.mainSucursal()

    def contratarSucursal(self):
        from vigilante import Vigilante
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
