
import pyodbc



class Session:

    def create_session_sp(self):
        
        server = '10.62.10.44;'
        database = 'Runtime'
        username = 'grafana'
        password = 'grafan@'
        
        # String de conexão
        conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

        # Conectar ao banco de dados
        connection = pyodbc.connect(conn_str, autocommit=True)
        cursor = connection.cursor()
        return cursor, connection
    

    def create_session_digiopc(self):
        
        server = '10.192.109.93;'
        database = 'DIGIOPC'
        username = 'amsuser'
        password = 'arauco2016'
        
        # String de conexão
        conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

        # Conectar ao banco de dados
        connection = pyodbc.connect(conn_str, autocommit=True)
        cursor = connection.cursor()
        return cursor, connection
    
        