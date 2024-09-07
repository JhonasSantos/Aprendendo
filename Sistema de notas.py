# Definindo a Lista onde serão guardadas as notas.
notas = []

# Loop para descrever as notas
for (i) in range(4):
    x = float(input("Digite a nota: "))
    notas.append(x)

# Função que realizará o calculo de média 
def calcular_media(notas):
    total = sum(notas)
    media = total/len(notas)
    return media

# Função anônima para arrendar a media em duas casas decimais.
arredondar_media = lambda media: round(media, 2)

# Calcular a média.
media = calcular_media(notas)
media_arredondada = arredondar_media(media)

# Exibição das notas e sua média final.
print (f"Notas do aluno: {notas}\n",end= ""f"Média final do aluno: {media}")

# Situação do aluno.
if media >= 7:
    print(f'\nO aluno foi aprovado com uma média de {media}')
else:
    print(f"\nPor conta da média de {media}, o aluno foi reprovado.")


