# Interface da calculadora

from bruno2 import div
from bruno2 import mult

# Apresentação
print('\n\t\t\t -- brunodiv -- \n')

# entrada
num1 = int(input('Informe o N1: '))
num2 = int(input('Informe o N2: '))

# prcessamento
total = div(num1, num2)

print(f'{num1} / {num2} = {total}')

# apresentação2
print('\n\t\t\t -- brunomult -- \n')

# entrada2
num3 = int(input('Informe o N3: '))
num4 = int(input('Informe o N4: '))


# Processamento
total2 = mult(num3, num4)

print(f'{num3} * {num4} = {total2}')

resultado = total + total2

print('\n\t\t\t -- contafinal -- \n')

# saida
print(f' result : {total} + {total2} = {resultado}')


