numeros=(50,45,20,30,40,87)
#convierto tupla en lista
listaNumeros=list(numeros)

#recorro la lista
listaNumerosMayores=[]
for numero in listaNumeros:
    #condicion a  evaluar
    if(numero > 40):
        listaNumerosMayores.append(numero)
print(listaNumerosMayores)