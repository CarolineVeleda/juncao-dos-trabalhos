import psycopg2

class dao:
    def __init__(self):
        self._conexao = "dbname=flask user=postgres password=postgres host=localhost port=5432"
