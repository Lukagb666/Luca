rta="si"
        #rta!="no":
while rta=="si":# condición a evaluar
     opcion=input("menú de opciones\n1-saludo\n2-despedida\n3-salir")
     if opcion=="1":
        print ("hola")
    elif opcion=="2": 
         print ("chau")
    elif opcion=="3":
         print ("saliendo del sistema")
       break #
    else:
    print ("la opcion ingresada es invalida")