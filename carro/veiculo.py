# Classe Veículo

def exibir_menu():
    print('Escolha uma opção de 0-4')
    print('1 - 100km/h')
    print('2 - 80km/h')
    print('3 - 60km/h')
    print('4 - 40km/h')
    print('5 - 20km/h')
    print('0 - 0km/h')

class Veiculo(object):
    # Médoto construtor
    def __init__(self, marca, modelo, cor, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = velocidade

    # Encapsulamento
    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def setCor(self, cor):
        self.cor = cor

    def getCor(self):
        return self.cor

    def setVelocidade(self, velocidade):
        self.velocidade = velocidade

    def getVelocidade(self):
        return self.velocidade

    # Retorno de dados da classe
    def __str__(self):
        return(
            '\n Marca: ' + str(self.getMarca()) +
            '\n Modelo: ' + str(self.getModelo()) +
            '\n Cor: ' + str(self.getCor()) +
            '\n Velocidade: ' + str(self.getVelocidade()) + 'km\h'
        )

    # Método acelerar
    def acelerar(self):
        if self.velocidade < 120:
            self.velocidade += 1
        # self.velocidade = self.velocidade + 1

    # Método frear
    def frear (self):
        print('\n Seu carro está a 120 km/h, tem um radar de 100 km/h deseja frear? (s/n)')
        x = input('-> ')

        if x == 's':
            print('\n Deseja ir para qual velocidade? ')
            exibir_menu()
            op = int(input('-> '))

            for i in range (0, 200):
                
                if op == 1:
                    if self.velocidade > 100:
                        self.velocidade -= 1

                if op == 2:
                    if self.velocidade > 80:
                        self.velocidade -= 1

                if op == 3:
                    if self.velocidade > 60:
                        self.velocidade -= 1

                if op == 4:
                    if self.velocidade > 40:
                        self.velocidade -= 1

                if op == 5:
                    if self.velocidade > 20:
                        self.velocidade -= 1

                if op == 0:
                    if self.velocidade > 0:
                        self.velocidade -= 1


        if x == 'n':
            print('Acabou de levar uma multa e uns pontinhos na carteira. =(')
