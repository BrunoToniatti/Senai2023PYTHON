# Calendario
from dia import data

# Apresentação
print('\n\t\t\t -- CALENDARIO --')
while True:

    d = int(input('Dia: '))
    m = int(input('Mes: '))
    a = int(input('Ano: '))

    dia = data(d,m,a)

    print(dia)

    dia.VerMes()
    dia.verDia()
    dia.MesExis()
    dia.feriado()

    op = input('\n Deseja pesquinar novamente? (s/n) \n')

    if op.lower() == 'n':
        break
