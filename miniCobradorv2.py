from ast import Try

lista_ptos = [
    [1,"Leche",2000], 
    [2,"pan", 1500], 
    [3,"huwvos", 10000], 
    [4,"cafe", 5350]]
cuenta =[]

def agregar_producto():
    while(True):
        try:
            codigo = int(input("Ingrese el código del producto: "))
            break
        except:
            print("")
            print("Error el codigo solo debe ser numeros.")
            print("")
        nompto = ""
        while(len(nompto)<3):
            nompto = input("Ingrese nombre del producto: ").lower()
            if(len(nompto)<3):
                print("El nombre del producto debe tener al menos 3 caracteres")
        while(True):
            try:
                precio = int(input("Ingrese el precio del producto: "))
                break
            except:
                print("")
                print("Error el precio solo debe ser numeros.")
                print("")
        lista_ptos.append([codigo,nompto,precio])
        print("Producto registrado correctamente")
        print("")

def eliminar_producto():
    #print(lista_ptos)
    #print("Lista de productos: %s" % lista_ptos)
    print("{:<8} {:<15} {:<10}".format('codigo','nombre','precio'))
    for elemento in lista_ptos:
        codigo,nombre,precio = elemento
        print("{:<8} {:<15} {:<10}".format(codigo,nombre,precio))
    encontrado = False
    while(True):
        try:
            print("")
            codigo = int(input("Ingrese el código del producto a eliminar: "))
            break
        except:
            print("")
            print("Error el codigo solo debe ser numeros.")
            print("")
    for i in range(len(lista_ptos)):
        if(codigo==lista_ptos[i][0]):
            encontrado = True
            pos = i
            break
    if(encontrado):
        print("")
        print("Producto a eliminar")
        print(lista_ptos[i][1])
        print("")
        print("Lista de productos actualizada")
        del lista_ptos[i]
        #print(lista_ptos)
        print("{:<8} {:<15} {:<10}".format('codigo','nombre','precio'))
        for elemento in lista_ptos:
            codigo,nombre,precio = elemento
            print("{:<8} {:<15} {:<10}".format(codigo,nombre,precio))
            print("")
    else:
        print("Producto no encontrado")
        print("")

def agregar_producto_cuenta():
    #print(lista_ptos)
    print("{:<8} {:<15} {:<10}".format('codigo','nombre','precio'))
    for elemento in lista_ptos:
        codigo,nombre,precio = elemento
        print("{:<8} {:<15} {:<10}".format(codigo,nombre,precio))
    encontrado = False
    while(True):
        try:
            print("")
            codigo = int(input("Ingrese el código del producto que desea agregar a la cuenta: "))
            break
        except:
            print("")
            print("Error el codigo solo debe ser numeros.")
            print("")
    for i in range(len(lista_ptos)):
        if(codigo==lista_ptos[i][0]):
            encontrado = True
            pos = i
            break
    if(encontrado):
        print("")
        cuenta.extend([lista_ptos[i]])
        print("Se ha añadido el sioguiente producto a la cuenta: ")
        print(cuenta[i][1])
        print("")
    else:
        print("Producto no encontrado")
        print("")

def eliminar_producto_cuenta():
    #print(cuenta)
    print("{:<8} {:<15} {:<10}".format('codigo','nombre','precio'))
    for elemento in cuenta:
        codigo,nombre,precio = elemento
        print("{:<8} {:<15} {:<10}".format(codigo,nombre,precio))
    encontrado = False
    while(True):
        try:
            print("")
            codigo = int(input("Ingrese el código del producto que desea eliminar de la cuenta: "))
            break
        except:
            print("")
            print("Error el codigo solo debe ser numeros.")
            print("")
    for i in range(len(cuenta)):
        if(codigo==cuenta[i][0]):
            encontrado = True
            pos = i
            break
    if(encontrado):
        print("")
        print("Producto a eliminar")
        print(cuenta[i][1])
        print("")
        print("Lista de productos actualizada")
        del cuenta[i]
        print("{:<8} {:<15} {:<10}".format('codigo','nombre','precio'))
        for elemento in cuenta:
            codigo,nombre,precio = elemento
            print("{:<8} {:<15} {:<10}".format(codigo,nombre,precio))
        #print(cuenta)
        print("")
    else:
        print("Producto no encontrado")
        print("")

def cobrar():
    print("")
    #print(cuenta)
    print("{:<8} {:<15} {:<10}".format('codigo','nombre','precio'))
    for elemento in cuenta:
        codigo,nombre,precio = elemento
        print("{:<8} {:<15} {:<10}".format(codigo,nombre,precio))
    suma_total = 0
    for i in range(len(cuenta)):
        suma_total += cuenta[i][2]
    print("El total de su compra es de: $" + str(suma_total))

while(True):
    print("----------CAJA REGISTRADORA----------")
    print("")
    print("Ingresa una opción:")
    print("1. Agregar producto ")
    print("2. Remover producto ")
    print("3. Añadir a la cuenta")
    print("4. Retirar de la cuenta")
    print("5. Cobrar")
    print("0 Salir")
    print("")

    try:
        op = int(input("Ingrese una opción: "))
        if(op ==1):
            agregar_producto()
        elif(op ==2):
            eliminar_producto()
        elif(op ==3):
            agregar_producto_cuenta()
        elif(op ==4):
            eliminar_producto_cuenta()
        elif(op ==5):
            cobrar()
        elif(op ==0):
            print("")
            print("Gracias por su compra")
            break
        else:
            print("")
            print("Error ingrese una opción valida")
            print("")
    except:
        print("")
        print("Error volviendo al menu principal...")
        print("")