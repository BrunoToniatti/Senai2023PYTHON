# Cadastro de alunos




nome = str(input('Qual o nome do aluno: '))
nota = float(input('Qual a nota do aluno: '))
matricula = bool(input('O aluno está matriculado: '))
curso = str(input('Qual o curso do aluno: '))

if matricula == False:
    print(f'\n\t\t\t O aluno {nome} não está matriculado')




while matricula:

    x = {'Nome': nome, 'Nota': nota, 'Matricula': matricula, 'Curso': curso}
    z = input('\n\t\t\t Oque você gostaria de ver no cadastro do aluno? (Nome, Nota, Curso) ')

    if z == 'Nome':
        print(x['Nome'])

    elif z == 'Nota':
        print(x['Nota'])

    elif z == 'Curso':
        print(x['Curso'])

    else:
        break
