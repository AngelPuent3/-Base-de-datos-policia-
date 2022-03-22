matrizBanco=list()
listaBanco=list()
listContrato=list()

class Banco:

    def mainBanco(self):
        from sucursal import Sucursal
        from main import mainP
        print("Menu Banco")
        print("---------")
        print(
            "1.-Añadir Banco\n2.- Visualizar Banco\n3.Agregar Sucursales\n4.- Contratar Vigilante\n5.-Regresar a menu principal\n ")
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
        global matrizBanco
        global listaBanco
        ba = Banco()
        print("Porfavor llenar la lista mediante las siguiente indicaciones\n"
              "Numero dato 0 ---> Codigo del Banco\n"
              "Numero dato 1 ---> Edad del banco\n"
              "Numero dato 2 ---> Domicilio banco---Ejemplo: 14 norte #102 col. Centro")
        f = input("Enterr >>>>")
        columnas = int(input("Ingrese el numero de Bancos que desea agregar"))
        matrizBanco = []
        for ren in range(columnas):
            listaBanco = []
            for col in range(3):
                print("Numero de juez", ren, "Numero dato", col)
                aBan = str(input(">"))
                listaBanco.append(aBan)
            matrizBanco.append(listaBanco)
        return ba.mainBanco()

    def visualizarBanco(self):
        print(matrizBanco)
        viBa = Banco()
        viBa.mainBanco()

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









