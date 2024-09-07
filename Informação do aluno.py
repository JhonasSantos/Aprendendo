turma = []
aluno = {}

print("Registro de Alunos")
while True:
    aluno['nome'] = str(input("Nome do aluno: "))
    aluno['idade'] = int(input("Idade do aluno: "))
    turma.append(aluno.copy())
    escolha = str(input("Gostaria de registrar mais algum aluno? [S/N]: ")).lower()
    if escolha != "s":
        break

for a in turma:
    print(a)
