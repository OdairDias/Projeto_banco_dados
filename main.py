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
comando_SQL=()
dados=pd.read_csv()
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
