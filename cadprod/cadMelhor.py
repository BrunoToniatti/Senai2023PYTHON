# Cadastro de produtos
# Adicionando o produto

class Produto:
    def __init__(self, nome, descricao, preco_unitario, quantidade, disponivel):
        self.nome = nome
        self.descricao = descricao
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.disponivel = disponivel

    def calcular_valor_total(self):
        return self.preco_unitario * self.quantidade

    def exibir_produto(self):
        print(f"Nome: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Preço Unitário: R${self.preco_unitario:.2f}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Disponível: {self.disponivel}")
        print(f"Valor Total: R${self.calcular_valor_total():.2f}")
        print("===================================================")


class SistemaInformacao:
    def __init__(self):
        self.produtos = []

    def cadastrar_produto(self, produto):
        self.produtos.append(produto)

    def exibir_produtos(self):
        for produto in self.produtos:
            produto.exibir_produto()

    def editar_produto(self, nome, descricao, novo_preco_unitario, nova_quantidade, nova_disponibilidade):
        for produto in self.produtos:
            if produto.nome == nome:
                produto.descricao = novo_descricao
                produto.preco_unitario = novo_preco_unitario
                produto.quantidade = nova_quantidade
                produto.disponivel = nova_disponibilidade
                print(f"Produto '{nome}' editado com sucesso.")
                return
        print(f"Produto '{nome}' não encontrado.")

    def remover_produto(self, nome: object) -> object:
        for produto in self.produtos:
            if produto.nome == nome:
                self.produtos.remove(produto)
                print(f"Produto '{nome}' removido com sucesso.")
                return
        print(f"Produto '{nome}' não encontrado.")

    def calcular_valor_total_estoque(self):
        valor_total = sum(produto.calcular_valor_total() for produto in self.produtos)
        return valor_total

def exibir_menu():
    print("1. Cadastrar Produto")
    print("2. Exibir Produtos")
    print("3. Editar Produto")
    print("4. Remover Produto")
    print("5. Calcular Valor Total do Estoque")
    print("6. Sair")

from senha import senha

produto = []
sistema = SistemaInformacao()

x = input('Coloque sua senha de acesso? ')

if x != senha:
    print('\n\t\t\t ==== Você não tem acesso a adicionar produtos ====')

else:
    y = 's'

    while True:
        exibir_menu()
        opcao = input('Escolha uma opção de (1-6): ')

        if opcao == '1':
            nome = input('Digite o nome do produto: ')
            descricao = input('Digite a descrição do produto: ')
            preco_uni = float(input('Digite o preço unitário do produto: '))
            quantidade = int(input('Digite a quantidade do produto: '))
            disponivel = input('O produto está disponível? (Sim ou Não) ')

            novo_produto = Produto(nome, descricao, preco_uni, quantidade, disponivel)
            sistema.cadastrar_produto(novo_produto)

            print('\n\t\t\t >>>>> Produto cadastrado com sucesso! <<<<<\n')

        elif opcao == '2':
            print('\n\t\t\t >>>>>>> Produtos cadastrados: <<<<<<<< ')
            sistema.exibir_produtos()
            print()

        elif opcao == '3':
            nome = input('Digite o nome do produto que deseja alterar: ')
            novo_descricao = input('Digite a nova descrição: ')
            novo_preco = float(input('Digite o novo preço uniário: '))
            novo_quantidade = int(input('Digite a nova quantidade: '))
            novo_disponibilidade = input('Digite a nova disponibilidade: (Sim ou Não) ')

            sistema.editar_produto(nome, novo_descricao, novo_preco, novo_quantidade, novo_disponibilidade)
            print()

        elif opcao == '4':
            nome = input('Digite o nome do produto que deseja remover: ')
            sistema.remover_produto(nome)
            print()

        elif opcao == '5':
            valor_total_estoque = sistema.calcular_valor_total_estoque()
            print(f'Valor total do estoque: R${valor_total_estoque:.2f}\n')

        elif opcao == '6':
            print('Saindo do programa. Até Mais!')
            break