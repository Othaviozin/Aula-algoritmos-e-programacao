listaum = []
listadois = []
listatres = []
for i in range(10):
    elemento = input("digite um elemento da primeira lista")
    listaum.append(elemento)
for i in range(10):
    elemento = input("digite um elemento da lista dois: ")
    listadois.append(elemento)
j = 0
for k in listaum:
    listatres.append(k)
    listatres.append(listadois[j])
    j += 1
    
print(listaum)
print(listadois)
print(listatres)
