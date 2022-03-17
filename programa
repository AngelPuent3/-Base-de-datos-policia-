#vuelvo global mis listas para poder trabajarlas
global listvigilante
global listJuez
global listAtraco
listAtraco=list() #Creo las listas para guardar los datos de las clase
listvigilante=list()
listVigilante=list()

class Vigilante: #Creacion de las clase
    def _init_(self,claveVigilante,cumpleaños): #constructor de la clase vigilante, igualo las variables...
        self.claveVigilante=claveVigilante #para poder trabajarla en las listas
        self.cumpleaños=cumpleaños

    def listaVigilante(self): #metodo para ingresar los datos
        v=Vigilante() #instacia de la clase para guardar los datos en la lista
        v.claveVigilante=int(input("ingrese la clave del vigilante (int)\n>"))
        v.cumpleaños=str(input("ingrese su fecha de nacimiento (int)\n>"))
        listvigilante.append(v)#implementacion de la lista con las instacias genradas a partir del constructor






class Juez:
    def _init_(self,claveJuez,nombreJuez,antiguedadJuez):
        self.claveJuez=claveJuez
        self.nombreJuez=nombreJuez
        self.antiguedadJuez=antiguedadJuez

    def listaJuez(self):
        j=Juez()
        j.claveJuez = int(input("Ingrese la clave del juez (int)\n>"))
        j.nombreJuez = str(input("Ingrese el nombre del Juez (str)\n>"))
        j.antiguedadJuez = int(input("ingrese sus años de servicion(int)\n>"))
        listJuez.appende(j)

class Atraco:
    def _init_(self,fechaAtraco,sentencia,condena):
        self.fechaAtraco=fechaAtraco
        self.sentencia=sentencia
        self.condena=condena

    def listaAtraco(self):
        a=Atraco()
        a.fechaAtraco = int(input("Ingrese la fecha del robo\n>"))
        a.sentencia = str("Ingrese la setencia a dar (int)\n>")
        a.condena = int(input("Ingrese los numeros de años a condeñar\n<"))
        listAtraco.append(a)
