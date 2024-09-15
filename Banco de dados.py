import pandas as pd

data = {
    'Nome': ['João', 'Ana', 'Pedro', 'Ana', 'Paulo'],
    'Itens comprados': [10, 10, 8, 10, 7],
    'Tipo de item': ['roupa', 'livro', 'livro', 'livro', 'livro'],
    'Receita total': [950, 1000, 762, 1000, 630]
}
df = pd.DataFrame(data)
print(df)


df.drop_duplicates(keep='last', inplace=True)
print(df)

df['Preço do item'] = df['Receita total'] / df['Itens comprados']
print(df['Preço do item'])

itens_acima_de_95 = df[df['Preço do item'] > 95]
print('Itens acima de 95: ')
print(itens_acima_de_95)
