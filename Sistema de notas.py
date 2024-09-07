# Definindo a Var
notas = []

for (i) in range(4):
    x = float(input("Digite a nota: "))
    notas.append(x)

def calcular_media(notas):
    total = sum(notas)
    media = total/len(notas)
    return media

media = calcular_media(notas)

if media >= 7:
    print(f'\nO aluno foi aprovado com uma média de {media}')
else:
    print(f"\nPor conta da média de {media}, o aluno foi reprovado.")


