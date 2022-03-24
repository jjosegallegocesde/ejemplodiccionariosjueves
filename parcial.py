print("Menu")
print("....")
print("1. Agregar")
print("2. Mostrar")
print("3. Editar")
print("4. Eliminar")
print("0. SALIR")

opcion=1
productos=[]
while(opcion !=0):
    opcion=int(input("Digite una opcion: "))
    if(opcion==1):
        producto={}
        #Llenando el diccionario
        producto['codigo']=input("Digita el codigo de producto: ")
        producto['nombre']= input("ingrese el nombre del producto: ")
        producto['precio']= int(input("ingrese el precio del producto: "))
        #Llenando la lista
        productos.append(producto)
    elif(opcion==2):
        print(productos)
    elif(opcion==3):
        bandera=True
        codigoBuscado=input("Digite un codigo a buscar")
        for producto in productos:
            if(producto['codigo']==codigoBuscado):
                producto['precio']= int(input("ingrese el precio del producto: "))
                bandera=True
                break
            else:
                bandera=False
        if(bandera==False):
            print("Producto no encontrado")
                
    else:
        print("En construccion")