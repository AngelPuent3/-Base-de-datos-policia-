global listBanco
global listContrato
listBanco=list()
listContrato=list()

class Banco:

    def mainBanco(self):
        from sucursal import Sucursal
        from main import mainP
        print("Menu Banco")
        print("---------")
        print(
            "Añadir Banco\n, 2.- Visualizar Banco\n 3.Agregar Sucursales\n  4.- Contratar Vigilante 5.Regresar a menu principal\n ")
        opMb = (int(input(">")))
        if opMb == 1:
            mainb = Banco()
            mainb.listaSBanco()
        elif opMb == 2:
            mainb = Banco()
            mainb.visualizarBanco()
        elif opMb == 3:
            suc = Sucursal()
            suc.mainSucursal()
        elif opMb == 4:
            mainb = Banco()
            mainb.contratarBanco()
        elif opMb == 5:
            mainP()
        else:
            exit("Adios")


    def listaSBanco(self):
          b=Banco()
          opBa = int(input("¿Cuantos sucursales  tiene el banco?"))
          for i in range(opBa):
               b.codigoBanco = int(input("Ingrese la clave de la sucursal\n>"))
               b.edadBanco = int(input("Ingrese los años de la sucursal\n>"))
               b.domicilioBanco=str(input("Ingrese la direccion del banco\nEjem: 14 norte Col. Centro"))
               listBanco.append(b)
          b.mainBanco()

    def visualizarBanco(self):
          b=Banco()
          for b in listBanco:
               print("**Registro banco*")
               print("-------------")
               print("CodigoBanco:", b.codigoBanco, "\nDomicilio del banco:", b.domicilioBanco,
                     "\n Sucursales banco:",
                     b.domicilioBanco)
               print("-------------")
          b.mainBanco()

    def contratarBanco(self):
          from vigilante import Vigilante
          viCon = Vigilante()
          viCon.mainVigilante()
          print("¿Desea contrarta al vigilante?\n"
                "1.- SI\n"
                "2.- No\n"
                "3.- Regresar al menu de banco")
          opMCon = int(input(">"))
          if opMCon == 1:
               viCon = Vigilante()
               viCon.mainVigilante()
               viCon.vigilante = "Vigilante contratado"
          elif opMCon == 2:
               viCon = Vigilante()
               viCon.vigilante = "Vigilante NO contratado"
          elif opMCon==3:
               b=Banco()
               b.mainBanco()
          else:
               print("Error")








