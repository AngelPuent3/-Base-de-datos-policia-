from Juez import *
from Banco import *
def mainP():
    print("**POlICIA**")
    print("Base de datos")
    print("-------------")
    print("1.-Juez\n2.Banco")
    opM=int(input(">"))
    if opM==1:
        main.jueMain()
    elif opM==2:
        bmain=Banco()
        bmain.mainBanco()
    else:
        exit("Adios :)")
mainP()


