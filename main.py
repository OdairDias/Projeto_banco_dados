import pandas as pd
import mysql.connector

# conectando com o banco
#dados=pd.read_csv('dados_trasnf')
# Connect to the database
banco = mysql.connector.connect(
    host="localhost",
    user='root',
    password="",
  
)

print(banco)
cursor = banco.cursor()

#criar variaveis a serem inseridas
comando_SQL='INSERT INTO banco_crim_sp (ANO_BO,NUM_BO,NUMERO_BOLETIM,DATAOCORRENCIA,HORAOCORRENCIA,PERIDOOCORRENCIA,DATACOMUNICACAO,BO_AUTORIA,FLAGRANTE,NUMERO_BOLETIM_PRINCIPAL,LOGRADOURO,NUMERO,BAIRRO,CIDADE,UF,LATITUDE,LONGITUDE,DESCRICAOLOCAL,EXAME,SOLUCAO,DELEGACIA_NOME,DELEGACIA_CIRCUNSCRICAO,ESPECIE,RUBRICA,DESDOBRAMENTO,STATUS,PLACA_VEICULO,UF_VEICULO,CIDADE_VEICULO,DESCR_COR_VEICULO,DESCR_MARCA_VEICULO,ANO_FABRICACAO,ANO_MODELO,DESCR_TIPO_VEICULO) VALUES($s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s,$s)'
dados=pd.read_csv('dados_roubo_veiculos_novembro_2022_completo_01.csv')
dados=dados
# Execute a query
cursor.execute(comando_SQL,dados)

# Insert the data into the "crimedata" table
#dados.to_sql(name='TB_crim_sp', con=conn, if_exists='replace', index=False)

# Commit the changes
banco.commit()

# Close the cursor and connection
#cur.close()
#conn.close()
