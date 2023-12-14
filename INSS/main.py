# Interface do calculo de INSS

from calc import funcionario

print('\n\t\t\t -- CALCULO DE INSS -- \n')

# Entrada de dados

nome = input('Nome do funcionario: ')
sala = float(input(f'Salario do {nome}: '))

func = funcionario(nome, sala)

print(func)
