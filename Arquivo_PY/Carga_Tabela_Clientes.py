# %%
"""
create table Clientes(
id			int,
created_at datetime,
first_name nvarchar(255),
last_name  nvarchar(255),
email nvarchar(255),
cell_phone nvarchar(255),
country nvarchar(255),
state nvarchar(255),
street nvarchar(255),
number  nvarchar(255),
additionals  nvarchar(255)
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
                           'Trusted_Connection=yes;'
                           # 'charset=UTF-16'

                           )

cursor = conexaoDB.cursor()   # criando cursor de comando

# %%
dados = pd.read_csv(
    r"C:\Users\Note reserva\Desktop\Python\04. ETL Pandas\arquivos_csv\Clientes.csv", delimiter=',')
# str(dados.columns).replace("'","")
dados.head(5)


# %%
# Converter a coluna 'created_at' para o formato de data e hora
dados['created_at'] = pd.to_datetime(dados['created_at'])
dados['email'] = dados['email'].fillna('Sem registro')
dados['street'] = dados['street'].fillna('Sem Info')
dados['number'] = dados['number'].fillna('Sem Numero')
dados['additionals'] = dados['additionals'].fillna('Sem Info')


# %%
for coluna in dados.columns:
    print(f"Coluna: {coluna}, Tipo de dados: {dados[coluna].dtypes}")

# %% [markdown]
#

# %%
str(dados.columns).replace("'", "")  # coluna de origem

# %%
cursor.execute('truncate table  [Clientes]')  # executa tarefa de  apagar dados
cursor.commit()

# %%
# Exemplo de inserção usando tupla de parâmetros
for index, linha in dados.iterrows():
    # Converter para o tipo 'str' antes da inserção
    linha.email = str(linha.email)
    linha.country = str(linha.country)
    linha.state = str(linha.state)
    linha.street = str(linha.street)
    linha.number = str(linha.number)
    linha.additionals = str(linha.additionals)

    # linha.cell_phone = str(linha.cell_phone)
    cursor.execute("INSERT INTO [Clientes] (id, created_at,first_name, last_name,email,cell_phone,country, state,street, number, additionals) VALUES (?,?,?,?,?,?,?,?,?,?,?)", linha.id, linha.created_at, linha.first_name,
                   linha.last_name, linha.email, linha.cell_phone, linha.country, linha.state, linha.street, linha.number, linha.additionals)
cursor.commit()   # validar dados no SQL Server
cursor.close()  # Fechar Cursor
conexaoDB.close()  # Fechar Conexao
