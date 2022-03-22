global listRe
global listCo
listJu = list()
listCo= list()


class Juez:

    def listaReservacion(self):
        j = Juez()
        opListRe = int(input("ingrese la cantidad de jueces"))
        for i in range(opListRe):
            j.codigoJuez = int(input("Ingrese el codigo del juez \n >"))
            j.nombreSJuez = str(input("Ingrese el nombre del juez\n>"))
            j.edadJuez = int(input("Ingrese los años de servicion del juez\n>"))
            listJu.append(j)
            print("-------------")
        j.mainJuez()

    def visualizarJuez(self):
        ViJu = Juez()
        for j in listRe:
            print("Codigo Juez ", j.codigoJuez, "\nNombre del juez:", j.nombreJuez,"\nEdad juez:",j.edadJuez)
        ViJu.mainJuez()

    def listaCondena(self):
        jc = Juez()
        opListCo = int(input("ingrese la cantidad de jueces"))
        for i in range(opListCo):
            jc.numJuez = int(input("Ingrese el numero de Juez\n>"))
            jc.casoJuez = int(input("Ingrese el numerto de caso \n>"))
            jc.condena = str(input("¿Lo va condenar?\n"))
            jc.tipoCondena = str(input("¿Cual es su condena?\n >"))
            jc.tiempoCondena = int(input("Ingrese su condena en años \n >"))
            listCo.append(jc)
            print("----")
        jc.mainJuez()

    def visualizarCondena(self):
        for jc in listSCondena:
            print("**Registro Juez*")
            print("-------------")
            print("Numero de Juez", jc.numuez, "\nCaso juez:", jc.casoJuez, "\n Lo va condenar?", jc.tipoCondena,
                  "\n Tipo de condena:", jc.tipoCondena,
                  "\nTiempo de condena", jc.tiempoCondena)
            print("-------------")
        jvi=Juez()
        jvi.mainJuez()


    def mainJuez(self):
        from main import mainP
        from ladron import Ladron
        print("Menu Juez")
        print("---------")
        print(
            "Añadir Juez\n, 2.- Visualizar Juez\n 3.-Determinar condena\n 4.-Visualizar Condena\n 5. Menu ladron \n 6.Regresar a menu principal")
        opMjuez = (int(input(">")))
        if opMjuez == 1:
            je = Juez()
            je.listaJuez()
        elif opMjuez == 2:
            je = Juez()
            je.visualizarJuez()
        elif opMjuez == 3:
            jeCon = Juez()
            jeCon.determinarCondena()
        elif opMjuez == 4:
            jeCon = Juez()
            jeCon.visualizarJuez()
        elif opMjuez == 5:
            mainJuezLa = Ladron()
            mainJuezLa.mainLadron()
        elif opMjuez == 6:
            mainP()
        else:
            exit("Adios")



