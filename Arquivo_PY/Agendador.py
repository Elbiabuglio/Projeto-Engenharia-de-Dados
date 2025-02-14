

# %%
import pyodbc
import time
import schedule
import pandas as pd
schedule.clear()  # limpar todas as jobs

# %%


def job():
    server = 'localhost'
    database = 'Python'
    conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                               f'SERVER={server};'
                               f'DATABASE={database};'
                               'Trusted_Connection=yes;')

    cursor = conexaoDB.cursor()   # criando cursor de comando

    dados = pd.read_excel(
        r"C:\Users\Note reserva\Desktop\Python\arquivos_excel\Categoria.xlsx")
    str(dados.columns).replace("'", "")

    # faz carga no banco de dados
    for index, linha in dados.iterrows():

        cursor.execute(
            "Insert into [Categoria](ID,Categoria)values(?,?)", linha.id, linha.name)
    conexaoDB.close()


schedule.every(10).seconds.do(job)  # escolher a frequencia
while True:  # loop contínuo
    # Executa tarefas agendadas que estão prontas para serem executadas
    schedule.run_pending()
    # Pausa por 1 segundo antes de verificar novamente as tarefas agendadas
    time.sleep(1)

