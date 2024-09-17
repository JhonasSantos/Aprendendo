import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import os

conn = sqlite3.connect('dados_vendas.db')

df = pd.read_sql_query('SELECT * FROM vendas', conn)
print(df)