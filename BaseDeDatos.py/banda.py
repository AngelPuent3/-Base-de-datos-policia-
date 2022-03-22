matrizBanda=[]
listaBanda=[]

class Banda:

    def listaSBanda(self):
        global matrizBanda
        global listaBanda
        print("Porfavor llenar la lista mediante las siguiente indicaciones\n"
              "Numero dato 0 ---> Numero de banda --int\n"
              "Numero dato 1 ---> Miembros de banda --int\n")
        f = input("Enterr >>>>")
        columnas = int(input("Ingrese el numero de bandas que desea agregar"))
        matrizBanda = []
        for ren in range(columnas):
            listaBanda = []
            for col in range(3):
                print("Numero de banda", ren, "Numero dato", col)
                aBand = str(input(">"))
                listaBanda.append(aBand)
            matrizBanda.append(listaBanda)
        lisBanda = Banda()
        return lisBanda.mainBanda()

    def visualizarBanda(self):
        print(matrizBanda)
        viBan = Banda()
        viBan.mainBanda()


    def mainBanda(self):
        from main import mainP
        from ladron import Ladron
        from juez import  Juez
        print("Menu Banda")
        print("---------")
        print(
            "1.- Añadir Banda\n, 2.- Visualizar banda\n 3.-Menu Ladron\n 4.-Menu juez\n 5.Regresar a menu principal")
        opMb = (int(input(">")))
        if opMb == 1:
            mainBanda = Banda()
            mainBanda.listaSBanda()
        elif opMb == 2:
            mainBanda = Banda()
            mainBanda.visualizarBanda()
        elif opMb== 3:
            maiLaB=Ladron()
            maiLaB.mainLadron()
        elif opMb == 4:
            maiJuezB=Juez()
            maiJuezB.mainJuez()
        elif opMb==5:
            mainP()
        else:
            print("error loa regraremos al menu principal \n ")
            mainP()
