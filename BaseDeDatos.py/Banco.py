from main import mainP
from Sucursal import Sucursal
from Vigilante import Vigilante
global listSBanco

class Banco:
     def listaSBanco(self):
          listSBanco = []
          b=Banco()
          opBa = int(input("¿Cuantos sucursales  tiene el banco?"))
          for i in range(opBa):
               b.codigoBanco = int(input("Ingrese la clave de la sucursal\n>"))
               b.edadBanco = int(input("Ingrese los años de la sucursal\n>"))
               listSBanco.append(listSBanco)
          b.mainBanco()

     def visualizarBanco(self):
          b=Banco()
          for b in listSBanco:
               print("**Registro Juez*")
               print("-------------")
               print("CodigoBanco:", b.codigoBanco, "\nDomicilio del banco:", b.domicilioBanco,
                     "\n Sucursales banco:",
                     b.domicilioBanco)
               print("-------------")
          b.mainBanco()

     def contratarBanco(self):
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


     def mainBanco(self):
          print("Menu Banco")
          print("---------")
          print(
               "Añadir Banco\n, 2.- Visualizar Banco\n 3.Agregar Sucursales\n  4.- Contratar Vigilante 5.Regresar a menu principal\n ")
          opMb= (int(input(">")))
          if opMb == 1:
               mainb = Banco()
               mainb.listaSBanco()
          elif opMb == 2:
               mainb = Banco()
               mainb.visualizarBanco()
          elif opMb == 3:
               suc = Sucursal()
               suc.mainSucursal()
          elif opMb==4:
               mainb=Banco()
               mainb.contratarBanco()
          elif opMb ==5:
               mainP()
          else :
               print("error loa regraremos al menu principal \n ", mainP())













