
#gestionando stock en python

"""
vamos a hacer distintos diccionarios que alamacenen 
dos claves-valor que representarian la cantidad y el eleento, cada diccionario
vendria a ser una posicion en el almacen, haremos la prueba con un minideposito de 5 posiciones 
"""

posicion1 = {'elemento':"objeto1",'cantidad':0}
posicion2 = {'elemento':"objeto2",'cantidad':0}
posicion3 = {'elemento':"objeto3",'cantidad':0}
posicion4 = {'elemento':"objeto4",'cantidad':0}
posicion5 = {'elemento':"objeto5",'cantidad':0}

#creando el menu principal
def menu():
    opcion = None
    while opcion != 5:
        print("*************")
        print("Esta ingresando al sistema de gestion del almacen, digite una opcion")
        print("*************")
        print("digite 1 si usted desea ingresar elemento y cantidad a una posicion o ver stock \n digite 2 si usted desea retirar stock\n digite 3 si desea agregar material en una posicion especifica\n digite 4 si desea ver stock \n digite 5 si desea salir")

        opcion = int(input("opcion: "))
        if opcion == 1:
            print("ingresando..")
            ingreso()
        elif opcion == 2:
            print("sacando..")
            retiro()
        elif opcion == 3:
            print("agregando..")
            agregarMaterial()
        elif opcion == 4:
            mostrar()
        elif opcion == 0 or opcion > 5:
            print("opcion erronea")
        else:
            print("finalizando")
            break



#ceando funcion que muestre stock
def mostrar():
    print(f'en posicion 1: {posicion1} \n en posicion 2:  {posicion2} \n en posicion 3: {posicion3 } \n en posicion 4:  {posicion4} \n en posicion 5:  { posicion5}')
# creando funcion de ingreso de mercaderia

def ingreso():
    print(f'posiciones del amlacen \n posicion1: {posicion1},\n posicion 2: {posicion2},\n posicion3: {posicion3},\n posicion4: {posicion4},\n posicion5: {posicion5}')
    opcion = None
    print("en que posicion desea ingresar mercancia?")
    opcion = int(input("digite posicion: "))

    if opcion == 1:
        print("va a ingresar en la opcion 1, digite material y cantidad a ingresar")
        posicion1['elemento']=input("ingrese elemento: ")
        posicion1['cantidad']=int(input("ingrese cantidad: "))
        print(f'Posicion 1 : { posicion1}')
    elif opcion == 2:
        print("va a ingresar en la opcion 2, digite material y cantidad a ingresar")
        posicion2['elemento'] = input("ingrese elemento: ")
        posicion2['cantidad'] = int(input("ingrese cantidad: "))
        print(f'Posicion 2 : {posicion2}')
    elif opcion == 3:
        print("va a ingresar en la opcion 3, digite material y cantidad a ingresar")
        posicion3['elemento']=input("ingrese elemento: ")
        posicion3['cantidad']=int(input("ingrese cantidad: "))
        print(f'Posicion 3 : { posicion3}')
    elif opcion ==4 :
        print("va a ingresar en la opcion 4, digite material y cantidad a ingresar")
        posicion4['elemento'] = input("ingrese elemento: ")
        posicion4['cantidad'] = int(input("ingrese cantidad: "))
        print(f'Posicion 4 : {posicion4}')
    elif opcion == 5:
        print("va a ingresar en la opcion 5, digite material y cantidad a ingresar")
        posicion5['elemento'] = input("ingrese elemento: ")
        posicion5['cantidad'] = int(input("ingrese cantidad: "))
        print(f'Posicion 5 : {posicion5}')
    else:
        print("opcion incorrecta")



#creando funcion de retiro de mercaderia
def retiro():
    print(f'en posicion 1: {posicion1} \n en posicion 2:  {posicion2} \n en posicion 3: {posicion3 } \n en posicion 4:  {posicion4} \n en posicion 5:  { posicion5}')
    opcion = None
    print("de que posicion desea retirar mercancia?")
    opcion = int(input("digite posicion: "))
    if opcion == 1:
        print("va a ingresar en la opcion 1, digite material y cantidad a retirar")
        print(posicion1['elemento'])
        posicion1['cantidad'] =posicion1['cantidad']- int(input("ingrese cantidad: "))
        print(f'Posicion 1 : {posicion1}')
    elif opcion == 2:
        print("va a ingresar en la opcion 2, digite material y cantidad a retirar")
        print(posicion2['elemento'])
        posicion2['cantidad'] =posicion2['cantidad'] - int(input("ingrese cantidad: "))
        print(f'Posicion 2 : {posicion2}')
    elif opcion == 3:
        print("va a ingresar en la opcion 3, digite material y cantidad a retirar")
        print(posicion3['elemento'])
        posicion3['cantidad'] = posicion3['cantidad'] - int(input("ingrese cantidad: "))
        print(f'Posicion 3 : {posicion3}')
    elif opcion == 4:
        print("va a ingresar en la opcion 4, digite material y cantidad a retirar")
        print(posicion4['elemento'])
        posicion4['cantidad'] = posicion4['cantidad'] - int(input("ingrese cantidad: "))
        print(f'Posicion 4 : {posicion4}')
    elif opcion == 5:
        print("va a ingresar en la opcion 5, digite material y cantidad a retirar")
        print(posicion5['elemento'])
        posicion5['cantidad'] = posicion5['cantidad'] - int(input("ingrese cantidad: "))
        print(f'Posicion 5 : {posicion5}')
    else:
        print("opcion incorrecta")


#agregando material a posicion indicada
def agregarMaterial():
    print(
        f'posiciones del amlacen posicion1: {posicion1}, posicion 2: {posicion2}, posicion3: {posicion3}, posicion4: {posicion4}, posicion5: {posicion5}')
    opcion = None
    print("en que posicion desea agregar mercancia?")
    opcion = int(input("digite posicion: "))
    if opcion == 1:
        print("va a ingresar en la posicion 1, digite cantidad a ingresar")
        print(posicion1['elemento'])
        posicion1['cantidad'] = posicion1['cantidad'] + int(input("ingrese cantidad: "))
        print(f'Posicion 1 : {posicion1}')
    elif opcion == 2:
        print("va a ingresar en la posicion 2, digite  cantidad a ingresar")
        print(posicion2['elemento'])
        posicion2['cantidad'] = posicion2['cantidad'] + int(input("ingrese cantidad: "))
        print(f'Posicion 2 : {posicion2}')
    elif opcion == 3:
        print("va a ingresar en la posicion 3, digite  cantidad a ingresar")
        print(posicion3['elemento'])
        posicion3['cantidad'] = posicion3['cantidad'] + int(input("ingrese cantidad: "))
        print(f'Posicion 3 : {posicion3}')
    elif opcion == 4:
        print("va a ingresar en la posicion 4, digite  cantidad a ingresar")
        print(posicion4['elemento'])
        posicion4['cantidad'] = posicion4['cantidad'] + int(input("ingrese cantidad: "))
        print(f'Posicion 4 : {posicion4}')
    elif opcion == 5:
        print("va a ingresar en la posicion 5,  cantidad a ingresar")
        print(posicion5['elemento'])
        posicion5['cantidad'] = posicion5['cantidad'] + int(input("ingrese cantidad: "))
        print(f'Posicion 5 : {posicion5}')
    else:
        print("opcion incorrecta")



menu()


