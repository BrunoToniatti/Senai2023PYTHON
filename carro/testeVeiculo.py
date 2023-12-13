# Arquivo com código de teste da classe Veículo

from veiculo import Veiculo

minhaCaranga = Veiculo('Fiat', '147', 'Amarelo', 0)

#Exibindo a minha caranga
print('\n\t\t\t -- Minha Caranga --\n')
print(minhaCaranga)

# Acelerando a minha caranga
for i in range(0, 200):
    minhaCaranga.acelerar()

#Exibindo a minha caranga acelerada
print('\n\t\t\t -- Minha Caranga Acelerada --\n')
print(minhaCaranga)


# Freando minha caranga
minhaCaranga.frear()

#Exibindo a minha caranga freada
print('\n\t\t\t -- Minha Caranga Freada --\n')
print(minhaCaranga)

