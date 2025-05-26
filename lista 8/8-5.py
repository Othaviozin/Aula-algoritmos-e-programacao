lista0 = [1,2,3,4,5,6,7,8,9,10]
lista1 = [2,3,4,6,9,2,2,1,0,9]
def crescente(lista):
    ordem = sorted(lista)
    if ordem == lista:
        return "Essa lista ja está ordenada crescentemente"
    else:
        return "essa lista nao esta ordenada crescentemente"

print(crescente(lista0))
print(crescente(lista1))