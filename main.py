import pandas as pd
import psycopg2

# lendo arquivo
dados=pd.read_csv('dados_trasnf')
# Connect to the database
conn = psycopg2.connect(
    dbname="projeto_analise_criminalidade",
    user="postgres",
    password="odairdias78",
    host="localhost",
    port="5432"
)

# Create a cursor object
cur = conn.cursor()

# Execute a query
#cur.execute("SELECT * FROM TB_crim_sp")
# Insert the data into the "crimedata" table
dados.to_sql(name='TB_crim_sp', con=conn, if_exists='replace', index=False)

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
