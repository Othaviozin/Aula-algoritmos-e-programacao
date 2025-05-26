perguntas = ["Telefonou para a vítima?",
"Esteve no local do crime?",
"Mora perto da vítima?",
"Devia para a vítima?",
"Já trabalhou com a vítima?"]
sim = ["sim","Sim","S","s"]
sins = 0
for x in perguntas:
    print (x)
    resposta =(input(""))
    if resposta in sim:
        sins += 1

if sins == 2:
    print("suspeito...")
elif sins == (3 or 4):
    print("cumplice")
elif sins == 5:
    print("culpado")
else:
    print("inocente")
