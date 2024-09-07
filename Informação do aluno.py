turma = []
aluno = {}

while True:
    aluno['nome'] = str(input("Nome do aluno: "))
    aluno['idade'] = int(input("Idade do aluno: "))
    turma.append(aluno)
    escolha = str(input("Gostaria de adicionar outro aluno? [S/N]: ")).lower()
    if escolha != 's':
        break
