a = int(input("informe o valor inicial do intervalo ; "))
b = int(input("informe o valor final do intervalo ; "))
pares = "numeros pares: "
impares = "numeros impares"
for x in range(a,b) :
    if (x % 2 == 0 ):
        pares += str(x) + ""
    else:
        impares += str(x) + ""
print(impares)
print(pares)