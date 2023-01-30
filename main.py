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

# Execute a query
cursor.execute("CREATE DATABASE banco_crim_sp")

# Insert the data into the "crimedata" table
#dados.to_sql(name='TB_crim_sp', con=conn, if_exists='replace', index=False)

# Commit the changes
#conn.commit()

# Close the cursor and connection
#cur.close()
#conn.close()
