aluno = {}
aluno['nome'] = 'Paulo'
aluno['idade'] = 28
nota = 'notas'
for cont in range(0, 4):
    notas = float(input("Notas do aluno: "))
    aluno.setdefault(nota, [])
    aluno[nota].append(notas)



print(aluno)