import sqlite3
import pandas as pd



conn = sqlite3.connect('Funcionários.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT,
               cargo TEXT,
               salario REAL
    )
''')

novo_funcionario = ('Joaquim', 'Gerente', 5000.00)
cursor.execute ("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", novo_funcionario)
conn.commit()

cursor.execute('SELECT * FROM funcionarios')
funcionarios = cursor.fetchall()
for funcionario in funcionarios:
    print(funcionario)

conn.close()


df = pd.DataFrame(funcionarios)
df.drop_duplicates(keep='last', inplace=True, ignore_index=True)
print(df)