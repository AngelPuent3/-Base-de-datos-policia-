from Sucursal import Sucursal as Sucursal
from main import mainP
global listSJuez
global listSCondena


class JuezMain:

    def listaJuez(self):
        listSJuez = []
        j = JuezMain()
        iniJuez=int(input("¿Cuantos jueces desea agregar"))
        for i in range(iniJuez):
            j.codigoJuez = int(input("Ingrese el codigo del juez \n >"))
            j.nombreSJuez = str(input("Ingrese el nombre del juez\n>"))
            j.edadJuez = int(input("Ingrese los años de servicion del juez\n>"))
            listSJuez.append(listSJuez)
        j.mainJuez()



    def visualizarJuez(self):
        j = JuezMain()
        for j in listSJuez:
            print("**Registro Juez*")
            print("-------------")
            print("Codigo de Juez:", j.codigoJuez, "\nNombreJuez:", j.nombreJuez, "\n Años de servicio:", j.edadJuez)
            print("-------------")
        j.mainJuez()

    def determinarCondena(self):
        listSCondena = []
        jc = JuezMain()
        jc.numJuez=int(input("Ingrese el numero de Juez\n>"))
        jc.casoJuez=int(input("Ingrese el numerto de caso \n>"))
        jc.condena=str(input("¿Lo va condenar?\n"))
        jc.tipoCondena=str(input("¿Cual es su condena?\n >"))
        jc.tiempoCondena=int(input("Ingrese su condena en años \n >"))
        listSCondena.append(jc)

    def visualizarCondena(self):
        for jc in listSCondena:
            print("**Registro Juez*")
            print("-------------")
            print("Numero de Juez", jc.numuez, "\nCaso juez:", jc.casoJuez, "\n Lo va condenar?", jc.tipoCondena,
                  "\n Tipo de condena:", jc.tipoCondena,
                  "\nTiempo de condena", jc.tiempoCondena)
            print("-------------")

    def mainJuez(self):
        print("Menu Juez")
        print("---------")
        print("Añadir Juez\n, 2.- Visualizar Juez\n 3.-Determinar condena\n 4.-Visualizar Condena\n 5. Agregar sucursal \n 6.Regresar a menu principal")
        opMjuez=(int(input(">")))
        if opMjuez==1:
            je=JuezMain()
            je.listaJuez()
        elif opMjuez==2:
            je=JuezMain()
            je.visualizarJuez()
        elif opMjuez==3:
            mainJuezSuc=Sucursal()
            mainJuezSuc.mainSucursal()
        elif opMjuez==4:
            mainP()
        else:
            print("error loa regraremos al menu principal \n ", mainP())




