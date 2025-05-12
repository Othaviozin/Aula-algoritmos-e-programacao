lista = []
a = "reprovado"
b = 0
for x in range(10):
    aluno = input("nome do aluno: ")
    lista.append(aluno)
    nota1 = float(input("digite a  Primeira   nota : "))
    nota2 = float(input("digite a  Segunda    nota : "))
    nota3 = float(input("digite a  Terceira   nota : "))
    nota4 = float(input("digite a  Quarta     nota : "))
    media = (nota1+nota2+nota3+nota4/4)
    if media >= 7:
        lista.append(media)
        b += 1
    else:
        lista.append(a)
print(lista)
print(f"numeros de alunos aprovados: {b}")

