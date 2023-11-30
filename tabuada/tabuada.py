# tabuada

print('\n\t\t\t --- Bem Vindo a Tabuada em Python --- \n')

nmr = int(input('Informe o número para realizar a tabuada: '))
contador = 0
mult = -1

print('\n\t\t\t TABUADA DO', nmr)

while contador <= 10:
    mult += 1
    total = nmr * mult
    contador += 1
    print('\t\t\t', nmr, 'X', mult, '=', total)