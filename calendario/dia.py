#def exibir_menu():

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
    def verDia(self):
        if (self.dia <= 0) or (self.dia > 32):
            print(f'\n Dia {self.dia} inválido')
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
            print(f'\n No mês de Setembro não existe o dia {self.dia}')

        elif (self.dia > 30) and (self.mes == 11):
            print(f'\n No mês de Novembro não existe o dia {self.dia}')

        else:
            pass

    def feriado(self):
        if (self.mes == 12) and (self.dia == 25):
            print('\n\t\t\t Feriado: Natal')
        elif (self.mes == 1) and (self.dia == 1):
            print('\n\t\t\t Feriado: Ano novo')
        elif (self.mes == 4) and (self.dia == 21):
            print('\n\t\t\t Feriado: Tiradentes')
        elif (self.mes == 5) and (self.dia == 1):
            print('\n\t\t\t Feriado: Dia do Trabalhador')
        elif (self.mes == 6) and (self.dia == 12):
            print('\n\t\t\t Feriado: Dia dos namorados')
        elif (self.mes == 9) and (self.dia == 7):
            print('\n\t\t\t Feriado: Independencia do Brasil')
        elif (self.mes == 10) and (self.dia == 12):
            print('\n\t\t\t Feriado: Nossa Senhora Aparecida')
        elif (self.mes == 11) and (self.dia == 2):
            print('\n\t\t\t Feriado: Finados')
        elif (self.mes == 11) and (self.dia == 15):
            print('\n\t\t\t Feriado: Proclamação da Republica')

    def __str__(self):
        return(
               f'\nData: {self.getDia()}/{self.getMes()}/{self.getAno()}'
               )
