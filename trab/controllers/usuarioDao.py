class usuarioDao:

    def __init__(self):
        self._conexao = "dbname=flask user=postgres password=postgres host=localhost port=5432"

    def listar(self):
        con = psycopg2.connect(self._conexao)
        v=[]
        with con as c:
            cursor = c.cursor()
            cursor.execute('select * from usuario')
            uor l in cursor.fetchall():
                u = Usuario(l[1],l[2],l[3],l[4],l[5],l[6])
                u.cod=int(l[0])
                v.append(u)
            
        cursor.close()
        return v
    

    
    def salvar(self, u):

        verifica=hasattr(u, 'cod')

        if (verifica):
                con = psycopg2.connect(self._conexao)
                cursor = con.cursor()
                cursor.execute('UPDATE usuario SET nome = %s, login = %s, altura = %s, idade = %s, senha=%s, email=%s WHERE codusuario = %s',(u.nome,u.login,u.altura,u.idade,u.senha,u.email,u.cod))
                con.commit()
                cursor.close()


        else:
                con = psycopg2.connect(self._conexao)
                cursor = con.cursor()
                cursor.execute('insert into usuario (nome,login,altura,idade,email,senha) values (%s,%s,%s,%s,%s,%s) RETURNING codusuario', (u.nome,u.login,u.altura,u.idade,u.senha,u.email,u.cod))
                c = (cursor.fetchone())[0]
                con.commit()
                u.cod = int(c)
                cursor.close()



    def buscar(self,cod):
        con = psycopg2.connect(self._conexao)
        cursor = con.cursor()
        cursor.execute('SELECT * FROM usuario WHERE codusuario = %s',[cod])
        l = cursor.fetchone()
        u = Usuario(l[1],l[2],l[3],l[4],l[5],l[6])
        u.cod = int(l[0])
        cursor.close()
        return u


    def excluir(self,cod):

        con = psycopg2.connect(self._conexao)
        cursor = con.cursor()
        cursor.execute('DELETE FROM usuario WHERE codusuario = %s',[cod])
        con.commit()
        cursor.close()


    def login(self,login,senha):
        try:
            con = psycopg2.connect(self._conexao)
            cursor = con.cursor()
            cursor.execute('SELECT * FROM usuario WHERE login = %s and senha= %s ',(login,senha))
            l = cursor.fetchone()
            u = Usuario(l[1],l[2],l[3],l[4],l[5],l[6])
            cursor.close()
            return u
        except TypeError:
            return "O login e senha não correspondem às informações em nossos registros. Tente Novamente"

