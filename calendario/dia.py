class data (object):
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano


    # Encapsulamento
    def setDia(self, dia):
        self.dia = dia

    def getDia(self):
        return self.dia

    def setMes(self, mes):
        self.mes = mes

    def getMes(self):
        return self.mes

    def setAno(self, ano):
        self.ano = ano

    def getAno(self):
        return self.ano

    # Processamento
    def VerMes(self):
        if (self.mes > 12) or (self.mes <= 0):
            print(f'\n Mês {self.mes} inválido')
        else:
            pass

    def verDia(self):
        if (self.dia <= 0) or (self.dia > 32):
            print(f'\n Dia {self.dia} inválido')
        else:
            pass

    def MesExis(self):
        if (self.dia > 28) and (self.mes == 2):
            print(f'\n No mês de janeiro não existe o dia {self.dia}')

        elif (self.dia > 30) and (self.mes == 4):
            print(f'\n No mês de abril não existe o dia {self.dia}')

        elif (self.dia > 30) and (self.mes == 6):
            print(f'\n No mês de junho não existe o dia {self.dia}')

        elif (self.dia > 29) and (self.mes == 7):
            print(f'\n No mês de julho não existe o dia {self.dia}')

        elif (self.dia > 30) and (self.mes == 9):
            print(f'\n No mês de Agosto não existe o dia {self.dia}')
