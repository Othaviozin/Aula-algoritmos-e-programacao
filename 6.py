meses = ["janeiro","fevereiro", 'março', 'abril', 'maio', 
'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
temperatura = []
for x in range(12):
    temperatura.insert(x,float(input(f"informe a média de temperatura do mes {meses[x]}")))
media = 0
for x in range(12):
    media += temperatura[x]
media = media / 12
if temperatura >= media:
print(meses)

