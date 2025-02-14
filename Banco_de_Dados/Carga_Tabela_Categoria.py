# %%
"""
Create table Categoria(
ID int,
Categoria nvarchar(255)
)

"""

# %%

import pandas as pd
import pyodbc

server = 'localhost'  # Substitua pelo nome do servidor SQL Server
database = 'Python'  # Substitua pelo nome do banco de dados
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                           f'SERVER={server};'
                           f'DATABASE={database};'
                           'Trusted_Connection=yes;')

cursor = conexaoDB.cursor()   # criando cursor de comando

# %%
dados = pd.read_excel(
    r"C:\Users\Note reserva\Desktop\Python\arquivos_excel\Categoria.xlsx")
str(dados.columns).replace("'", "")


# %%
cursor.execute('truncate table [Categoria]')  # executa tarefa de  apagar dados
cursor.commit()

# %%
for index, linha in dados.iterrows():
    cursor.execute(
        "INSERT INTO [Categoria] (ID, Categoria) VALUES (?, ?)", (linha.id, linha.nome))
    # Certifique-se de passar os valores como uma tupla

conexaoDB.commit()  # Confirmar a transação no banco de dados
cursor.close()      # Fechar o cursor
conexaoDB.close()   # Fechar a conexão


# %% [markdown]
#
