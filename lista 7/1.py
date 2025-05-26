opcoes= {
    1 : 'Adicionar item',
    2 : 'Remover item',
    3 : 'Exibir item',
    4 : 'ordernar o conjunto alfabeticamente',
    5 : 'verificar se um item esta na lista',
    6 : 'gravar lista em um arquivo',
    7 : 'ler a lista de comprar de um arquivo',
    8 : 'sair'
}
lista = []

while True:
    for l, k in opcoes.items():
        print(F"{l}-{k}")
    print("")

    op = int(input("informe qual opção deseja acessar: "))

    match op:
        case 1:
            x = input("adicione algo a sua lista: ")
            lista.append(x)
        case 2:
            print()
        case 3:
            print(lista)
            print("")
        case 4:
            print()
        case 5:
            print()
        case 6:
            print()
        case 7:
            print()
        case 8:
            break

    
    


        
