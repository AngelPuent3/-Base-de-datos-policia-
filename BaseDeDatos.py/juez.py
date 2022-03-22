matrizJuez=[]
listaJuez=[]
class Juez:

    def mostrarJuez(self):
        global matrizJuez
        global listaJuez
        b=Juez()
        print("Porfavor llenar la lista mediante las siguiente indicaciones\n"
              "Numero dato 0 ---> Codigo del juez\n"
              "Numero dato 1 ---> Nombre del Juez\n"
              "Numero dato 2 ---> Años experiencia juez")
        f = input("Enterr >>>>")
        print("Ingrese el numero de jueces")
        columnas = int(input())
        matrizJuez = []
        for ren in range(columnas):
            listaJuez = []
            for col in range(3):
                print("Numero de juez", ren,"Numero dato", col)
                a=str(input(">"))
                listaJuez.append(a)
            matrizJuez.append(listaJuez)
        return b.mainJuez()

    def mostrarCondena(self):
        global matrizCondena
        global listaCondena
        print("Porfavor llenar la lista mediante las siguiente indicaciones\n"
              "Numero dato 0 ---> Ingrese el numero de Juez\n"
              "Numero dato 1 ---> Numero de caso\n"
              "Numero dato 2 ---> Años experiencia juez\n"
              "Numero dato 3 ---> Lo va condenar? -- si/no\n"
              "Numero dato 4 ---> Que tipo de condena le va a dar\n"
              "Numero dato 5 ---> Años de condena\n>")
        f = input("Enterr >>>>")
        print("Ingrese el numero de condenas")
        columnas = int(input())
        matrizCondena = []
        for ren in range(columnas):
            listaCondena = []
            for col in range(6):
                print("Numero de juez", ren,"Numero dato", col)
                co=str(input(">"))
                listaCondena.append(co)
            matrizCondena.append(listaCondena)
        c = Juez()
        return c.mainJuez()

    def visualizarJuez(self):
        print(matrizJuez)
        viJu=Juez()
        viJu.mainJuez()

    def visualizarCondena(self):
        print(matrizCondena)
        viCo=Juez()
        viCo.mainJuez()

    def mainJuez(self):
        from main import mainP
        from ladron import Ladron
        print("Menu Juez")
        print("---------")
        print(
            "1.-Añadir Juez\n2.-Visualizar Juez\n3.-Determinar condena\n4.-Visualizar Condena\n5. Menu ladron \n6.Regresar a menu principal")
        opMjuez = (int(input(">")))
        if opMjuez == 1:
            je = Juez()
            je.mostrarJuez()
        elif opMjuez == 2:
            je = Juez()
            je.visualizarJuez()
        elif opMjuez == 3:
            jeCon = Juez()
            jeCon.mostrarCondena()
        elif opMjuez == 4:
            jeCon = Juez()
            jeCon.visualizarCondena()
        elif opMjuez == 5:
            mainJuezLa = Ladron()
            mainJuezLa.mainLadron()
        elif opMjuez == 6:
            mainP()
        else:
            exit ("Adios")
