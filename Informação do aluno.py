turma = []
aluno = {}
nota = 'Notas'

def calculo(x):
    total = sum(x)
    media = total / len(aluno[nota])
    return media

print("=+"*30, "Registro de Alunos", "=+"*30)
while True:
    aluno['Nome'] = str(input("Nome do aluno: "))
    aluno['Idade'] = int(input("Idade do aluno: "))

    for cont in range(0, 4):
        notas = float(input("Notas do aluno: "))
        aluno.setdefault(nota, [])
        aluno[nota].append(notas)
    aluno['Media'] = calculo (aluno[nota])
    turma.append(aluno.copy())
    escolha = str(input("Gostaria de registrar mais algum aluno? [S/N]: ")).lower()
    
    if escolha != "s":
        break


