def ehPrimo(n, divisor=2):
    if n < 2:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return ehPrimo(n, divisor + 1)

numero = int(input("digite um numero :"))
if ehPrimo(numero):
    print("é primo")
else:
    print("nao é primo")

