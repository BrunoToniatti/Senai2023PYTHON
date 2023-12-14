class funcionario(object):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setSalario(self, salario):
        self.salario = salario

    def getSalario(self):
        return self.salario

    def calcular(self):
        if self.getSalario() >= 5000:
            inss = self.getSalario() * 0.1
            return inss

    def __str__(self):
        return (
                f'\n Nome: ' + str(self.getNome()) +
                f'\n Salario: ' + str(self.getSalario()) +
                f'\n INSS: ' + str(self.calcular())
        )
