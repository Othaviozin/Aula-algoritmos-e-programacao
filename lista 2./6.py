meses = ["janeiro","fevereiro", 'março', 'abril', 'maio', 
'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
soma =  0
temperatura = []
temp = 0
media = 0
for x in range(1,13):
    temp = (float(input(f"informe a média de temperatura do mes {meses[x]}")))
    temperatura.append(temp)
    soma += temp

for x in range(1,13):
    media += temperatura[x]
    media = media / 12
if temperatura >= media:
    print(meses)

