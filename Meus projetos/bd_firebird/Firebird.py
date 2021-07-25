import firebirdsql
from firebirdsql.consts import DEFAULT_CHARSET
import pandas as pd

conn =firebirdsql.connect(
    user='SYSDBA',
    password='masterkey',
    database='D:\\sistemas\\fdcmarket\\dados\\elity\\FDCMARKET.FDB',
    host='localhost',
    charset='ANSI'
)

q = conn.cursor()
q.execute("SELECT * FROM cliente")
cliente = q.fetchall()
#print(cliente)

cliente_df = pd.DataFrame(cliente)
print(cliente_df)



