global listLadron
lisLadron=[]

class Ladron:
    def listaLadron(self):
        l=Ladron()
        n=int(input("¿Cuantos Ladrones son?"))
        for i in range (n):
            l.codigoLadron = int(input("Ingrese el codigo del ladron\n>"))
            l.nombreLadron = str(input("Ingrese el nombre del ladron\n>"))
            l.perteneceBanda = str(input("¿Pertenece alguna banda?"))
            listLadron.append(l)
        l.mainLadron()

    def visualizarLadron(self):
        le2=Ladron
        for l in listLadron:
            print("**Registro Ladrones*")
            print("-------------")
            print("Numero de ladron", l.ladron, "\nCodigo ladron:",l.codigoLadron, "\n Nombre Ladron", l.nombreLadron , "\nPertenece a una banda?:" , l.perteneceBanda)
            print("-------------")
        le2.mainLadron()

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
            maiLa.listaLadron()
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
