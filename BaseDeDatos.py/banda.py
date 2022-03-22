global listBanda
listBanda=[]


class Banda:

    def listaBanda(self):
        b = Banda()
        opBlis=int(input("¿Ingrese cuantos numeros de banda son?"))
        for i in range(opBlis):
            b.numDeBanda = int(input("Ingrese el numero de banda\n>"))
            b.miembrosBanda = int(input("Ingrese los numeros de miembros que tiene la banda\n>"))
            listBanda.append(listBanda)
        b.mainBanda()

    def visualizarBanda(self):
        for b in listBanda:
            print("**Registro Banda*")
            print("-------------")
            print("Numero de banda", b.numDeBanda, "\nNumero de miembros", b.miembrosBanda)
            print("-------------")

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
            mainBanda.listaBanda()
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
