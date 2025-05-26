ordem = ("Primeiro ","Segundo ","Terceiro ","Quarto ","Quinto ")
nome = (input("nome do participante:"))
soma = 0
saltos = []
for k in ordem:
    print(k)
    salto = float(input(""))
    saltos.append(salto)
    soma += salto

media = soma/5
y = 0

print(f"resultado final:")
print(f"Nome do competidor : {nome}")

for x in ordem: 
    print(f"O {x} salto foi de :", saltos[y])
    y += 1
    


print(f"A média do competidor {nome} é : {media}")