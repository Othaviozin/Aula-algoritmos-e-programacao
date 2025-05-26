while True:
    def formatar_data(data):
        meses = {
            '01': 'janeiro', 
            '02': 'fevereiro',
            '03': 'março', 
            '04': 'abril',
            '05': 'maio',
            '06': 'junho',
            '07': 'julho',
            '08': 'agosto',
            '09': 'setembro',
            '10': 'outubro',
            '11': 'novembro',
            '12': 'dezembro',
        }

        try:
            dia, mes, ano = data.split('/')
            if len(dia) == 2 and len(mes) == 2 and len(ano) == 4:
                if mes in meses and 1 <= int(dia) <= 31:
                    return f"{dia} de {meses[mes]} de {ano}"
                elif dia > 28 and mes == 2: # tentativa falha de adicionar o mes de fevereiro no script
                    return ("o mes de fevereiro tem somente 28 dias ")

        except:
            return None  # Retorna NULL (opção invalida)
    
    if data == 0:
        exit()
    else:
        data = input("digite sua data (DD/MM/YYYY) : ")
        resultado = formatar_data(data)
        print(resultado)
        print("digite 0 para sair")
    
