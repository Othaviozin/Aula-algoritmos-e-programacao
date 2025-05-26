
for x in range(10):
    numero = int(input("Informe um numero: "))
    if numero > 0:
        positivos += 1
    if numero < 0:
        negativos += 1
    else:
        print("zero informado")
print(positivos)
print(negativos)