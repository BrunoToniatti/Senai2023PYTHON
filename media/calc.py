class estudante(object):
    def __init__(self, nome, nota1, nota2, nota3, nota4):
        self.nome = nome
        self.nota1 = float(nota1)
        self.nota2 = float(nota2)
        self.nota3 = float(nota3)
        self.nota4 = float(nota4)

    def setNome(self, nome):
        self.nome = nome
    def getNome(self):
        return self.nome

    def setNota1(self, nota1):
        self.nota1 = nota1
    def getNota1(self):
        return self.nota1

    def setNota2(self, nota2):
        self.nota2 = nota2
    def getNota2(self):
        return self.nota2

    def setNota3(self, nota3):
        self.nota3 = nota3
    def getNota3(self):
        return self.nota3

    def setNota4(self, nota4):
        self.nota4 = nota4
    def getNota4(self):
        return self.nota4

    def media(self):
        mediaB = (self.getNota1() + self.getNota2() + self.getNota3() + self.getNota4()) / 4
        return mediaB

    def __str__(self):
        return(
            f'\n Nome: ' + str(self.getNome()) +
            f'\n 1Bimestre: ' + str(self.getNota1()) +
            f'\n 2Bimestre: ' + str(self.getNota2()) +
            f'\n 3Bimestre: ' + str(self.getNota3()) +
            f'\n 4Bimestre: ' + str(self.getNota4()) +
            '\n Média Bimestral: {:.2f}'.format(self.media())
        )
