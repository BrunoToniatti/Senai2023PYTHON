# Interface da calculadora

from calc2 import soma

# Apresentação
print('\n\t\t\t -- Calculadora 2 -- \n')

# Entrada
num1 = int(input('Informe o N1: '))
num2 = int(input('Informe o N2: '))

# Processamento
total = soma(num1, num2)

# Saida
print(f'{num1} + {num2} = {total}')
