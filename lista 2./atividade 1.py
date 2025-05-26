meses = {
    1:'janeiro',
    2:'fevereiro',
    3:'março',
    4:'abril',
    5:'maio',
    6:'junho',
    7:'julho',
    8:'agosto',
    9:'setembro',
    10:'outubro',
    11:'novembro',
    12:'dezembro',
}

datinha = input("aaa   ")

def data(vardata):
    DD = vardata[0:2]
    MM = vardata[2:4]
    YYYY = vardata[4:8]
    return '{}/{}/{}'.format(DD, MM, YYYY)

print(data(datinha))
