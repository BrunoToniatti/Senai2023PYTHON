# Estações do ano

from calendario import o
from calendario import i
from calendario import v
from calendario import p


def exibir_menu():
    print('Escolha uma das opções')
    print('* 1 -> Pesqusiar por mês')
    print('* 2 -> Pesqusiar por mês e dia')
    print('* 0 -> Sair')

# Apresentação
print('\n\t\t\t --- Bem-Vindo(a) --- ')

# laço de repetiçãpo
while True:

    exibir_menu()
    opcao = int(input('-> '))

    if opcao == 1:
        print('Qual mês você deseja pesquisar?')
        mes = input('-> ')

        if mes.lower() in o:
            print(f'\n\t\t\t --> {mes} esta no outono, aproveite as cobertas e os banhos quentes =) <--')
        elif mes.lower() in i:
            print(f'\n\t\t\t --> {mes} esta no inverno, aproveite as cobertas <--')
        elif mes.lower() in p:
            print(f'\n\t\t\t --> {mes} esta na primavera, aproveite os parques <--')
        elif mes.lower() in v:
            print(f'\n\t\t\t --> {mes} esta no verão, aproveite as piscinas e as praias =) <--')

    elif opcao == 2:
        print('Qual mês você deseja pesquisar?')
        mes = input('-> ')
        print('Qual dia você gostaria de pesquisar?')
        dia = int(input('-> '))

        if mes.lower() in o:
            if (mes == 'mar' and dia >= 20):
                print('\n *** Outono ***\n')
            else:
                print('\n *** Verão *** \n')
        if mes.lower() in i:
            if (mes == 'jun' and dia >= 21):
                print('\n *** Inverno *** \n')
            else:
                print('\n **** Outono *** \n')
        if mes.lower() in p:
            if (mes == 'set' and dia >= 23):
                print('\n*** Primavera ***\n')
            else:
                print('\n *** Primavera *** \n')
        if mes.lower() in v:
            if (mes == 'dez' and dia >= 22):
                print('\n *** Verão ***\n')
            else:
                print('\n *** Primavera *** \n')


    elif opcao == 0:
        print('\n\t\t\t ***** Saindo do programa... Até mais =) *****')
        break


# Saída