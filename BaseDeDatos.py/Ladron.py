from Juez import JuezMain
from Banda import Banda
global listLadron
class Ladron:
    def listaLadron(self):
        listLadron = []
        l=Ladron()
        n=int(input("¿Cuantos Ladrones son?"))
        for i in range (n):
            l.ladron=input("Ladron:")
            l.codigoLadron = int(input("Ingrese el codigo del ladron\n>"))
            l.nombreLadron = (input("Ingrese el nombre del ladron\n>"))
            l.perteneceBanda = str(input("¿Pertenece alguna banda?"))
            listLadron.append(listLadron)
        l.mainLadron()

    def visualizarLadron(self):
        l=Ladron()
        for l in listLadron:
            print("**Registro Ladrones*")
            print("-------------")
            print("Numero de ladron", l.ladron, "\nCodigo ladron:",l.codigoLadron, "\n Nombre Ladron", l.nombreLadron , "\nPertenece a una banda?:" , l.perteneceBanda)
            print("-------------")
        l.mainLadron()

    def mainLadron(self):
        print("Menu ladron")
        print("---------")
        print(
            "Añadir Ladron\n, 2.- Visualizar ladron\n 3.-Ingresar banda delectiva\n 4.-Regresar menu Juez\n 6.Regresar a menu principal")
        opMLa = (int(input(">")))
        if opMLa == 1:
            maiLa = Ladron()
            maiLa.listaLadron()
        elif opMLa == 2:
            maiLa = Ladron()
            maiLa.visualizarLadron()
        elif opMLa == 3:
            mainLaBa = Banda()
            mainLaBa.Banda()
        elif opMLa == 4:
            mainLaJu=JuezMain()
            mainLaJu.mainJuez
        else:
            print("error loa regraremos al menu principal \n ", mainP())

