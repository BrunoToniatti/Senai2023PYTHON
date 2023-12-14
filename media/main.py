from calc import estudante

print('\n\t\t\t -- CALCULO MÉDIA BIMESTRAL -- \n')

nome = input('Nome: ')
b1 = input('1 Bimestre: ')
b2 = input('2 Bimestre: ')
b3 = input('3 Bimestre: ')
b4 = input('4 Bimestre: ')

med = estudante(nome, b1, b2, b3, b4)

print(med)
