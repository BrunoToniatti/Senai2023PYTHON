#Variaveis
descontoS = 528
SBase = 0

# Apresentação
print('\n\t\t\t -- CALCULO DE IMPOSTOS --')

# ENTRADA
NM = input('Nome: ')
SB = float(input('Salário Bruto: '))
NMRD = float(input('Número de Dependentes: '))

# Processamento

# DESCONTO POR DEPENDENTES
DPD = float(189.59 * NMRD)
# SALÁRIO BASE
if DPD < descontoS:
    SBase = float(SB - descontoS)
else:
    SBase = float(SB - DPD)

# SABER A ALIQUOTA
# MAIS VARIAVEIS

vlrAli = 0
dedu = 0
aliquotat = ''

if SBase <= 1903.98:
    aliquotat = 'Isento'
    vlrAli = 0
    dedu = 0

elif (SBase >= 1903.99) and (SBase <= 2826.65):
    aliquotat = '7.5%'
    vlrAli = 7.5
    dedu = 158.40

elif (SBase >= 2826.66) and (SBase <= 3751.05):
    aliquotat = '15.0%'
    vlrAli = 15
    dedu = 370.40

elif (SBase >= 3751.06) and (SBase <= 4664.68):
    aliquotat = '22.5%'
    vlrAli = 22.5
    dedu = 651.73

elif SBase > 4664.68:
    aliquotat = '27.5%'
    vlrAli = 27.5
    dedu = 884.96

transform = vlrAli / 100
IBc = SBase * transform

if IBc == 0:
    IB = 'Isento'

else:
    IB = IBc

if IB == 'Isento':
    IR = 'Isento'

else:
    IR = IB - dedu

if IR == 'Isento':
    SL = SB

else:
    SL = SB - IR

# SL = SB - IR

if SL == SB:
    aliquotaEfe = 'Isento'
else:
    aliquotaEfe = (IR / SB) * 100

# Saída

print(f'\n\t\t\t *** Aqui esta {NM} ***')
print(f'Salário Bruto = {SB}')
print(f'Numero de dependentes = {NMRD}')
print(f'Salário Base = {SBase}')
print(f'Aliquota = {aliquotat}')
if IR == 'Isento':
    print(f'IR devido = {IR}')
else:
    print(f'IR devido = {IR:.2f}')
print(f'Salário liquido = {SL}')
if aliquotaEfe == 'Isento':
    print(f'Aliquota efetiva = {aliquotaEfe}')
else:
    print(f'Aliquota efetiva = {aliquotaEfe:.2f}')