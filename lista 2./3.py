print("numeros primos entre 1 e 1000 : ")
for i in range(2,1001):
    primo = True
    for j in range(i-1,i,-1):
        if (i % j == 0):
            primo = False
            break
        if (primo):
            print(j)
