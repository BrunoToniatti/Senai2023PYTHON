# Cadastro de produtos
# Adicionando o produto

from senha import senha

produto = []

x = input('Coloque sua senha de acesso? ')

if x != senha:
    print('\n\t\t\t ==== Você não tem acesso a adicionar produtos ====')

else:
    y = 's'

    while y == 's':
        nome = input('Nome do prduto: ')
        desc = input(f'Descrição de {nome}: ')
        preco = float(input(f'Qual o valor de {nome}: R$'))
        quantidade = int(input(f'Qual a quantidade de {nome}: '))

        quantidadetotal = float(preco*quantidade)

        prodinfo = {
            'Nome': nome,
            'Descrição': desc,
            'Preço': preco,
            'Estoque': quantidade,
            'qtdtotal': quantidadetotal
            }

        y = input('Deseja adicionar outro produto? s/n ')

        produto.append(prodinfo)

    print('\n\t\t\t Produtos cadastrados \n =========================================')

    for prodinfo in produto:

        print(f'-> Produto: {prodinfo['Nome']}')

        if prodinfo['Estoque'] > 0:
            pass
        else:
            print('->Produto sem estoque!')

        print(f'-> Descrição: {prodinfo['Descrição']}')
        print(f'-> Preço: {prodinfo['Preço']}')
        print('-> Preço total: {:.2f}'.format(prodinfo['qtdtotal']))
        print('====================================================')
