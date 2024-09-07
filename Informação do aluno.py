turma = []
aluno = {}
nota = 'notas'
print("Registro de Alunos")
while True:
    aluno['nome'] = str(input("Nome do aluno: "))
    aluno['idade'] = int(input("Idade do aluno: "))
    for cont in range(0, 4):
        notas = float(input("Notas do aluno: "))
        aluno.setdefault(nota, [])
        aluno[nota].append(notas)
    turma.append(aluno.copy())
    escolha = str(input("Gostaria de registrar mais algum aluno? [S/N]: ")).lower()
    if escolha != "s":
        break

for a in turma:
    print(a)
