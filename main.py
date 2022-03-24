#LISTAS
valores=[1,2,3,4,5]

#TUPLA
valoresTupla=(1,2,3,4,5)
print(valoresTupla)

#for valor in valoresTupla:
#    print(valor)

#accediendo a elemento de tupla
#print(valoresTupla[0])
#valoresTupla.append(6)
#print(valoresTupla)

#Transformemos una tupla en una lista
listaValores=list(valoresTupla)
print(listaValores)
listaValores.append(6)
valoresTupla=tuple(listaValores)
print(valoresTupla)