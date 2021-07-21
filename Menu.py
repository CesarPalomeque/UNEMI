def menu():
    print("1)calculadora")
    print("2) numero")
    print("3)listas")
    print("4)cadenas")
    print("5)salir")
    opc= input("Elija la opcion[1....5]: ")

    if opc == "1":
        print("calculadora")

    elif opc == "2":
        print(" Operaciones con Numero") 
        print("1)Perfecto")
        print("2)Primo")
        print("3)salir")
        opc2= input("Elija la opcion[1....5]: ")
        if opc2 == "1":
            print("Numeros perfectos")
            num=int(input("Ingrese Numero: "))
            print("El numero ")
    elif opc == "3":
        print("listas")    
    elif opc == "4":
        print("cadenas ")   
    elif opc == "5":
        print("salir")    

menu()                   


# titulo=Menu principal
# opciones=[
#     1 claculadora
#     2 numero
#     3 listas
#     4 calculos salir ]