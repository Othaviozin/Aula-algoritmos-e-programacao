def triangulo(a, b, c):
    if (a + b) <= c or (b + c) <= a or (a + c) <= b:
        return "Nao forma triangulo"
    elif a == b and b == c:
        return "equilatero"
    elif a != b and b != c and a != c:
        return "escaleno"
    else:
        return "isoceles"

cateto1 = float(input("Digite o primeiro cateto: "))
cateto2 = float(input("Digite o segundo cateto: "))
cateto3 = float(input("Digite o terceiro cateto: "))

print(triangulo(cateto1, cateto2, cateto3))
