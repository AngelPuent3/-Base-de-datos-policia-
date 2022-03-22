matrizLadron=list()
listaLadron=list()

class Ladron:

    def listaSLadron(self):
        global matrizLadron
        global listaLadron
        print("Porfavor llenar la lista mediante las siguiente indicaciones\n"
              "Numero dato 0 ---> Codigo del ladron\n"
              "Numero dato 1 ---> Nombre del ladron\n"
              "Numero dato 2 ---> Pertenece alguna banda?---Si---No")
        f = input("Enterr >>>>")
        columnas = int(input("Ingrese el numero de ladrones que desea agregar"))
        matrizLadron = []
        for ren in range(columnas):
            listaLadron = []
            for col in range(3):
                print("Numero de ladrones", ren, "Numero dato", col)
                aLa = str(input(">"))
                listaLadron.append(aLa)
            matrizLadron.append(listaLadron)
        liLa=Ladron()
        return liLa.mainLadron()
    
    def visualizarLadron(self):
        print(matrizLadron)
        viLa = Ladron()
        viLa.mainLadron()

    def mainLadron(self):
        from main import  mainP
        from juez import Juez
        from banda import Banda
        print("Menu ladron")
        print("---------")
        print(
            "Añadir Ladron\n2.- Visualizar ladron\n3.-Menu banda\n4.-Regresar menu Juez\n5.Regresar a menu principal")
        opMLa = (int(input(">")))
        if opMLa == 1:
            maiLa = Ladron()
            maiLa.listaSLadron()
        elif opMLa == 2:
            maiLa = Ladron()
            maiLa.visualizarLadron()
        elif opMLa == 3:
            mainLaBa = Banda()
            mainLaBa.Banda()
        elif opMLa == 4:
            mainLaJu=Juez()
            mainLaJu.mainJuez()
        elif opMLa==5:
            mainP()
        else:
            print("error loa regraremos al menu principal \n ", mainP())
