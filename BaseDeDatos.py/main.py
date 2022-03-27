
def mainP():
    print("**POlICIA**")
    print("Base de datos")
    print("-------------")
    print("1.-Juez\n2.Banco")
    opM=int(input(">"))
    if opM==1:
        from Juez import MenuJuez
        main1=MenuJuez()
        main1.mainJuez()
    elif opM==2:
        from bancos import MenuBanco
        main1=MenuBanco()
        main1.mainBanco()
    else:
        exit("Adios :)")
mainP()


