class Dao:
    def conexao:      
        banco = "dbname=empresa user=postgres password=postgres host=localhost port=5432"
        return psycopg2.connect(banco)
    def  buscar(id)
        conn = self.conexao()  
        cur = conn.cursor()
        cur.execute('SELECT *FROM "Funcionario" where id= %s',[id])
        res = cur.fetchall()
        func = Funcionario(res[0],res[1],res[2])
        conn.close()
        return func