import psycopg2
    #sendo necessário, usar "pip install psycopg2" no terminal

class Postgre_Sql_Context:

    parametros_conexao = None
    conexao = None
    cursor = None

    def __init__(self):
        #parametros de conexão
        self.parametros_conexao = {
            'host' : "192.168.15.1",
            'port' : "5432",
            'database': "dev_rap_python",
            'user' : "postgres",
            'password': '1234'}
    
    #metodo para iniciar conexao com banco de dados
    def conectar(self):
        try:
            self.conexao = psycopg2.connect(
                host=self.parametros_conexao.get('host'),
                port=self.parametros_conexao.get('port'),
                database=self.parametros_conexao.get('database'),
                user=self.parametros_conexao.get('user'),
                password=self.parametros_conexao.get('password')
            )
        except Exception as e:
            print("Não foi possivel se conectar ao banco de dados")
            print("Erro ->", e)

    #metodo para desconectar do banco de dados
    def desconectar(self):
        if self.conexao is not None:
            self.conexao.close()
    
    def executar_update_sql(self, query):
        if self.conexao is None:
            print("Erro: Não há conexão com o banco de dados.")
        return
        
        try:
            self.cursor = self.conexao.cursor()
            self.cursor.execute(query)
            self.conexao.commit()
        except Exception as e:
            print("Erro ao executar a atualização:", e)
        finally:
            self.cursor.close()

    # Método para executar consultas SQL
    def executar_query_sql(self, query):
        if self.conexao is None:
            print("Erro: Não há conexão com o banco de dados.")
            return []
        
        try:
            self.cursor = self.conexao.cursor()
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print("Erro ao executar a consulta:", e)
            return []
        finally:
            self.cursor.close()



