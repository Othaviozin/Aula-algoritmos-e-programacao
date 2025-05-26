lista = []
a = 0
b = 0
for x in range (10):
  letra = input("digite uma letra : ")
  if letra in "AaEeIiOoUu":
    a += 1
  else:
    b += 1
print(f"numero de consoantes {b}, Numero de vogais {a}")