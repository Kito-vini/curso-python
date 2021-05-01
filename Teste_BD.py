import firebirdsql 

# Conecta no seu BD #
con = firebirdsql.connect(
    host='127.0.0.1',
    database=r'C:\sistemas\fdcmarket\dados\fdcmarket.gdb',
    #port=3050,
    user='SYSDBA',
    password='masterkey',
    charset='none'
       
)

q = con.cursor()
q.execute("SELECT * FROM cliente")
clientes = q.fetchall()
print(cliente)
