def estado(sigla): # questao 4
    estados = {
        'SC': 'Santa Catarina',
        'PR': 'Paraná',
        'RS': 'Rio Grande do Sul',
        'MG': 'Minas Gerais',
        'SP': 'São Paulo',
        'RJ': 'Rio de Janeiro',
        'BA': 'Bahia',
        'CE': 'Ceará',
        'GO': 'Goiás',
        'AM': 'Amazonas',
        'PE': 'Pernambuco',
        'ES': 'Espírito Santo',
        'PB': 'Paraíba',
        'PA': 'Pará',
        'MA': 'Maranhão',
        'MT': 'Mato Grosso',
        'RN': 'Rio Grande do Norte',
        'AL': 'Alagoas',
        'MS': 'Mato Grosso do Sul',
        'DF': 'Distrito Federal',
        'PI': 'Piauí',
        'RO': 'Rondônia',
        'SE': 'Sergipe',
        'RR': 'Roraima',
        'TO': 'Tocantins',
        'AC': 'Acre',
        'AP': 'Amapá'
    }
    sigla = sigla.upper()
    return estados[sigla]
E = input("digite a sigla do seu estado :")
print(estado(E))